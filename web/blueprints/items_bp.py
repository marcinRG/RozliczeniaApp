from flask import Blueprint, render_template, request, redirect

from db_cms.db_cms_core import db
from forms.items_form import ItemsForm

items_blueprint = Blueprint('items_blueprint', __name__)

settings = {
    'title': 'Towary',
    'button_name': 'Dodaj nowy towar',
    'table_headers': ['skrócona nazwa', 'pełna nazwa', 'kategoria', 'jednostka miary']}


@items_blueprint.route('/items/list')
def items_list():
    request_params = request.args.to_dict()
    if request_params and request_params.get('mode') == 'remove':
        id_elem = request_params.get('id_elem')
        if id_elem:
            db.remove_item(int(id_elem))
            return redirect('/items/list')
    list_data = db.show_all_items()
    return render_template('custom_forms/items.html', settings=settings, page_state='list', list_data=list_data)


@items_blueprint.route('/items/edit/<item_id>')
def edit_item(item_id):
    id_elem = None
    form = ItemsForm()

    if request.method == 'POST':
        id_elem = request.form.to_dict().get('element_id')
        if form.validate():
            db.edit_unit(int(id_elem), {'name': form.name.data,
                                        'short_name': form.short_name.data,
                                        'category_id': form.category_id.data,
                                        'measurement_id': form.measurement_id.data})
            return redirect('/items/list')
    else:
        if item_id:
            element_to_edit = db.get_item(int(item_id))
            form.name.data = element_to_edit.name
            form.short_name.data = element_to_edit.short_name
            form.category_id.data = element_to_edit.category_id
            form.measurement_id.data = element_to_edit.measurement_id
            id_elem = element_to_edit.id

    return render_template('custom_forms/items.html', form=form, page_state='edit', element_id=id_elem,
                           settings=settings)


@items_blueprint.route('/items/new', methods=['POST', 'GET'])
def new_item():
    form = ItemsForm()
    if request.method == 'POST':
        if form.validate():
            db.add_item({'name': form.name.data,
                         'short_name': form.short_name.data,
                         'category_id': form.category_id.data,
                         'measurement_id': form.measurement_id.data})
            return redirect('/items/list')
    return render_template('custom_forms/items.html', form=form, page_state='new', settings=settings)
