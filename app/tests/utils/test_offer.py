import io
import os
from datetime import datetime
from werkzeug.datastructures import FileStorage

from app.app import ABSOLUTE_OFFERS_IMAGES_PATH, OFFERS_IMAGES_DIR


def test_get_allowed_categories(app):
    # hack for database intialization so import Category doesn't break
    from app.utils.offer import get_allowed_categories
    expected = [(1, 'Moda'), 
                (2, 'Elektronika'), 
                (3, 'Edukacja'), 
                (4, 'Zdrowie i uroda'), 
                (5, 'Sport'), 
                (6, 'Jedzenie'), 
                (7, 'Wnętrze'), 
                (8, 'Muzyka i hobby')]

    with app.app_context():
        assert get_allowed_categories() == expected

def test_get_offer_images_href_paths():
    from app.utils.offer import get_offer_images_href_paths
    offer_id = 1
    images = ['image1.jpg', 'image2.jpg']
    expected = [f'{OFFERS_IMAGES_DIR}/1/image1.jpg', f'{OFFERS_IMAGES_DIR}/1/image2.jpg']
    
    result = get_offer_images_href_paths(offer_id, images)

    assert expected == result

def test_get_offer_images_dir_path():
    from app.utils.offer import get_offer_images_dir_path
    offer_id = 1
    expected = os.path.join(ABSOLUTE_OFFERS_IMAGES_PATH, str(offer_id))

    result = get_offer_images_dir_path(offer_id)

    assert expected == result

def test_create_offer_images_dir(mocker):
    from app.utils.offer import create_offer_images_dir
    mock = mocker.patch("app.utils.offer.create_directory")
    offer_id = 1

    create_offer_images_dir(offer_id)

    expect_argument = os.path.join(ABSOLUTE_OFFERS_IMAGES_PATH, str(offer_id))
    mock.assert_called_once_with(expect_argument)


def test_save_offer_images(mocker):
    from app.utils.offer import save_offer_images
    mock = mocker.patch("app.utils.offer.save_files")
    offer_id = 1
    images = ['file1', 'file2']

    save_offer_images(offer_id, images)

    expected_argument = os.path.join(ABSOLUTE_OFFERS_IMAGES_PATH, str(offer_id))
    mock.assert_called_once_with(expected_argument, images)


def test_delete_offers_images(mocker):
    from app.utils.offer import delete_offers_images
    mock = mocker.patch("app.utils.offer.delete_file")
    offer_id = 1
    images = ['file1', 'file2']

    delete_offers_images(offer_id, images)

    expected_argument = os.path.join(ABSOLUTE_OFFERS_IMAGES_PATH, str(offer_id))
    for filename in images:
        mock.assert_any_call(expected_argument, filename)

def test_change_offer_images_filenames(mocker):    
    from app.utils.offer import change_offer_images_filenames
    filenames = ['test1.txt', 'test2.txt', 'test3.txt']
    datas = [b'text1', b'text2', b'text3']
    files = [FileStorage(io.BytesIO(data), filename) for filename, data in zip(filenames, datas)]
    
    mocker.patch("app.utils.offer.secure_filename", return_value='changed')

    change_offer_images_filenames(files)
    for file in files:
        file.filename == 'changed'
