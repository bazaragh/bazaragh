from flask import request, redirect, abort, url_for
from flask_admin import BaseView
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import typefmt
from flask_security import current_user


class ModeratorBaseView(BaseView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                (current_user.has_role('Moderator') or current_user.has_role('Admin')))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('security.login', next=request.url))


class AdminBaseView(ModeratorBaseView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('Admin'))


class ModeratorBaseModelView(ModeratorBaseView, ModelView):
    CUSTOM_DETAIL_FORMATTERS = {
        type(None): typefmt.empty_formatter,
        bool: typefmt.bool_formatter,
        list: typefmt.list_formatter,
        dict: typefmt.dict_formatter,
    }

    column_type_formatters_detail = CUSTOM_DETAIL_FORMATTERS
    edit_template = 'admin/model/edit_custom.jinja'

    def __init__(self, *args, **kwargs):
        kwargs.pop('app')
        kwargs.pop('db')
        super(ModeratorBaseModelView, self).__init__(*args, **kwargs)


class AdminBaseModelView(AdminBaseView, ModeratorBaseModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('Admin'))
