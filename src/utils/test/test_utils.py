import pytest
from utils.file import read_file


def test_read_file():
    assert read_file("utils/test/foo.txt") == "bar"

