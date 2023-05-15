from app.views.admin.base import ModeratorBaseModelView


class FacultyModelView(ModeratorBaseModelView):
    can_view_details = False
    can_create = True
    can_edit = True
    can_delete = True

    column_labels = {
        'name': 'Nazwa'
    }
