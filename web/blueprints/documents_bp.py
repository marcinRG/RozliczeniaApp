from flask import Blueprint, render_template, request, redirect

from db_cms.db_cms_core import db
from forms.documents_form import DocumentsForm

documents_blueprint = Blueprint('documents_blueprint', __name__)


@documents_blueprint.route('/documents/list')
def documents_list():
    print(db.show_all_documents())
    return 'documents list'


@documents_blueprint.route('/documents/edit/<item_id>')
def edit_document(item_id):
    return 'edit document'


@documents_blueprint.route('/documents/new', methods=['POST','GET'])
def new_document():
    form = DocumentsForm()
    if request.method == 'POST' and form.validate():
        print(request.form.to_dict())
        db.add_document({
            'document_title': form.document_title.data,
            'date': form.date.data,
            'document_sum': form.document_sum.data,
            'operation_id':form.operation_id.data,
            'description': form.description.data
        })
    return render_template('documents.html', form=form)


@documents_blueprint.route('/documents/details/<item_id>')
def documents_details(item_id):
    return 'document details'
