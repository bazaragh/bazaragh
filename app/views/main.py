from flask import Blueprint, render_template

bp = Blueprint("bp_main", __name__)
categories = {
    " moda ": "cat.webp",
    "elektronika": "cat.webp",
    "edukacja": "cat.webp",
    "zdrowie i uroda": "cat.webp",
    " sport ": "cat.webp",
    " jedzenie ": "cat.webp",
    "wnętrze": "cat.webp",
    "muzyka i hobby": "cat.webp",
}

prom_pub = [
    ("Piwo paliwo", "21.07.2022", "4.2", "cat.webp"),
    ("Kustosz teqilla", "01.03.2023", "4.99", "cat.webp"),
    ("Notateczki z ISI", "03.03.2023", "49.99", "cat.webp"),
    ("Stara zniszczona bluza agh", "03.04.2023", "89.99", "cat.webp"),
]

# Here you can read about routing:
# https://flask.palletsprojects.com/en/2.2.x/api/#url-route-registrations
# https://hackersandslackers.com/flask-routes/


@bp.route('/')
def main_get():
    return render_template('main.jinja', categories=categories, publications=prom_pub)
