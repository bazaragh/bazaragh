from flask import Blueprint, redirect, url_for, render_template, abort
from flask_login import current_user
from flask_security import auth_required

from app.app import db
from app.forms.offer import AddEditOfferForm, DeleteOfferForm
from app.models import Offer

bp = Blueprint("bp_offer", __name__, url_prefix='/user/offer')


@bp.route('/offer/add', methods=["GET", "POST"])
@auth_required()
def add():
    form = AddEditOfferForm()
    if form.validate_on_submit():
        offer = Offer(author=current_user.id,
                      description=form.description.data,
                      category=1,
                      title=form.title.data,
                      price=form.price.data if form.price.data != 0 else None,
                      is_used=False,
                      images='["1200px-RedCat_8727.jpg", "cat.webp"]')
        db.session.add(offer)
        db.session.commit()
        return redirect(url_for('bp_user.offers_get'))
    return render_template('offer/offer_add_edit.jinja', form=form, offer_id=None)


@bp.route('/offer/edit/<int:offer_id>', methods=["GET", "POST"])
@auth_required()
def edit(offer_id):
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()

    if offer is None:
        abort(404)
    if offer.author != current_user.id:
        abort(401)

    form = AddEditOfferForm(obj=offer)

    if form.validate_on_submit():
        form.populate_obj(offer)
        db.session.commit()
        return redirect(url_for('bp_user.offers_get'))
    return render_template('offer/offer_add_edit.jinja', form=form, offer_id=offer_id)


@bp.route('/offer/delete/<int:offer_id>', methods=['GET', 'POST'])
@auth_required()
def delete(offer_id):
    form = DeleteOfferForm()
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    if offer.author != current_user.id:
        abort(401)

    if form.validate_on_submit():
        db.session.delete(offer)
        db.session.commit()
        return redirect(url_for('bp_user.offers_get'))
    return render_template('offer/offer_delete.jinja', form=form, offer=offer)
