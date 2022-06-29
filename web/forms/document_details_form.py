from flask_wtf import FlaskForm
from wtforms import validators, SelectField, DecimalField, StringField, TextAreaField, DateField
from db_cms.db_cms_core import db


class DocumentDetailsForm(FlaskForm):
    item_id = SelectField('Wybierz przedmiot:', choices=db.get_items_list())

    tax_id = SelectField('Wybierz stawkę podatku:', choices=db.get_taxes_list())

    price_per_one = DecimalField('Cena za jednostkę towaru:',
                                 [validators.InputRequired(message='Musisz wypełnić to pole')])
    quantity = DecimalField('Ilość jednostek towaru:',
                            [validators.InputRequired(message='Musisz wypełnić to pole')])
    price_all = DecimalField('Wartość:')

    tax_value = DecimalField('Wartość podatku:')
