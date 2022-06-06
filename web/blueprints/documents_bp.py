from flask import Blueprint, render_template, request, redirect

from db_cms.db_cms_core import db
from forms.documents_form import DocumentsForm

documents_blueprint = Blueprint('documents_blueprint', __name__)

settings = {
    'title': 'Dokumnety',
    'button_name': 'Dodaj nowy dokument',
    'table_headers': ['data', 'nr dokumentu', 'przychód/rozchód', 'suma']}


@documents_blueprint.route('/documents/list')
def documents_list():
    request_params = request.args.to_dict()
    if request_params and request_params.get('mode') == 'remove':
        id_elem = request_params.get('id_elem')
        if id_elem:
            db.remove_document(int(id_elem))
            return redirect('/documents/list')
    list_data = db.show_all_documents()
    return render_template('custom_forms/documents.html', settings=settings, page_state='list', list_data=list_data)


@documents_blueprint.route('/documents/edit/<item_id>')
def edit_document(item_id):
    id_elem = None
    form = DocumentsForm()

    if request.method == 'POST':
        id_elem = request.form.to_dict().get('element_id')
        if form.validate():
            db.edit_document(int(id_elem), {'document_title': form.document_title.data,
                                            'date': form.date.data,
                                            'operation_id': form.operation_id.data,
                                            'document_sum': form.document_sum.data,
                                            'description': form.description.data})
            return redirect('/documents/list')
    else:
        if item_id:
            element_to_edit = db.get_document(int(item_id))

            form.document_title.data = element_to_edit.document_title
            form.date.data = element_to_edit.date
            form.operation_id.data = element_to_edit.operation_id
            form.document_sum.data = element_to_edit.document_sum
            form.description.data = element_to_edit.description
            id_elem = element_to_edit.id

    return render_template('custom_forms/documents.html', form=form, page_state='edit', element_id=id_elem,
                           settings=settings)


@documents_blueprint.route('/documents/new', methods=['POST', 'GET'])
def new_document():
    form = DocumentsForm()
    if request.method == 'POST' and form.validate():
        print(request.form.to_dict())
        db.add_document({
            'document_title': form.document_title.data,
            'date': form.date.data,
            'document_sum': form.document_sum.data,
            'operation_id': form.operation_id.data,
            'description': form.description.data
        })
    return render_template('custom_forms/documents.html', form=form)


@documents_blueprint.route('/documents/details/<item_id>')
def documents_details(item_id):
    return 'document details'
