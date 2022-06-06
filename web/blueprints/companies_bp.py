from flask import Blueprint, render_template, request, redirect
from db_cms.db_cms_core import db
from forms.company_form import CompaniesForm

companies_blueprint = Blueprint('companies_blueprint', __name__)
settings = {
    'title': 'Kontrahenci',
    'button_name': 'Dodaj nową firmę',
    'table_headers': ['skrócona nazwa', 'nazwa', 'kod pocztowy', 'miasto', 'Nr VAT']}


@companies_blueprint.route('/companies/list')
def list_tax_rates():
    request_params = request.args.to_dict()
    if request_params and request_params.get('mode') == 'remove':
        id_elem = request_params.get('id_elem')
        if id_elem:
            db.remove_company(int(id_elem))
            return redirect('/companies/list')
    list_data = db.show_all_companies()
    return render_template('custom_forms/companies.html', list_data=list_data, settings=settings, page_state='list')


@companies_blueprint.route('/companies/edit/<item_id>', methods=['GET', 'POST'])
def tax_rates_edit(item_id):
    id_elem = None
    form = CompaniesForm()

    if request.method == 'POST':
        id_elem = request.form.to_dict().get('element_id')
        if form.validate():
            db.edit_company(int(id_elem), {'name': form.name.data,
                                           'short_name': form.short_name.data,
                                           'VAT_number': form.VAT_number.data,
                                           'name_cont': form.name_cont.data,
                                           'postal_code': form.postal_code.data,
                                           'city': form.city.data,
                                           'street': form.street.data})
            return redirect('/companies/list')
    else:
        if item_id:
            element_to_edit = db.get_company(int(item_id))
            form.short_name.data = element_to_edit.short_name
            form.VAT_number.data = element_to_edit.VAT_number
            form.name.data = element_to_edit.name
            form.name_cont.data = element_to_edit.name_cont
            form.postal_code.data = element_to_edit.postal_code
            form.city.data = element_to_edit.city
            form.street.data = element_to_edit.street
            id_elem = element_to_edit.id
    return render_template('simple_forms/companies.html', form=form, page_state='edit', element_id=id_elem,
                           settings=settings)


@companies_blueprint.route('/companies/new', methods=['GET', 'POST'])
def tax_rates_new():
    form = CompaniesForm()
    if request.method == 'POST':
        if form.validate():
            db.add_company({'name': form.name.data,
                            'short_name': form.short_name.data,
                            'VAT_number': form.VAT_number.data,
                            'name_cont': form.name_cont.data,
                            'postal_code': form.postal_code.data,
                            'city': form.city.data,
                            'street': form.street.data})
            return redirect('/companies/list')
    return render_template('simple_forms/companies.html', form=form, page_state='new', settings=settings)
