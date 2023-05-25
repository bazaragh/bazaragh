from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import DataRequired

from app.app import ALLOWED_IMAGE_EXTENSIONS


class AddUserProfilePicture(FlaskForm):
    image = FileField("Dodaj zdjęcie profilowe", validators=[DataRequired(message='Zdjęcie jest wymagane'),
                                                             FileAllowed(ALLOWED_IMAGE_EXTENSIONS, "Dozwolone są pliki w formacie jpg, jpeg lub png")])
    submit = SubmitField("Potwierdź")
