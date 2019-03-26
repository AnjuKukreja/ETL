from main.inputoutput.io import inc, unzip_file
import os


def diff(li1, li2):
    return list(set(li1) - set(li2))


def test_answer():
    assert inc(3) == 5


def test_unzip_file():
    from_path = os.path.join("..", "data", "TestFile.zip")
    to_path = os.path.join("..", "data", "target")
    unzip_file(from_path, to_path)
    extracted_files = os.listdir(to_path)
    file_list = set(file for file in os.listdir(os.path.join("..", "data"))
                      if os.path.isfile(os.path.join("..", "data", file)))
    file_list.discard("TestFile.zip")
    diff_files = file_list - set(extracted_files)
    assert diff_files.__len__() == 0

