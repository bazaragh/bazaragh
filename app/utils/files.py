import os
from typing import List

from werkzeug.datastructures import FileStorage


def delete_file(directory_path, filename):
    file_path = os.path.join(directory_path, filename)
    if os.path.exists(file_path):
        os.remove(file_path)

def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)

def save_file(dir_path, file: FileStorage):
    file.save(os.path.join(dir_path, file.filename))

def save_files(dir_path, images: List[FileStorage]):
    for file in images:
        save_file(dir_path, file)

def get_file_name_from_href_path(href_path):
    return href_path.split("/")[-1]

