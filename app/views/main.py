from flask import Blueprint, render_template
from werkzeug.exceptions import abort
from datetime import datetime

bp = Blueprint("bp_main", __name__)


# Here you can read about routing:
# https://flask.palletsprojects.com/en/2.2.x/api/#url-route-registrations
# https://hackersandslackers.com/flask-routes/

class Offer: # temporary, change to database later
    def __init__(self, id, seller_id, name, post_date, category, price, description, image_links, is_new):
        self.id = id
        self.seller_id = seller_id
        self.name = name
        self.post_date = post_date
        self.category = category
        self.price = price
        self.description = description
        self.image_links = image_links
        self.is_new = is_new

hardcoded_offers = [
    Offer(1, 100, "Prolog - najlepszy język świata", datetime(2023, 4, 3, 16, 24, 43), "education", 13.99, "lorem ipsum aaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaa", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(2, 100, "Prolog - najlepszy język świata 2", datetime(2023, 4, 3, 16, 24, 43), "education", 15.99, "lorem ipsum bbbbbbbbbbbbbb bbbbbbbbbbbbb bbbbbbbbbbbb", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(3, 100, "Prolog - najlepszy język świata 3", datetime(2023, 4, 3, 16, 24, 43), "education", 17.99, "lorem ipsum cccccccccc cccccccccccccc ccccccccccc najlepsza część", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(4, 100, "Prolog - najlepszy język świata 4", datetime(2023, 4, 3, 16, 24, 43), "education", 7.99, "lorem ipsum dddddddddddd dddddddddddddd ddddddddddddd", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(5, 100, "Prolog - najlepszy język świata 5", datetime(2023, 4, 3, 16, 24, 43), "entertainment", 4.99, "lorem ipsum eeeeeeeeeeee eeeeeeeeeeeeeeeeeeeee eeeeeeeeeee proszę kupcie, już nie mogę więcej prolgoa", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False)
]


@bp.route('/')
def main_get():
    return render_template('main.jinja', offers=hardcoded_offers)

@bp.route('/offer/<int:offer_id>')
def offer_get(offer_id):
    offer = next(filter(lambda x: x.id == offer_id, hardcoded_offers), None)
    if offer is None:
        abort(404)
    return render_template('offer.jinja', offer=offer)
