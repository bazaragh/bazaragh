from flask import current_app, render_template
from flask_login import current_user
from flask_mailman import EmailMessage
from sqlalchemy import null
from wtforms import ValidationError
from wtforms.fields import SelectField
from wtforms.validators import Optional

from app.models import Dormitory, Faculty
from app.views.admin.base import AdminBaseModelView


def get_dorms(app, db):
    with app.app_context():
        dorms = [(dorm.id, f"{dorm.id} {dorm.name}" if not dorm.id == "None" else dorm.name)
                 for dorm in db.session.query(Dormitory).all()]
        dorms.sort(key=lambda x: int(x[0][2:].replace("DS", "0").replace("ne", "-1").strip()))
        return dorms


def get_faculties(app, db):
    with app.app_context():
        return [(faculty.id, faculty.name) for faculty in db.session.query(Faculty).all()]


class UserModelView(AdminBaseModelView):
    can_view_details = True
    can_create = False
    can_edit = True
    can_delete = True

    column_default_sort = ('id', True)

    column_list = [
        'email', 'active', 'dorm', 'faculty', 'current_login_at'
    ]

    column_details_list = [
        'email', 'active', 'create_datetime', 'confirmed_at', 'dorm', 'faculty', 'current_login_at'
    ]

    form_columns = [
        'email', 'roles', 'active', 'dorm', 'faculty'
    ]

    column_labels = {
        'active': 'Aktywny',
        'current_login_at': 'Ostatnie logowanie',
        'current_login_ip': 'Ostatni adres IP',
        'create_datetime': 'Rejestracja',
        'confirmed_at': 'Aktywacja linkiem',
        'roles': 'Role',
        'dorm': 'Akademik',
        'faculty': 'Wydział'
    }

    form_overrides = {
        'dorm': SelectField,
        'faculty': SelectField
    }

    def __init__(self, *args, **kwargs):
        self.form_args = {
            'dorm': {
                'choices': get_dorms(kwargs.get('app'), kwargs.get('db'))
            },
            'faculty': {
                'choices': get_faculties(kwargs.get('app'), kwargs.get('db'))
            }
        }
        super().__init__(*args, **kwargs)

    def on_model_change(self, form, model, is_created):
        if not current_user.has_role('Admin'):
            raise ValidationError('Nie możesz pozbawić się roli Admin, poproś innego administratora o zmianę.')

    def on_model_delete(self, model):
        if current_user.id == model.id:
            raise ValidationError('Nie możesz usunąć swojego konta.')

    def after_model_delete(self, model):
        content = "Administrator usunął twoje konto"
        message = EmailMessage(subject="Twoje konto zostało usunięte",
                               body=render_template('admin/email/delete_user.html', user=model),
                               from_email=current_app.config['MAIL_DEFAULT_SENDER'],
                               to=[model.email],
                               bcc=[current_app.config['MAIL_USERNAME']])
        message.content_subtype = "html"
        message.send()
