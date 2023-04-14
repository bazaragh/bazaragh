from flask_security.forms import RegisterForm, ConfirmRegisterForm, get_form_field_label, EqualTo
from wtforms import StringField, PasswordField, validators, SelectField
from wtforms.validators import DataRequired, Length

dorm_list = [("other", "Mieszkam poza MS AGH"),
             ("ds-alfa", "DS Alfa"),
             ("ds-1", "DS1 Olimp"),
             ("ds-2", "DS2 Babilon"),
             ("ds-3", "DS3 Akropol"),
             ("ds-4", "DS4 Filutek"),
             ("ds-5", "DS5 Strumyk"),
             ("ds-6", "DS6 Bratek"),
             ("ds-7", "DS7 Zaścianek"),
             ("ds-8", "DS8 Stokrotka"),
             ("ds-9", "DS9 Omega"),
             ("ds-10", "DS10 Hajduczek"),
             ("ds-11", "DS11 Bonus"),
             ("ds-12", "DS12 Pomyk"),
             ("ds-13", "DS13 Straszny Dwór"),
             ("ds-14", "DS14 Kapitol"),
             ("ds-15", "DS15 Maraton"),
             ("ds-16", "DS16 Itaka"),
             ("ds-17", "DS17 Arkadia"),
             ("ds-18", "DS18 Odyseja"),
             ("ds-19", "DS19 Apollo")]


class Select2Field(SelectField):
    def pre_validate(self, form):
        pass


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('Imię', validators=[DataRequired(message='Your first name is required.'),
                                                 Length(max=255)])
    last_name = StringField('Nazwisko', validators=[DataRequired(message='Your first name is required.'),
                                                    Length(max=255)])
    faculty = StringField('Wydział')
    dorm = Select2Field('Akademik', choices=dorm_list)
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
    faculty = StringField('Wydział')
    dorm = Select2Field('Akademik', choices=dorm_list)
    password = PasswordField(
        get_form_field_label("password"),
        validators=[
            EqualTo("password", message="RETYPE_PASSWORD_MISMATCH"),
            validators.InputRequired(),
            validators.Length(min=10)
        ],
    )
