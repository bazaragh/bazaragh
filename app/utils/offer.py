from app.app import OFFERS_IMAGES_DIR


def get_offer_images_src_paths(offer_id, images):
    return [f'{OFFERS_IMAGES_DIR}/{offer_id}/{image}' for image in images]


def get_image_name_from_href_path(href_path):
    return href_path.split("/")[-1]
