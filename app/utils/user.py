import os
from app.app import ABSOLUTE_PROFILE_IMAGES_PATH, ALLOWED_IMAGE_EXTENSIONS, DEFAULT_PROFILE_PICTURE_FILENAME, PROFILE_IMAGES_DIR
from app.utils.files import delete_file, save_file


def get_user_profile_picture_href_path(filename):
    return f'{PROFILE_IMAGES_DIR}/{filename}'

def get_users_profile_picture_dir_path():
    return ABSOLUTE_PROFILE_IMAGES_PATH

def save_user_profile_picture(image):
    offer_images_path = get_users_profile_picture_dir_path()
    save_file(offer_images_path, image)

def change_user_profile_picture_filename(user_id, file):
    file.filename = f"{user_id}.{file.filename.split('.')[-1]}"

def get_user_profile_picture_absolute_path(filename):
    return os.path.join(get_users_profile_picture_dir_path(), filename)

def delete_user_profile_picture(user_id):
    filename = get_user_profile_picture_filename_or_default(user_id)
    if filename != DEFAULT_PROFILE_PICTURE_FILENAME:
        delete_file(get_users_profile_picture_dir_path(), filename)

def get_user_profile_picture_filename_or_default(user_id):
    for ext in ALLOWED_IMAGE_EXTENSIONS:
        filename = f"{user_id}.{ext}"
        if os.path.exists(get_user_profile_picture_absolute_path(filename)):
            return filename
    return DEFAULT_PROFILE_PICTURE_FILENAME
