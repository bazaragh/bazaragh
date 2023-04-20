from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import Length, DataRequired, NumberRange


class AddEditOfferForm(FlaskForm):
    title = StringField('Tytuł', [DataRequired(message='Tytuł ogłoszenia jest wymagany'), Length(max=128)])
    description = TextAreaField('Opis', [Length(max=4096)])
    price = DecimalField('Cena', [NumberRange(min=0, max=None)])
    submit = SubmitField("Potwierdź")


class DeleteOfferForm(FlaskForm):
    submit = SubmitField("Potwierdź")
