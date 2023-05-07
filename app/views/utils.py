import os
import json

IMAGE_DIR_HREF_PATH = 'uploads/'

def get_offer_images_src_paths(images):
    return [IMAGE_DIR_HREF_PATH + image for image in images]
