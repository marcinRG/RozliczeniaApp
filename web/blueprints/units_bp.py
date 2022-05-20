from flask import Blueprint, render_template, request, redirect
from db_cms.db_cms_core import db
from forms.unit_form import MeasurementsUnitsForm

units_blueprint = Blueprint('units_blueprint', __name__)
settings = {
    'title': 'Jednostki miary',
    'button_name': 'Dodaj nową jednostkę miary',
    'table_headers': ['#', 'nazwa jednostki miary', 'symbol jednostki', 'operacje']}


@units_blueprint.route('/units/list')
def list_tax_rates():
    list_data = []
    return render_template('simple_forms/index.html', list_data=list_data)


@units_blueprint.route('/units/edit/<item_id>', methods=['GET', 'POST'])
def tax_rates_edit(item_id):
    id_elem = None
    form = MeasurementsUnitsForm()
    return render_template('tax_rates.html', form=form, page_state='edit', element_id=id_elem)


@units_blueprint.route('/taxes/new')
def tax_rates_new():
    form = MeasurementsUnitsForm()
    return render_template('tax_rates.html', form=form, page_state='new')
