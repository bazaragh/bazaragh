from flask_login import current_user
from wtforms import ValidationError
from wtforms.fields import SelectField

from app.models import Dormitory, Faculty
from app.views.admin.base import AdminBaseModelView


def get_dorms(app, db):
    with app.app_context():
        dorms = [(dorm.id, f"{dorm.id} {dorm.name}") for dorm in db.session.query(Dormitory).all()]
        dorms.sort(key=lambda x: int(x[0][2:].replace("DS", "0").strip()))
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
        'email', 'active', 'create_datetime', 'confirmed_at', 'current_login_at'
    ]

    column_details_list = [
        'email', 'active', 'current_login_at', 'current_login_ip', 'create_datetime', 'confirmed_at', 'dorm', 'faculty'
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

    # FIXME: save null to db
    def __init__(self, *args, **kwargs):
        self.form_args = {
            'dorm': {
                'choices': [('null', 'Mieszka poza Miasteczkiem Studenckim AGH'),
                            *get_dorms(kwargs.get('app'), kwargs.get('db'))]
            },
            'faculty': {
                'choices': [('null', 'Studiuje poza AGH'),
                            *get_faculties(kwargs.get('app'), kwargs.get('db'))]
            }
        }
        super().__init__(*args, **kwargs)

    def on_model_change(self, form, model, is_created):
        if not current_user.has_role('Admin'):
            raise ValidationError('Nie możesz pozbawić się roli Admin, poproś innego administratora o zmianę.')
