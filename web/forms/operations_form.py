from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, SelectField, DecimalField, StringField, BooleanField, TextAreaField


class CategoriesForm(FlaskForm):

    name = StringField('Podaj nazwę operacji:', [
        validators.InputRequired(message='Musisz wypełnić to pole'),
        validators.Length(max=15, message='Pole może zawierać jedynie {} znaków!'.format(15))])
