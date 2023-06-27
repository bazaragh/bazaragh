import io

from flask import url_for
from app.app import db


def test_change_email_email_taken(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        new_email = "test1@bazaragh.pl"
        response = client.post('/user/settings/change_email',
                               data={"email": new_email}, follow_redirects=True)

        from app.models import User
        user = db.session.query(User).filter_by(id=1).one_or_none()
        assert user.email == "admin@bazaragh.pl"


def test_change_email(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        new_email = "admin2@bazaragh.pl"
        response = client.post('/user/settings/change_email',
                               data={"email": new_email}, follow_redirects=True)

        from app.models import User
        user = db.session.query(User).filter_by(id=1).one_or_none()
        assert user.email == new_email


def test_delete_account(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        email = "admin@bazaragh.pl"
        response = client.post('/user/settings/delete',
                               data={"email": email}, follow_redirects=True)

        from app.models import User
        user = db.session.query(User).filter_by(id=1).one_or_none()
        assert user is None


def test_delete_account_bad_email(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        email = "admin123@bazaragh.pl"
        response = client.post('/user/settings/delete',
                               data={"email": email}, follow_redirects=True)

        from app.models import User
        user = db.session.query(User).filter_by(id=1).one_or_none()
        assert user is not None


def test_set_profile_picture(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_change_user_profile_picture_filename = mocker.patch(
            "app.views.settings.change_user_profile_picture_filename")
        mock_delete_user_profile_picture = mocker.patch(
            "app.views.settings.delete_user_profile_picture")
        mock_save_user_profile_picture = mocker.patch(
            "app.views.settings.save_user_profile_picture")

        filename = 'test.jpg'
        file = (io.BytesIO(b'text'), filename)
        data = {'image': file}
        response = client.post('/user/settings/profilePicture', data=data, follow_redirects=True,
                               content_type='multipart/form-data')

        assert response.request.path == url_for('bp_user.profile_get')

        mock_change_user_profile_picture_filename.assert_called_once()
        mock_delete_user_profile_picture.assert_called_once()
        mock_save_user_profile_picture.assert_called_once()


def test_set_profile_picture_bad_extension(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_change_user_profile_picture_filename = mocker.patch(
            "app.views.settings.change_user_profile_picture_filename")
        mock_delete_user_profile_picture = mocker.patch(
            "app.views.settings.delete_user_profile_picture")
        mock_save_user_profile_picture = mocker.patch(
            "app.views.settings.save_user_profile_picture")

        filename = 'test.txt'
        file = (io.BytesIO(b'text'), filename)
        data = {'image': file}
        response = client.post('/user/settings/profilePicture', data=data, follow_redirects=True,
                               content_type='multipart/form-data')

        assert response.request.path == url_for('bp_user.settings_get')

        assert mock_change_user_profile_picture_filename.call_count == 0
        assert mock_delete_user_profile_picture.call_count == 0
        assert mock_save_user_profile_picture.call_count == 0
