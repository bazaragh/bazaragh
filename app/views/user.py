from flask import Blueprint, render_template
from flask_login import current_user
from flask_security import auth_required, ChangePasswordForm

from app.app import db
from app.forms.security import DeleteAccountForm, ChangeEmailForm
from app.forms.user import AddUserProfilePicture
from app.models import Offer
from app.utils.user import get_user_profile_picture_filename_or_default, get_user_profile_picture_href_path

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
    profile_picture_filename = get_user_profile_picture_filename_or_default(current_user.id)
    profile_picture = get_user_profile_picture_href_path(profile_picture_filename)
    return render_template('user/user_profile.jinja', personal_data=user_data, profile_picture=profile_picture)


@bp.route('/settings')
@auth_required()
def settings_get():
    return render_template('user/user_settings.jinja',
                           change_password_form=ChangePasswordForm(),
                           change_email_form=ChangeEmailForm(),
                           delete_account_confirm_form=DeleteAccountForm(),
                           add_user_profile_picture=AddUserProfilePicture())


@bp.route('/offers')
@auth_required()
def offers_get():
    offers = db.session.query(Offer).filter_by(author=current_user.id).all()
    return render_template('user/user_offers.jinja', offers=offers)


@bp.route('/opinion')
@auth_required()
def opinion_get():
    return render_template('user/user_opinion.jinja')


@bp.route('/favourites')
@auth_required()
def favs_get():
    return render_template('user/user_favs.jinja')