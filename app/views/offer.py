import json
import os
from datetime import datetime

from flask import Blueprint, redirect, url_for, render_template, abort, request
from flask_login import current_user
from flask_security import auth_required

from werkzeug.utils import secure_filename

from app.app import db, ABSOLUTE_IMAGES_UPLOAD_PATH
from app.forms.offer import AddEditOfferForm, DeleteOfferForm
from app.models import Offer, Category

bp = Blueprint("bp_offer", __name__, url_prefix='/user/offer')


@bp.route('/add', methods=["GET", "POST"])
@auth_required()
def add():
    print(request.files)
    try:
        form = AddEditOfferForm()
        form.category.choices = get_allowed_categories()
        if form.validate_on_submit():
            for file in form.images.data:
                print(file)
                file.filename = secure_filename(datetime.now().isoformat() + "_" + file.filename)
                print(file)
                print(type(file))
            offer = Offer(author=current_user.id,
                        description=form.description.data,
                        category=int(form.category.data),
                        title=form.title.data,
                        price=form.price.data if form.price.data is not None and form.price.data > 0 else None,
                        is_used=form.is_used.data,
                        images=json.dumps([f.filename for f in form.images.data]))#'["1200px-RedCat_8727.jpg", "cat.webp"]')
            db.session.add(offer)
            db.session.commit()
            for f in form.images.data:
                f.save(os.path.join(
                    ABSOLUTE_IMAGES_UPLOAD_PATH, f.filename
                ))
            return redirect(url_for('bp_user.offers_get'))
        return render_template('offer/offer_add_edit.jinja', form=form, offer_id=None)
    except Exception as e:
        print(e)


@bp.route('/edit/<int:offer_id>', methods=["GET", "POST"])
@auth_required()
def edit(offer_id):
    try:
        offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
        if offer is None:
            abort(404)
        if offer.author != current_user.id:
            abort(401)

        form = AddEditOfferForm(obj=offer)
        form.category.choices = get_allowed_categories()
        if form.validate_on_submit():
            form.populate_obj(offer)
            offer.images = json.dumps(form.images.data)
            db.session.commit()
            return redirect(url_for('bp_user.offers_get'))
        return render_template('offer/offer_add_edit.jinja', form=form, offer_id=offer_id)

    except Exception as e:
        print(e)

@bp.route('/delete/<int:offer_id>', methods=['GET', 'POST'])
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

def get_allowed_categories():
    categories = db.session.query(Category).all()
    return [(c.id, c.name) for c in categories]
