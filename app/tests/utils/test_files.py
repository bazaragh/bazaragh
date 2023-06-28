import os
import io
from app.utils.files import *
from werkzeug.datastructures import FileStorage


def test_delete_file(tmpdir):
    tmpdir = str(tmpdir)
    filename = 'test.txt'
    filepath = os.path.join(tmpdir, filename)

    try:
        delete_file(tmpdir, filename)
        with open(filepath, 'w') as f:
            f.write('Text')
        assert os.path.exists(filepath)

        delete_file(tmpdir, filename)
        assert not os.path.exists(filepath)
    except OSError:
        assert False


def test_create_directory(tmpdir):
    tmpdir = str(tmpdir)
    filename = 'test.txt'
    filepath = os.path.join(tmpdir, filename)
    with open(filepath, 'w') as f:
        f.write('Text')

    create_directory(tmpdir)
    assert os.path.exists(filepath)

    dirpath = os.path.join(tmpdir, 'test_dir')
    assert not os.path.exists(dirpath)
    create_directory(dirpath)
    assert os.path.exists(dirpath)


def test_save_file(tmpdir):
    tmpdir = str(tmpdir)
    filename = 'test.txt'
    filepath = os.path.join(tmpdir, filename)
    data = b'text'
    file = FileStorage(io.BytesIO(data), filename)

    save_file(tmpdir, file)

    assert os.path.exists(filepath)
    with open(filepath, 'rb') as f:
        assert f.read() == data


def test_save_files(tmpdir):
    tmpdir = str(tmpdir)
    filenames = ['test1.txt', 'test2.txt', 'test3.txt']
    filepaths = [os.path.join(tmpdir, filename) for filename in filenames]
    datas = [b'text1', b'text2', b'text3']
    files = [FileStorage(io.BytesIO(data), filename)
             for filename, data in zip(filenames, datas)]

    save_files(tmpdir, files)

    for filepath, data in zip(filepaths, datas):
        assert os.path.exists(filepath)
        with open(filepath, 'rb') as f:
            assert f.read() == data


def test_get_file_name_from_href_path():
    href = 'static/templates/image.jpg'
    expected = 'image.jpg'
    result = get_file_name_from_href_path(href)
    assert expected == result
