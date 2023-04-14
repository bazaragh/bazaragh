from flask import url_for
from flask_admin.menu import MenuLink

from app import models
from app.views.admin.user import UserModelView


def admin_panel_init(app, admin, db):
    class LogoutLink(MenuLink):
        def get_url(self):
            return url_for("security.logout")

    admin.add_link(LogoutLink(name="Wyloguj się"))

    admin.add_view(UserModelView(models.User, db.session, app=app, db=db, name='Użytkownicy'))
