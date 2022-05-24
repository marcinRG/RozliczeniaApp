from flask import Blueprint, render_template, request, redirect
from db_cms.db_cms_core import db
from forms.unit_form import MeasurementsUnitsForm

units_blueprint = Blueprint('units_blueprint', __name__)
settings = {
    'title': 'Jednostki miary',
    'button_name': 'Dodaj nową jednostkę miary',
    'table_headers': ['nazwa jednostki miary', 'symbol jednostki']}


@units_blueprint.route('/units/list')
def list_tax_rates():
    request_params = request.args.to_dict()
    if request_params and request_params.get('mode') == 'remove':
        id_elem = request_params.get('id_elem')
        if id_elem:
            db.remove_unit(int(id_elem))
            return redirect('/units/list')
    list_data = db.show_all_units()
    return render_template('simple_forms/units.html', list_data=list_data, settings=settings, page_state='list')


@units_blueprint.route('/units/edit/<item_id>', methods=['GET', 'POST'])
def tax_rates_edit(item_id):
    id_elem = None
    form = MeasurementsUnitsForm()

    if request.method == 'POST':
        id_elem = request.form.to_dict().get('element_id')
        if form.validate():
            db.edit_unit(int(id_elem), {'name': form.name.data,
                                        'unit_symbol': form.unit_symbol.data})
            return redirect('/units/list')
    else:
        if item_id:
            element_to_edit = db.get_unit(int(item_id))
            form.name.data = element_to_edit.name
            form.unit_symbol.data = element_to_edit.unit_symbol
            id_elem = element_to_edit.id
    return render_template('simple_forms/units.html', form=form, page_state='edit', element_id=id_elem,
                           settings=settings)


@units_blueprint.route('/units/new', methods=['GET', 'POST'])
def tax_rates_new():
    form = MeasurementsUnitsForm()
    if request.method == 'POST':
        if form.validate():
            db.add_unit({'name': form.name.data,
                         'unit_symbol': form.unit_symbol.data})
            return redirect('/units/list')
    return render_template('simple_forms/units.html', form=form, page_state='new', settings=settings)
