from zipfile import ZipFile


def inc(num):
    return num+2


def unzip_file(from_path, to_path):
    """This method unzips a file present on from_path path to to_path."""
    file_count = 0
    with ZipFile(from_path, 'r') as file:
        file.extractall(to_path)
        file.close()
