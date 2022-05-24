from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, SelectField, DecimalField, StringField, BooleanField, TextAreaField


class CompaniesForm(FlaskForm):

    short_name = StringField('Skrócona nazwa:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=15, message='Pole może zawierać jedynie {} znaków!'.format(15))])

    name = TextAreaField(label='Pełna nazwa:')
    name_cont = TextAreaField(label='Pełna nazwa cd.:')

    postal_code = StringField('Kod pocztowy:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=7, message='Pole może zawierać jedynie {} znaków!'.format(7))])

    VAT_number = StringField('Numer VAT:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=15, message='Pole może zawierać jedynie {} znaków!'.format(15))])

    city = StringField('Miasto:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=25, message='Pole może zawierać jedynie {} znaków!'.format(25))])

    street = StringField('Ulica i numer domu:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=35, message='Pole może zawierać jedynie {} znaków!'.format(35))])



