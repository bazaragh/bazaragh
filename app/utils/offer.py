from datetime import datetime
import os

from werkzeug.utils import secure_filename

from app.app import db, ABSOLUTE_OFFERS_IMAGES_PATH, OFFERS_IMAGES_DIR
from app.models import Category
from app.utils.files import create_directory, delete_file, save_files

def get_allowed_categories():
    categories = db.session.query(Category).all()
    return [(c.id, c.name) for c in categories]

def get_offer_images_href_paths(offer_id, images):
    return [f'{OFFERS_IMAGES_DIR}/{offer_id}/{image}' for image in images]

def get_offer_images_dir_path(id):
    return os.path.join(ABSOLUTE_OFFERS_IMAGES_PATH, str(id))

def create_offer_images_dir(id):
    dir_path = get_offer_images_dir_path(id)
    create_directory(dir_path)

def save_offer_images(id, images):
    offer_images_path = get_offer_images_dir_path(id)
    save_files(offer_images_path, images)

def delete_offers_images(id, images):
    offer_images_path = get_offer_images_dir_path(id)
    for filename in images:
        delete_file(offer_images_path, filename)

def change_offer_images_filenames(images):    
    timestamp = int(round(datetime.now().timestamp()))
    for file in images:
        file.filename = secure_filename(str(timestamp) + "_" + file.filename)
