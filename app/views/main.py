import json

from flask import Blueprint, render_template
from werkzeug.exceptions import abort

from app.app import db
from app.models import Category, Offer, User

from app.utils.offer import get_offer_images_href_paths

bp = Blueprint("bp_main", __name__)
OFFERS_PER_PAGE = 8


# Here you can read about routing:
# https://flask.palletsprojects.com/en/2.2.x/api/#url-route-registrations
# https://hackersandslackers.com/flask-routes/

@bp.route('/', methods=['GET'])
def main_get():
    categories = db.session.query(Category).all()
    offers = db.session.query(Offer).order_by(Offer.created_at).limit(8).all()
    images = {}
    for offer in offers:
        offer_images = json.loads(offer.images)
        images[offer.id] = get_offer_images_href_paths(offer.id, offer_images)
    return render_template('main.jinja',
                           offers=offers,
                           categories=categories,
                           images=images)


@bp.route('/offer/<int:offer_id>', methods=['GET'])
def offer_get(offer_id):
    categories = db.session.query(Category).all()
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    images = json.loads(offer.images)
    images = get_offer_images_href_paths(offer.id, images)
    author = db.session.query(User).filter_by(id=offer.author).one_or_none()
    return render_template('offer/offer.jinja',
                        offer=offer,
                        categories=categories,
                        images=images,
                        author=author)


@bp.route('/category/<string:category_name>', methods=['GET'], defaults={'page': 1})
@bp.route('/category/<string:category_name>/<int:page>', methods=['GET'])
def category_offers(category_name, page: int = 1):
    category = db.session.query(Category).filter_by(name=category_name).one_or_none()
    if category is None:
        abort(404)

    pagination = db.session.query(Offer).filter_by(category=category.id).order_by(Offer.created_at).paginate(
        per_page=OFFERS_PER_PAGE, page=page)
    for offer in pagination.items:
        offer.images = get_offer_images_href_paths(offer.id, json.loads(offer.images))
    return render_template("category_view.jinja", category_name=category_name, pagination=pagination)

@bp.route('/user/<int:user_id>', methods=['GET'])
def user_get(user_id):
    user = db.session.query(User).filter_by(id=user_id).one_or_none()
    if user is None:
        abort(404)
    return render_template('user_view.jinja',
                        user=user)

@bp.route('/user/<int:user_id>/offers', methods=['GET'])
def user_get_offers(user_id):
    user = db.session.query(User).filter_by(id=user_id).one_or_none()
    offers = db.session.query(Offer).filter_by(author=user.id).all()
    for offer in offers:
        offer.images = get_offer_images_src_paths(offer.id, json.loads(offer.images))
    if user is None:
        abort(404)
    return render_template('user_offers_view.jinja',
                        user=user, offers=offers)