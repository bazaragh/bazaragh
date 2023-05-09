import decimal

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, DecimalField, SubmitField, SelectField, BooleanField, MultipleFileField
from wtforms.validators import Length, DataRequired, NumberRange, Optional


class AddEditOfferForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired(message='Tytuł ogłoszenia jest wymagany'), Length(max=128)])
    description = TextAreaField('Opis', [Length(max=4096)])
    price = DecimalField('Cena', validators=[Optional(), NumberRange(min=0, max=None)],
                         description="Zostaw puste, by wystawić darmową ofertę", places=2, rounding=decimal.ROUND_UP)
    category = SelectField("Kategoria", validators=[DataRequired(message='Kategoria ogłoszenia jest wymagana')])
    is_used = BooleanField("Przedmiot używany")
    images = MultipleFileField("Dodaj zdjęcia", validators=[FileAllowed(['jpg', 'png', 'jpeg'], "Dozwolone są pliki w formacie jpg, jpeg lub png")])
    submit = SubmitField("Potwierdź")


class DeleteOfferForm(FlaskForm):
    submit = SubmitField("Potwierdź")
