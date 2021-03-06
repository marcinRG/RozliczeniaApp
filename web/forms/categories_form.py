from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, SelectField, DecimalField, StringField, BooleanField, TextAreaField


class CategoriesForm(FlaskForm):

    name = StringField('Podaj nazwę kategorii:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=35, message='Pole może zawierać jedynie {} znaków!'.format(3))])

    description = TextAreaField(label='Dodatkowy opis:')


