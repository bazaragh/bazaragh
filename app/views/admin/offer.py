import json

from app.views.admin.base import ModeratorBaseModelView

from app.app import db
from app.models import User, Category


class OfferModelView(ModeratorBaseModelView):
    can_view_details = True
    details_template = 'admin/model/offer_details.html'
    can_create = False
    can_edit = False
    can_delete = True
    column_list = ['title', 'author', 'category', 'created_at']
    column_default_sort = ('created_at', True)
    column_labels = {
        'author': 'Autor',
        'description': 'Opis',
        'category': 'Kategoria',
        'title': 'Tytuł',
        'created_at': 'Data utworzenia',
        'price': 'Cena',
        'is_used': 'Używany?',
        'images': 'Zdjęcia'
    }

    column_formatters = {
        'author': lambda v, c, m, p: db.session.query(User).filter_by(id=m.author).one(),
        'description': lambda v, c, m, p: "brak" if m.description is (None or "") else m.description,
        'category': lambda v, c, m, p: db.session.query(Category).filter_by(id=m.category).one(),
        'price': lambda v, c, m, p: "Za darmo" if m.price is None else f"{m.price} zł",
        'is_used': lambda v, c, m, p: 'Tak' if m.is_used == 1 else 'Nie',
        'images': lambda v, c, m, p: json.loads(m.images),
    }
