from flask import Blueprint, render_template, request, redirect
from db_cms.db_cms_core import db
from forms.tax_rates_form import TaxRatesForm

tax_rates_blueprint = Blueprint('tax_rates_blueprint', __name__)
settings = {
    'title': 'Stawki podatku',
    'button_name': 'Dodaj nową stawkę',
    'table_headers': ['#', 'nazwa jednostki miary', 'symbol jednostki', 'operacje']}


@tax_rates_blueprint.route('/taxes/list')
def list_tax_rates():
    list_data = db.show_all_tax_rates()
    return render_template('simple_forms/index.html', list_data=list_data)


@tax_rates_blueprint.route('/taxes/edit/<item_id>', methods=['GET', 'POST'])
def tax_rates_edit(item_id):
    id_elem = None
    form = TaxRatesForm()

    if request.method == 'POST':
        id_elem = request.form.to_dict().get('element_id')
        if form.validate():
            db.edit_tax_rate(int(id_elem), {'name': form.name.data,
                                            'symbol': form.symbol.data,
                                            'rate': form.rate.data / 100,
                                            'default': form.default.data})
            return redirect('/taxes/list')
    else:
        if item_id:
            element_to_edit = db.get_tax_rate(int(item_id))
            form.name.data = element_to_edit.name
            form.symbol.data = element_to_edit.symbol
            form.rate.data = int(element_to_edit.rate * 100)
            form.default.data = element_to_edit.default
            id_elem = element_to_edit.id
    print(id_elem)
    return render_template('tax_rates.html', form=form, page_state='edit', element_id=id_elem)


@tax_rates_blueprint.route('/taxes/new')
def tax_rates_new():
    form = TaxRatesForm()
    return render_template('tax_rates.html', form=form, page_state='new')
