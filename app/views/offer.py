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
from app.views.utils import get_offer_images_src_paths, get_image_name_from_href_path

bp = Blueprint("bp_offer", __name__, url_prefix='/user/offer')


@bp.route('/add', methods=["GET", "POST"])
@auth_required()
def add():
    form = AddEditOfferForm()
    form.category.choices = get_allowed_categories()

    if form.validate_on_submit():
        change_images_filenames(form.images.data)

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

        os.mkdir(get_offer_images_dir_path(offer.id))
        save_offer_images(offer.id, form.images.data)
        return redirect(url_for('bp_user.offers_get'))
    return render_template('offer/offer_add_edit.jinja', form=form, offer_id=None)


@bp.route('/edit/<int:offer_id>', methods=["GET", "POST"])
@auth_required()
def edit(offer_id):
    offer = db.session.query(Offer).filter_by(id=offer_id).one_or_none()
    if offer is None:
        abort(404)
    if offer.author != current_user.id:
        abort(401)

    images = json.loads(offer.images)
    images_paths = get_offer_images_src_paths(offer.id, images)
    existing_images = [{'should_delete': False, 'image_href_path': image_path} for image_path in images_paths]
    form = AddEditOfferForm(obj=offer, existing_images=existing_images)
    form.category.choices = get_allowed_categories()
    if request.method == 'GET':
        form.images.data = []

    if form.validate_on_submit():
        added_files = form.images.data
        files_to_stay = [get_image_name_from_href_path(delete_image_form.image_href_path.data) for delete_image_form in form.existing_images if not delete_image_form.should_delete.data]
        files_to_delete = [get_image_name_from_href_path(delete_image_form.image_href_path.data) for delete_image_form in form.existing_images if delete_image_form.should_delete.data]
        form.existing_images.entries = [] # clear FieldList so form.populate_obj works

        change_images_filenames(added_files)
        form.populate_obj(offer)

        offer.images = json.dumps(files_to_stay + [f.filename for f in added_files])
        db.session.commit()
        save_offer_images(offer.id, added_files)
        delete_offers_images(offer.id, files_to_delete)
        return redirect(url_for('bp_user.offers_get'))
    return render_template('offer/offer_add_edit.jinja', form=form, offer_id=offer_id)


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

        images = json.loads(offer.images)
        delete_offers_images(offer.id, images)
        os.rmdir(get_offer_images_dir_path(offer.id))
        return redirect(url_for('bp_user.offers_get'))
    
    return render_template('offer/offer_delete.jinja', form=form, offer=offer)


def get_allowed_categories():
    categories = db.session.query(Category).all()
    return [(c.id, c.name) for c in categories]

def get_offer_images_dir_path(id):
    return os.path.join(ABSOLUTE_OFFERS_IMAGES_PATH, str(id))

def save_offer_images(id, images):
    offer_images_path = get_offer_images_dir_path(id)
    for file in images:
        file.save(os.path.join(offer_images_path, file.filename))

def delete_offers_images(id, images):
    offer_images_path = get_offer_images_dir_path(id)
    for filename in images:
        delete_file(offer_images_path, filename)

def delete_file(directory_path, filename):
    file_path = os.path.join(directory_path, filename)
    if os.path.exists(file_path):
        os.remove(file_path)

def change_images_filenames(images):    
    timestamp = int(round(datetime.now().timestamp()))
    for file in images:
        file.filename = secure_filename(str(timestamp) + "_" + file.filename)