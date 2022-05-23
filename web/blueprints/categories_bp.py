from flask import Blueprint, render_template, request, redirect
from db_cms.db_cms_core import db
from forms.categories_form import CategoriesForm

categories_blueprint = Blueprint('categories_blueprint', __name__)
settings = {
    'title': 'Kategorie towarów',
    'button_name': 'Dodaj nową kategorię',
    'table_headers': ['nazwa kategorii', 'dodatkowy opis']}


@categories_blueprint.route('/categories/list')
def list_tax_rates():
    list_data = db.show_all_categories()
    return render_template('simple_forms/categories.html', list_data=list_data, settings=settings)


@categories_blueprint.route('/categories/edit/<item_id>', methods=['GET', 'POST'])
def tax_rates_edit(item_id):
    id_elem = None
    form = CategoriesForm()

    if request.method == 'POST':
        id_elem = request.form.to_dict().get('element_id')
        if form.validate():
            db.edit_category(int(id_elem), {'name': form.name.data,
                                            'description': form.description.data})
            return redirect('/categories/list')
    else:
        if item_id:
            element_to_edit = db.get_unit(int(item_id))
            form.name.data = element_to_edit.name
            form.description.data = element_to_edit.description
            id_elem = element_to_edit.id
    return render_template('simple_forms/categories.html', form=form, page_state='edit', element_id=id_elem,
                           settings=settings)


@categories_blueprint.route('/categories/new', methods=['GET', 'POST'])
def tax_rates_new():
    form = CategoriesForm()
    if request.method == 'POST':
        if form.validate():
            db.add_category({'name': form.name.data,
                             'description': form.description.data})
            return redirect('/categories/list')
    return render_template('simple_forms/categories.html', form=form, page_state='new', settings=settings)
