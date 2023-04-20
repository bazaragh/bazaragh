from flask import Blueprint, render_template
from flask_login import current_user
from flask_security import auth_required, ChangePasswordForm

from app.app import db
from app.forms.security import DeleteAccountForm, ChangeEmailForm
from app.models import Offer

bp = Blueprint("bp_user", __name__, url_prefix='/user')


@bp.route('/profile')
@auth_required()
def profile_get():
    user_data = {
        "Imię": current_user.first_name,
        "Nazwisko": current_user.last_name,
        "Wydział": current_user.faculty,
        "Akademik": current_user.dorm,
        "Email": current_user.email,
    }
    return render_template('user/user_profile.jinja', personal_data=user_data)


@bp.route('/settings')
@auth_required()
def settings_get():
    return render_template('user/user_settings.jinja',
                           change_password_form=ChangePasswordForm(),
                           change_email_form=ChangeEmailForm(),
                           delete_account_confirm_form=DeleteAccountForm())


@bp.route('/offers')
@auth_required()
def offers_get():
    offers = db.session.query(Offer).filter_by(author=current_user.id).all()
    return render_template('user/user_offers.jinja', offers=offers)
