from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class OpinionForm(FlaskForm):
    contents = TextAreaField('Treść wiadomości', validators=[InputRequired()])
    submit = SubmitField('Wyślij')
