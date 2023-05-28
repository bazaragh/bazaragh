import decimal

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField, SelectField, BooleanField, MultipleFileField, FormField, FieldList
from wtforms.validators import Length, DataRequired, NumberRange, Optional, StopValidation
from werkzeug.datastructures import FileStorage
from collections.abc import Iterable

from app.app import ALLOWED_IMAGE_EXTENSIONS


class MultiFileAllowed(object):

    def __init__(self, upload_set, message=None):
        self.upload_set = upload_set
        self.message = message

    def __call__(self, form, field):

        field.data = [file for file in field.data if file.filename and file.filename != '']
        if not (all(isinstance(item, FileStorage) for item in field.data) and field.data):
            return

        for data in field.data:
            filename = data.filename.lower()

            if isinstance(self.upload_set, Iterable):
                if any(filename.endswith('.' + x) for x in self.upload_set):
                    continue

                raise StopValidation(self.message or field.gettext(
                    'File does not have an approved extension: {extensions}'
                ).format(extensions=', '.join(self.upload_set)))

            if not self.upload_set.file_allowed(field.data, filename):
                raise StopValidation(self.message or field.gettext(
                    'File does not have an approved extension.'
                ))

class OfferImageDeleteForm(FlaskForm):
    should_delete = BooleanField("Usuń zdjęcie")
    image_href_path = StringField('Ścieżka do zdjęcia')


class AddEditOfferForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired(message='Tytuł ogłoszenia jest wymagany'), Length(max=128)])
    description = TextAreaField('Opis', [Length(max=4096)])
    price = DecimalField('Cena', validators=[Optional(), NumberRange(min=0, max=None)],
                         description="Zostaw puste, by wystawić darmową ofertę", places=2, rounding=decimal.ROUND_UP)
    category = SelectField("Kategoria", validators=[DataRequired(message='Kategoria ogłoszenia jest wymagana')])
    is_used = BooleanField("Przedmiot używany")
    images = MultipleFileField("Dodaj zdjęcia", validators=[MultiFileAllowed(ALLOWED_IMAGE_EXTENSIONS, "Dozwolone są pliki w formacie jpg, jpeg lub png")])
    existing_images = FieldList(FormField(OfferImageDeleteForm), min_entries=0)
    submit = SubmitField("Potwierdź")


class DeleteOfferForm(FlaskForm):
    submit = SubmitField("Potwierdź")
