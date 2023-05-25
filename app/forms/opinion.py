from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class OpinionForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(max=255), Email()], render_kw={'readonly': False})
    contents = TextAreaField('Treść wiadomości', validators=[InputRequired()])
    submit = SubmitField('Wyślij')
