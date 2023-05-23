import json
import os

from flask import Blueprint, redirect, url_for, render_template, abort, request
from flask_login import current_user
from flask_security import auth_required

from app.app import db
from app.forms.offer import AddEditOfferForm, DeleteOfferForm
from app.models import Offer
from app.utils.files import get_file_name_from_href_path
from app.utils.offer import *

bp = Blueprint("bp_offer", __name__, url_prefix='/user/offer')


@bp.route('/add', methods=["GET", "POST"])
@auth_required()
def add():
    form = AddEditOfferForm()
    form.category.choices = get_allowed_categories()

    if form.validate_on_submit():
        change_offer_images_filenames(form.images.data)

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

        create_offer_images_dir(offer.id)
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
    images_paths = get_offer_images_href_paths(offer.id, images)
    existing_images = [{'should_delete': False, 'image_href_path': image_path}
                       for image_path in images_paths]
    form = AddEditOfferForm(obj=offer, existing_images=existing_images)
    form.category.choices = get_allowed_categories()
    if request.method == 'GET':
        form.images.data = []

    if form.validate_on_submit():
        added_files = form.images.data
        files_to_stay = [get_file_name_from_href_path(delete_image_form.image_href_path.data)
                         for delete_image_form in form.existing_images if not delete_image_form.should_delete.data]
        files_to_delete = [get_file_name_from_href_path(delete_image_form.image_href_path.data)
                           for delete_image_form in form.existing_images if delete_image_form.should_delete.data]
        form.existing_images.entries = []  # clear FieldList so form.populate_obj works

        change_offer_images_filenames(added_files)
        form.populate_obj(offer)

        offer.images = json.dumps(
            files_to_stay + [f.filename for f in added_files])
        db.session.commit()
        create_offer_images_dir(offer.id)
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

        offer_images_dir_path = get_offer_images_dir_path(offer.id)

        if os.path.exists(offer_images_dir_path):
            delete_offers_images(offer.id, images)
            os.rmdir(offer_images_dir_path)
        return redirect(url_for('bp_user.offers_get'))

    return render_template('offer/offer_delete.jinja', form=form, offer=offer)
