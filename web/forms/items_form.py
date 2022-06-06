from flask_wtf import FlaskForm
from wtforms import validators, SelectField, DecimalField, StringField, TextAreaField, DateField
from db_cms.db_cms_core import db


class ItemsForm(FlaskForm):
    short_name = StringField('Nazwa skrócona:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=15, message='Pole może zawierać jedynie {} znaków!'.format(15))])

    name = StringField('Nazwa pełna:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=80, message='Pole może zawierać jedynie {} znaków!'.format(80))])

    category_id = SelectField('Wybierz kategorię towaru:', choices=db.get_categories_list())
    measurement_id = SelectField('Wybierz jednostkę miary:', choices=db.get_measurement_units_list())
