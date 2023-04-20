from datetime import datetime

from MySQLdb import IntegrityError
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from flask_security import auth_required

from app.app import db
from app.forms.security import ChangeEmailForm, DeleteAccountForm
from app.models import User

bp = Blueprint("bp_settings", __name__, url_prefix="/user/settings")


@bp.route('/change_email', methods=['POST'])
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
    return render_template('user/user_settings.jinja',
                           change_email_form=ChangeEmailForm(),
                           delete_account_confirm_form=delete_account_form)
