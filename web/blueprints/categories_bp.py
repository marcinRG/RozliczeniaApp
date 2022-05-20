from flask import Blueprint, render_template, request, redirect
from db_cms.db_cms_core import db
from forms.categories_form import CategoriesForm

categories_blueprint = Blueprint('categories_blueprint', __name__)


@categories_blueprint.route('/units/list')
def list_tax_rates():
    list_data = []
    return render_template('simple_forms/index.html', list_data=list_data)


@categories_blueprint.route('/units/edit/<item_id>', methods=['GET', 'POST'])
def tax_rates_edit(item_id):
    id_elem = None
    form = CategoriesForm()
    return render_template('tax_rates.html', form=form, page_state='edit', element_id=id_elem)


@categories_blueprint.route('/taxes/new')
def tax_rates_new():
    form = CategoriesForm()
    return render_template('tax_rates.html', form=form, page_state='new')
