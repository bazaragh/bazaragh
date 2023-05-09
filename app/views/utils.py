from app.app import OFFERS_IMAGES_DIR

def get_offer_images_src_paths(offer_id, images):
    return [f'{OFFERS_IMAGES_DIR}/{offer_id}/{image}' for image in images]
