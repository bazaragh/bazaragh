from app.views.admin.base import ModeratorBaseModelView


class DormitoryModelView(ModeratorBaseModelView):
    can_view_details = False
    can_create = True
    can_edit = True
    can_delete = True

    column_labels = {
        'name': 'Nazwa',
        'address': 'Adres'
    }

    column_formatters = {
        'address': lambda v, c, m, p: "Brak informacji" if m.address is "" else m.address
    }
