from flask_wtf import FlaskForm
from wtforms import validators, SelectField, DecimalField, StringField, TextAreaField, DateField
from db_cms.db_cms_core import db


class DocumentsForm(FlaskForm):
    document_title = StringField('Numer dokumentu:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=50, message='Pole może zawierać jedynie {} znaków!'.format(50))])
    date = DateField('Data dokumentu:', [
        validators.InputRequired(message='Musisz wypełnić to pole')], format='%Y-%m-%d')

    document_sum = DecimalField('Suma całości dokumentu:')

    operation_id = SelectField('Wybierz operację:', choices=db.get_operations_list())

    description = TextAreaField('Dodatkowe uwagi do dokumentu:')
