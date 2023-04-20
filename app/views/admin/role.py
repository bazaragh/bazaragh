from flask_security import current_user
from wtforms import ValidationError

from app.views.admin.base import AdminBaseModelView
from flask_admin.contrib.sqla.view import func


class RoleModelView(AdminBaseModelView):
    can_create = False
    can_edit = True
    can_delete = False
    column_list = ['name']
    form_columns = ['users', 'update_datetime']
    column_labels = {
        'name': 'Nazwa',
        'users': 'Członkowie grupy',
        'update_datetime': 'Data edycji'
    }

    def get_query(self):
        return self.session.query(self.model).filter(self.model.name != 'Resident')

    def get_count_query(self):
        return self.session.query(func.count('*')).select_from(self.model).filter(self.model.name != 'Resident')

    def on_model_change(self, form, model, is_created):
        if not current_user.has_role('Admin'):
            # Tylko admin ma dostęp do edycji ról, więc użytkownik się pozbawił praw administratora
            raise ValidationError('Nie możesz pozbawić się tej roli, poproś innego administratora o zmianę.')
