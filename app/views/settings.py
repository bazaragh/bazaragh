from datetime import datetime

from MySQLdb import IntegrityError
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from flask_security import auth_required

from app.app import ALLOWED_IMAGE_EXTENSIONS, db
from app.forms.security import ChangeEmailForm, DeleteAccountForm
from app.forms.user import AddUserProfilePicture
from app.models import User
from app.utils.user import change_user_profile_picture_filename, delete_user_profile_picture, save_user_profile_picture

bp = Blueprint("bp_settings", __name__, url_prefix="/user/settings")


@bp.route('/change_email', methods=['POST'])
@auth_required()
def change_email():
    change_email_form = ChangeEmailForm()
    if change_email_form.validate_on_submit():
        try:
            user_check = User.query.filter_by(
                email=change_email_form.email.data).one_or_none()
            if user_check is None:
                current_user.email = change_email_form.email.data
                current_user.email_change_new = change_email_form.email.data
                current_user.email_change_last = datetime.now()
                db.session.add(current_user)
                db.session.commit()
            else:
                change_email_form.email.errors.append(
                    'Ten email jest używany!')
        except IntegrityError:
            change_email_form.email.errors.append('Ten email jest używany!')
    return redirect(url_for('bp_user.settings_get'))


@bp.route('/delete', methods=['POST'])
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
    return redirect(url_for('bp_user.settings_get'))


@bp.route('/profilePicture', methods=['POST'])
@auth_required()
def set_profile_picture():
    add_user_profile_picture = AddUserProfilePicture()
    if add_user_profile_picture.validate_on_submit():
        file = add_user_profile_picture.image.data
        change_user_profile_picture_filename(current_user.id, file)
        delete_user_profile_picture(current_user.id)
        save_user_profile_picture(file)
    elif not add_user_profile_picture.validate() and add_user_profile_picture.is_submitted():
        add_user_profile_picture.image.errors.append(
            f'Nieprawidłowe rozszerzenie pliku, akceptowane są tylko pliki z rozszerzeniami {ALLOWED_IMAGE_EXTENSIONS}')
        return redirect(url_for('bp_user.settings_get'))

    return redirect(url_for('bp_user.profile_get'))
