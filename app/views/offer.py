import json
import os
from datetime import datetime

from flask import Blueprint, redirect, url_for, render_template, abort, request
from flask_login import current_user
from flask_security import auth_required

from werkzeug.utils import secure_filename

from app.app import db, ABSOLUTE_OFFERS_IMAGES_PATH
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
            timestamp = int(round(datetime.now().timestamp()))
            for file in form.images.data:
                file.filename = secure_filename(str(timestamp) + "_" + file.filename)

            offer = Offer(author=current_user.id,
                        description=form.description.data,
                        category=int(form.category.data),
                        title=form.title.data,
                        price=form.price.data if form.price.data is not None and form.price.data > 0 else None,
                        is_used=form.is_used.data,
                        images=json.dumps([f.filename for f in form.images.data]))
            db.session.add(offer)
            db.session.flush()
            db.session.refresh(offer)
            db.session.commit()

            offer_images_path = get_offer_images_dir_path(offer.id)
            os.mkdir(offer_images_path)
            for file in form.images.data:
                file.save(os.path.join(offer_images_path, file.filename))

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
    try:
        form = DeleteOfferForm()
        offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
        if offer is None:
            abort(404)
        if offer.author != current_user.id:
            abort(401)

        if form.validate_on_submit():
            db.session.delete(offer)
            db.session.commit()

            images = json.loads(offer.images)
            delete_offers_images(offer.id, images)
            return redirect(url_for('bp_user.offers_get'))
        
        return render_template('offer/offer_delete.jinja', form=form, offer=offer)
    except Exception as e:
        print(e)

def get_allowed_categories():
    categories = db.session.query(Category).all()
    return [(c.id, c.name) for c in categories]

def delete_offers_images(id, images):
    offer_images_path = get_offer_images_dir_path(id)
    for filename in images:
        delete_file(offer_images_path, filename)
    os.rmdir(offer_images_path)

def get_offer_images_dir_path(id):
    return os.path.join(ABSOLUTE_OFFERS_IMAGES_PATH, str(id))

def delete_file(directory_path, filename):
    file_path = os.path.join(directory_path, filename)
    if os.path.exists(file_path):
        os.remove(file_path)