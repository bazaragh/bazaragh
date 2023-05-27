from flask_security.forms import RegisterForm, ConfirmRegisterForm, get_form_field_label, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional


class Select2Field(SelectField):
    def pre_validate(self, form):
        pass


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('Imię', validators=[DataRequired(message='Your first name is required.'),
                                                 Length(max=255)])
    last_name = StringField('Nazwisko', validators=[DataRequired(message='Your first name is required.'),
                                                    Length(max=255)])
    faculty = Select2Field('Wydział', choices=[(None, "Studiuję poza AGH")], validators=[Optional()])
    dorm = Select2Field('Akademik', choices=[(None, "Mieszkam poza MS AGH")], validators=[Optional()])
    password_confirm = PasswordField(
        get_form_field_label("retype_password"),
        validators=[
            EqualTo("password", message="RETYPE_PASSWORD_MISMATCH"),
            validators.InputRequired(),
            validators.Length(min=10)
        ],
    )


class ExtendedConfirmRegisterForm(ConfirmRegisterForm):
    first_name = StringField('Imię', validators=[DataRequired(message='Your first name is required.'),
                                                 Length(max=255)])
    last_name = StringField('Nazwisko', validators=[DataRequired(message='Your first name is required.'),
                                                    Length(max=255)])
    faculty = Select2Field('Wydział', choices=[(None, "Studiuję poza AGH")], validators=[Optional()])
    dorm = Select2Field('Akademik', choices=[(None, "Mieszkam poza MS AGH")], validators=[Optional()])
    password = PasswordField(
        get_form_field_label("password"),
        validators=[
            EqualTo("password", message="RETYPE_PASSWORD_MISMATCH"),
            validators.InputRequired(),
            validators.Length(min=10)
        ],
    )


class ChangeEmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=255)])
    submit = SubmitField("Potwierdź")


class DeleteAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=255)])
    submit = SubmitField("Usuń konto")
