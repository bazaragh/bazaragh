from flask import Blueprint, render_template, current_app, flash, redirect, url_for
from flask_login import current_user
from flask_mailman import EmailMessage
from flask_security import auth_required, ChangePasswordForm

from app.app import db
from app.forms.opinion import OpinionForm
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


@bp.route('/opinion', methods=["GET", "POST"])
@auth_required()
def opinion_get():
    form = OpinionForm()
    logged_in = 'gość'

    if current_user.is_authenticated:
        form.email.data = current_user.email
        form.email.render_kw['readonly'] = True
        logged_in = 'użytkownik zalogowany'
    else:
        form.email.render_kw['readonly'] = False

    if form.validate_on_submit():
        content = f"Wiadomość od {form.email.data} ({logged_in})\n" \
                  f"Treść zgłoszenia:\n" \
                  f"{form.contents.data}"
        message = EmailMessage(subject="Wiadomość z formularza kontaktowego",
                               body=content,
                               from_email=current_app.config['MAIL_DEFAULT_SENDER'],
                               to=[current_app.config['MAIL_USERNAME']],
                               reply_to=[form.email.data])
        message.send()
        flash("Wiadomość została wysłana", "success")

        return redirect(url_for('bp_user.opinion_get'))

    return render_template('user/user_opinion.jinja', form=form)


@bp.route('/favourites')
@auth_required()
def favs_get():
    return render_template('user/user_favs.jinja')
