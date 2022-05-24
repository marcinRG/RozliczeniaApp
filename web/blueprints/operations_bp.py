from flask import Blueprint, render_template, request, redirect
from db_cms.db_cms_core import db
from forms.operations_form import OperationsForm

operations_blueprint = Blueprint('operations_blueprint', __name__)
settings = {
    'title': 'Operacje',
    'button_name': 'Dodaj nową operację',
    'table_headers': ['nazwa operacji']}


@operations_blueprint.route('/operations/list')
def list_tax_rates():
    request_params = request.args.to_dict()
    if request_params and request_params.get('mode') == 'remove':
        id_elem = request_params.get('id_elem')
        if id_elem:
            db.remove_operation(int(id_elem))
            return redirect('/operations/list')
    list_data = db.show_all_operations()
    return render_template('simple_forms/operations.html', list_data=list_data, settings=settings, page_state='list')


@operations_blueprint.route('/operations/edit/<item_id>', methods=['GET', 'POST'])
def tax_rates_edit(item_id):
    id_elem = None
    form = OperationsForm()

    if request.method == 'POST':
        id_elem = request.form.to_dict().get('element_id')
        if form.validate():
            db.edit_operation(int(id_elem), {'name': form.name.data})
            return redirect('/operations/list')
    else:
        if item_id:
            element_to_edit = db.get_operation(int(item_id))
            form.name.data = element_to_edit.name
            id_elem = element_to_edit.id
    return render_template('simple_forms/operations.html', form=form, page_state='edit', element_id=id_elem,
                           settings=settings)


@operations_blueprint.route('/operations/new', methods=['GET', 'POST'])
def tax_rates_new():
    form = OperationsForm()
    if request.method == 'POST':
        if form.validate():
            db.add_operation({'name': form.name.data})
            return redirect('/operations/list')
    return render_template('simple_forms/operations.html', form=form, page_state='new', settings=settings)
