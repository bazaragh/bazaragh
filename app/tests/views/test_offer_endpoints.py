
import json
from flask_login import current_user
from flask import request, session, url_for
from sqlalchemy import text
from app.app import db


def test_offer_add(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_change_offer_images_filenames = mocker.patch(
            "app.views.offer.change_offer_images_filenames")
        mock_create_offer_images_dir = mocker.patch(
            "app.views.offer.create_offer_images_dir")
        mock_save_offer_images = mocker.patch(
            "app.views.offer.save_offer_images")

        offer = dict(author=1,
                     description='test_description',
                     category=1,
                     title='test_title',
                     price=1,
                     is_used=True,
                     images=[])
        response = client.post(
            "/user/offer/add", data=offer, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == url_for('bp_user.offers_get')

        mock_change_offer_images_filenames.assert_called_once()
        mock_create_offer_images_dir.assert_called_once()
        mock_save_offer_images.assert_called_once()

        from app.models import Offer
        saved_offer = db.session.query(Offer).order_by(Offer.id.desc()).first()
        saved_offer.images = json.loads(saved_offer.images)
        for key, value in offer.items():
            assert key in saved_offer.__dict__
            assert value == saved_offer.__dict__[key]


def test_offer_edit_unauthorized(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        response = client.get('/user/offer/edit/89')
        assert response.status_code == 401


def test_offer_edit_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        response = client.get('/user/offer/edit/1111111111')
        assert response.status_code == 404


def test_offer_edit(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_change_offer_images_filenames = mocker.patch(
            "app.views.offer.change_offer_images_filenames")
        mock_create_offer_images_dir = mocker.patch(
            "app.views.offer.create_offer_images_dir")
        mock_save_offer_images = mocker.patch(
            "app.views.offer.save_offer_images")
        mock_delete_offers_images = mocker.patch(
            "app.views.offer.delete_offers_images")

        offer = dict(description='test_description',
                     category=1,
                     title='test_title',
                     price=1,
                     is_used=True,
                     images=[])
        response = client.post(
            "/user/offer/add", data=offer, follow_redirects=True)

        from app.models import Offer
        saved_offer = db.session.query(Offer).order_by(Offer.id.desc()).first()

        offer_id = saved_offer.id
        offer['description'] = 'test_description_changed'
        offer['existing_images'] = []

        response = client.post(
            f"/user/offer/edit/{offer_id}", data=offer, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == url_for('bp_user.offers_get')

        assert mock_change_offer_images_filenames.call_count == 2
        assert mock_create_offer_images_dir.call_count == 2
        assert mock_save_offer_images.call_count == 2
        assert mock_delete_offers_images.call_count == 1

        edited_offer = db.session.query(
            Offer).order_by(Offer.id.desc()).first()
        edited_offer.images = json.loads(edited_offer.images)

        offer.pop('existing_images')
        for key, value in offer.items():
            assert key in edited_offer.__dict__
            assert value == edited_offer.__dict__[key]


def test_offer_delete_unauthorized(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        response = client.get('/user/offer/delete/89')
        assert response.status_code == 401


def test_offer_delete_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        response = client.get('/user/offer/delete/1111111111')
        assert response.status_code == 404


def test_offer_delete(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_change_offer_images_filenames = mocker.patch(
            "app.views.offer.change_offer_images_filenames")
        mock_create_offer_images_dir = mocker.patch(
            "app.views.offer.create_offer_images_dir")
        mock_save_offer_images = mocker.patch(
            "app.views.offer.save_offer_images")

        offer = dict(author=1,
                     description='test_description',
                     category=1,
                     title='test_title',
                     price=1,
                     is_used=True,
                     images=[])
        response = client.post(
            "/user/offer/add", data=offer, follow_redirects=True)

        mock_os_path_exists = mocker.patch("os.path.exists", return_value=True)
        mock_delete_offers_images = mocker.patch(
            "app.views.offer.delete_offers_images")
        mock_os_rmdir = mocker.patch("os.rmdir")

        from app.models import Offer
        saved_offer = db.session.query(Offer).order_by(Offer.id.desc()).first()
        offer_id = saved_offer.id

        response = client.post(
            f"/user/offer/delete/{offer_id}", follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == url_for('bp_user.offers_get')

        deleted_offer = db.session.query(
            Offer).filter_by(id=offer_id).one_or_none()
        assert deleted_offer is None

        mock_os_path_exists.assert_called_once()
        mock_delete_offers_images.assert_called_once()
        mock_os_rmdir.assert_called_once()


def test_offer_add_favourite_is_author(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        mock_change_offer_images_filenames = mocker.patch(
            "app.views.offer.change_offer_images_filenames")
        mock_create_offer_images_dir = mocker.patch(
            "app.views.offer.create_offer_images_dir")
        mock_save_offer_images = mocker.patch(
            "app.views.offer.save_offer_images")

        offer = dict(author=1,
                     description='test_description',
                     category=1,
                     title='test_title',
                     price=1,
                     is_used=True,
                     images=[])
        response = client.post(
            "/user/offer/add", data=offer, follow_redirects=True)

        from app.models import Offer, Favourite
        saved_offer = db.session.query(Offer).order_by(Offer.id.desc()).first()
        offer_id = saved_offer.id

        response = client.post(
            f"/user/offer/add-favourite/{offer_id}", follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == url_for(
            'bp_main.offer_get', offer_id=offer_id)

        favourite = db.session.query(Favourite).filter_by(
            offer=offer_id, user=1).one_or_none()
        assert favourite is None


def test_offer_add_favourite_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        response = client.get('/user/offer/add-favourite/1111111111')
        assert response.status_code == 404


def test_offer_add_favourite(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        from app.models import Favourite
        offer_id = 84

        response = client.post(
            f"/user/offer/add-favourite/{offer_id}", follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == url_for(
            'bp_main.offer_get', offer_id=offer_id)

        favourite = db.session.query(Favourite).filter_by(
            offer=offer_id, user=1).one_or_none()
        assert favourite is not None

def test_offer_delete_favourite_not_found(client):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        response = client.get('/user/offer/delete-favourite/1111111111')
        assert response.status_code == 404


def test_offer_delete_favourite(client, mocker):
    with client.session_transaction() as session:
        response = client.post(
            "login", data={"email": "admin@bazaragh.pl", "password": "test"})
    with client:
        from app.models import Favourite
        offer_id = 84

        response = client.post(
            f"/user/offer/add-favourite/{offer_id}", follow_redirects=True)
        favourite = db.session.query(Favourite).filter_by(
            offer=offer_id, user=1).one_or_none()
        assert favourite is not None

        response = client.post(f'/user/offer/delete-favourite/{offer_id}')

        favourite = db.session.query(Favourite).filter_by(
            offer=offer_id, user=1).one_or_none()
        assert favourite is None

        response = client.post(f'/user/offer/delete-favourite/{offer_id}')
        favourite = db.session.query(Favourite).filter_by(
            offer=offer_id, user=1).one_or_none()
        assert favourite is None
