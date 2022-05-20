from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, SelectField, DecimalField, StringField, BooleanField, TextAreaField


class MeasurementsUnitsForm(FlaskForm):

    name = StringField('Podaj nazwę jednostki miary:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=35, message='Pole może zawierać jedynie {} znaków!'.format(35))])

    unit_symbol = StringField('Podaj symbol jednostki miary:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=3, message='Pole może zawierać jedynie {} znaków!'.format(3))])
