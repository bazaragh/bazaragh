import decimal

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import Length, DataRequired, NumberRange, Optional


class AddEditOfferForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired(message='Tytuł ogłoszenia jest wymagany'), Length(max=128)])
    description = TextAreaField('Opis', [Length(max=4096)])
    price = DecimalField('Cena', validators=[Optional(), NumberRange(min=0, max=None)],
                         description="Zostaw puste, by wystawić darmową ofertę", places=2, rounding=decimal.ROUND_UP)
    submit = SubmitField("Potwierdź")


class DeleteOfferForm(FlaskForm):
    submit = SubmitField("Potwierdź")
