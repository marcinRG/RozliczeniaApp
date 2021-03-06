from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, SelectField, DecimalField, StringField, BooleanField


class TaxRatesForm(FlaskForm):
    name = StringField('Podaj nazwę stawki:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=35, message='Pole może zawierać jedynie {} znaków!'.format(35))])

    symbol = StringField('Podaj symbol stawki:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=3, message='Pole może zawierać jedynie {} znaków!'.format(3))])

    rate = IntegerField(label='Podaj wysokość stawki w procentach:', validators=[
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.NumberRange(message='Podana wartość musi być z przediału 0-100', min=0, max=100)])

    default = BooleanField('Domyślna stawka podatku')
