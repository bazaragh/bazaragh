from flask_login import current_user
from wtforms import ValidationError

from app.app import db
from app.models import Dormitory, Faculty
from app.views.admin.base import AdminBaseModelView


def query_table(model: db.Model, elem_id: str):
    return db.session.query(model).filter_by(id=elem_id).one_or_none()


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
    column_formatters = {
        'dorm': lambda v, c, m, p: f"{m.dorm} {query_table(Dormitory, m.dorm)}"
        if query_table(Dormitory, m.dorm) is not None else "Brak",
        'faculty': lambda v, c, m, p: f"({m.faculty}) {query_table(Faculty, m.faculty)}"
        if query_table(Faculty, m.faculty) is not None else "Brak"
    }

    def on_model_change(self, form, model, is_created):
        if not current_user.has_role('Admin'):
            raise ValidationError('Nie możesz pozbawić się roli Admin, poproś innego administratora o zmianę.')
