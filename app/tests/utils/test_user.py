import os
import io

from app.app import ABSOLUTE_PROFILE_IMAGES_PATH, ALLOWED_IMAGE_EXTENSIONS, DEFAULT_PROFILE_PICTURE_FILENAME, PROFILE_IMAGES_DIR
from app.utils.user import *
from werkzeug.datastructures import FileStorage


def test_get_user_profile_picture_href_path():
    filename = 'text.txt'
    expected = f'{PROFILE_IMAGES_DIR}/{filename}'
    
    result = get_user_profile_picture_href_path(filename)

    assert expected == result

def test_get_users_profile_picture_dir_path():
    assert ABSOLUTE_PROFILE_IMAGES_PATH == get_users_profile_picture_dir_path()

def test_save_user_profile_picture(mocker):
    mock = mocker.patch("app.utils.user.save_file")
    image = 'file1'

    save_user_profile_picture(image)

    expected_argument = ABSOLUTE_PROFILE_IMAGES_PATH
    mock.assert_called_once_with(expected_argument, image)

def test_change_user_profile_picture_filename():
    user_id = 1
    filename = 'test.txt'
    data = b'text'
    file = FileStorage(io.BytesIO(data), filename)

    change_user_profile_picture_filename(user_id, file)
    assert file.filename == '1.txt'

def test_get_user_profile_picture_absolute_path():
    filename = 'test.txt'
    expected = os.path.join(ABSOLUTE_PROFILE_IMAGES_PATH, filename)

    result =  get_user_profile_picture_absolute_path(filename)

    assert expected == result

def test_delete_user_profile_picture(mocker):
    mock_delete = mocker.patch("app.utils.user.delete_file")
    filename = '1.jpg'
    mock = mocker.patch("app.utils.user.get_user_profile_picture_filename_or_default")
    mock.return_value = filename
    user_id = 1

    delete_user_profile_picture(user_id)

    expected_argument = ABSOLUTE_PROFILE_IMAGES_PATH
    mock_delete.assert_called_once_with(expected_argument, filename)

def test_get_user_profile_picture_filename_or_default_returns_default(mocker):
    mock_path_exists = mocker.patch("os.path.exists", return_value=False)
    user_id = 1
    expected_filename = DEFAULT_PROFILE_PICTURE_FILENAME

    result_filename = get_user_profile_picture_filename_or_default(user_id)
    assert result_filename == expected_filename


def test_get_user_profile_picture_filename_or_default_return_profile_picture(mocker):
    mock_path_exists = mocker.patch("os.path.exists", return_value=True)
    user_id = 1
    expected_filename = f"{user_id}.{list(ALLOWED_IMAGE_EXTENSIONS)[0]}"

    result_filename = get_user_profile_picture_filename_or_default(user_id)
    assert result_filename == expected_filename