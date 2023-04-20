import json
from MySQLdb import IntegrityError

from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user
from flask_security import auth_required
from flask_security.utils import url_for_security
from werkzeug.exceptions import abort
from datetime import datetime

from app.app import db
from app.models import Category, Offer, User

from app.forms.offer import AddEditOfferForm
from app.forms.security import ChangeEmailForm, DeleteAccountForm

bp = Blueprint("bp_main", __name__)


# Here you can read about routing:
# https://flask.palletsprojects.com/en/2.2.x/api/#url-route-registrations
# https://hackersandslackers.com/flask-routes/


@bp.route('/')
def main_get():
    categories = db.session.query(Category).all()
    offers = db.session.query(Offer).order_by(Offer.created_at).limit(8).all()
    images = {}
    for o in offers:
        images[o.id] = json.loads(o.images)
    return render_template('main.jinja',
                           offers=offers,
                           categories=categories,
                           images=images)


@bp.route('/offer/<int:offer_id>')
def offer_get(offer_id):
    categories = db.session.query(Category).all()
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    print("dupa")
    print(offer.price)
    images = json.loads(offer.images)
    author = db.session.query(User).filter_by(id=offer.author).one_or_none()
    return render_template('offer/offer.jinja',
                           offer=offer,
                           categories=categories,
                           images=images,
                           author=author)


@bp.route('/offer/add', methods=["GET", "POST"])
@auth_required()
def offer_add():
    form = AddEditOfferForm()
    if request.method == 'POST':
        offer = Offer(author=current_user.id,
                      description=form.description.data,
                      category=1,
                      title=form.title.data,
                      price=form.price.data if form.price.data != 0 else None,
                      is_used=False,
                      images='["1200px-RedCat_8727.jpg", "cat.webp"]')
        db.session.add(offer)
        db.session.commit()
        return redirect(url_for('bp_main.user_offers_get'))
    else:
        return render_template('offer/offer_add_edit.jinja', form=form, offer_id=None)


@bp.route('/offer/<int:offer_id>/edit', methods=["GET", "POST"])
@auth_required()
def offer_edit(offer_id):
    form = AddEditOfferForm()
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    if offer.author != current_user.id:
        abort(401)

    if request.method == 'POST':
        offer.title = form.title.data
        offer.description = form.description.data
        offer.price = form.price.data
        db.session.commit()
        return redirect(url_for('bp_main.user_offers_get'))
    else:
        form.title.data = offer.title
        form.description.data = offer.description
        form.price.data = offer.price
        return render_template('offer/offer_add_edit.jinja', form=form, offer_id=offer_id)


@bp.route('/offer/<int:offer_id>/delete', methods=['POST'])
@auth_required()
def offer_delete(offer_id):
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    if offer.author != current_user.id:
        abort(401)
    db.session.delete(offer)
    db.session.commit()
    return redirect(url_for('bp_main.user_offers_get'))


@bp.route('/user/profile')
@auth_required()
def user_profile_get():
    user_data = {
        "Imię": current_user.first_name,
        "Nazwisko": current_user.last_name,
        "Wydział": current_user.faculty,
        "Akademik": current_user.dorm,
        "Email": current_user.email,
    }
    return render_template('user/user_profile.jinja', personal_data=user_data)


@bp.route('/user/offers')
@auth_required()
def user_offers_get():
    offers = db.session.query(Offer).filter_by(author=current_user.id).all()
    return render_template('user/user_offers.jinja', offers=offers)


@bp.route('/user/settings')
@auth_required()
def user_settings_get():
    return render_template('user/user_settings.jinja', 
                           change_email_form=ChangeEmailForm(), 
                           delete_account_confirm_form=DeleteAccountForm())

@bp.route('/user/settings/change_email', methods=['POST'])
@auth_required()
def change_email():
    change_email_form = ChangeEmailForm()
    if change_email_form.validate_on_submit():
        try:
            user_check = User.query.filter_by(email=change_email_form.email.data).one_or_none()
            if user_check is None:
                current_user.email = change_email_form.email.data
                current_user.email_change_new = change_email_form.email.data
                current_user.email_change_last = datetime.now()
                db.session.add(current_user)
                db.session.commit()
            else:
                change_email_form.email.errors.append('Ten email jest używany!')
        except IntegrityError:
            change_email_form.email.errors.append('Ten email jest używany!')
    return render_template('user/user_settings.jinja', 
                           change_email_form=change_email_form, 
                           delete_account_confirm_form=DeleteAccountForm())


@bp.route('/user/settings/delete', methods=['POST'])
@auth_required()
def delete_account():
    delete_account_form = DeleteAccountForm()
    if delete_account_form.validate_on_submit():
        try:
            if delete_account_form.email.data == current_user.email:
                db.session.delete(current_user)
                db.session.commit()
                return redirect(url_for('security.logout'))
            else:
                delete_account_form.email.errors.append('Nieprawidlowy email!')
        except IntegrityError:
            delete_account_form.email.errors.append('Nieprawidlowy email!')
    return render_template('user/user_settings.jinja', 
                           change_email_form=ChangeEmailForm(), 
                           delete_account_confirm_form=delete_account_form)
