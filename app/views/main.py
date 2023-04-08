from flask import Blueprint, render_template
from werkzeug.exceptions import abort
from datetime import datetime
from werkzeug.exceptions import abort
from datetime import datetime

bp = Blueprint("bp_main", __name__)

# Here you can read about routing:
# https://flask.palletsprojects.com/en/2.2.x/api/#url-route-registrations
# https://hackersandslackers.com/flask-routes/

class Category:
    def __init__(self, id, name, icon):
        self.id = 1
        self.name = name
        self.icon = icon

class Offer: # temporary, change to database later
    def __init__(self, id, salesman_id, name, post_date, category, price, description, image_links, is_new):
        self.id = id
        self.salesman_id = salesman_id
        self.name = name
        self.post_date = post_date
        self.category_id = category
        self.price = price
        self.description = description
        self.image_links = image_links
        self.is_new = is_new

categories = [
    Category(1, "moda", "cat.webp"),
    Category(2, "elektronika", "cat.webp"),
    Category(3, "edukacja", "cat.webp"),
    Category(4, "zdrowie i uroda", "cat.webp"),
    Category(5, "sport", "cat.webp"),
    Category(6, "jedzenie", "cat.webp"),
    Category(7, "wnętrze", "cat.webp"),
    Category(8, "muzyka i hobby", "cat.webp"),
]

hardcoded_offers = [
    Offer(1, 100, "Prolog - najlepszy język świata", datetime(2023, 4, 3, 16, 24, 43), 3, 13.99, "Sprzedam ciągnik rolniczy URSUS 4512. Stan bardzo dobry. Pierwszy właściciel, garażowany, niskie spalanie. Pracował przy lekkich pracach - siewnik do warzyw, brony, rozdrabniacz przyczepa, opryskiwacz sadowniczy.", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(2, 100, "Prolog - najlepszy język świata 2", datetime(2023, 4, 3, 16, 24, 43), 3, 15.99, "lorem ipsum bbbbbbbbbbbbbb bbbbbbbbbbbbb bbbbbbbbbbbb", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(3, 100, "Prolog - najlepszy język świata 3", datetime(2023, 4, 3, 16, 24, 43), 3, 17.99, "lorem ipsum cccccccccc cccccccccccccc ccccccccccc najlepsza część", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(4, 100, "Prolog - najlepszy język świata 4", datetime(2023, 4, 3, 16, 24, 43), 3, 7.99, "lorem ipsum dddddddddddd dddddddddddddd ddddddddddddd", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(5, 100, "Prolog - najlepszy język świata 5", datetime(2023, 4, 3, 16, 24, 43), 8, 4.99, "lorem ipsum eeeeeeeeeeee eeeeeeeeeeeeeeeeeeeee eeeeeeeeeee proszę kupcie, już nie mogę więcej prolgoa", ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg"], False),
    Offer(6, 200, "Widzę że ktoś jest fanem prologa", datetime(2023, 4, 3, 16, 24, 43), 8, 4.99, "lorem ipsum eeeeeeeeeeee eeeeeeeeeeeeeeeeeeeee eeeeeeeeeee proszę kupcie, już nie mogę więcej prolgoa", ["https://i.ytimg.com/vi/fTJ5o_uW3eM/maxresdefault.jpg"], False),
    Offer(7, 200, "Trochę", datetime(2023, 4, 3, 16, 24, 43), 8, 4.99, "----------", ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnZZiyl1EJJji3kVQRH6O_RIg036fIgMBDyw&usqp=CAU"], False),
    Offer(8, 200, "Sus", datetime(2023, 4, 3, 16, 24, 43), 8, 4.99, "lorem ipsum eeeeeeeeeeee eeeeeeeeeeeeeeeeeeeee eeeeeeeeeee proszę kupcie, już nie mogę więcej prolgoa", ["https://jigidi-images.s3.amazonaws.com/puzzles/GIY72183CGHKQYXN.jpg"], False)
]


@bp.route('/')
def main_get():
    return render_template('main.jinja', offers=hardcoded_offers, categories=categories)

@bp.route('/offer/<int:offer_id>')
def offer_get(offer_id):
    offer = next(filter(lambda x: x.id == offer_id, hardcoded_offers), None)
    if offer is None:
        abort(404)
    return render_template('offer.jinja', offer=offer, categories=categories)
