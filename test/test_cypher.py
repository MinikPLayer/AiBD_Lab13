import random

from cypher import caesar_encrypt
from cypher import caesar_decrypt
from cypher import letters
import pytest

test_data = [
    ("", "", 13),
    ("ABCD", "NOPQ", 13),
    ("abcd", "nopq", 13),
    ("Dzisiaj jest ladna pogoda", "QMvFvnwmwrFGmynqAnmCBtBqn", 13),
    ("xyz", "ABC", 3),
    ("XYZ", "123", 4),
    ("789", "abc", 4),
    ("9", " ", 1),
]


@pytest.mark.parametrize('data', test_data)
def test_encryption(data):
    text = data[0]
    expected = data[1]
    move_count = data[2]
    ret = caesar_encrypt(text, move_count)

    assert ret == expected


@pytest.mark.parametrize('data', test_data)
def test_decryption(data):
    expected = data[0]
    text = data[1]
    move_count = data[2]
    ret = caesar_decrypt(text, move_count)

    assert ret == expected


def test_invalid_encrypt():
    inv = 5
    ret = caesar_encrypt(inv, 1)
    assert ret is None


def test_invalid_decrypt():
    inv = 5
    ret = caesar_decrypt(inv, 1)
    assert ret is None


def test_random_encryption_decryption():
    ret = ""
    for i in range(0, 32768):
        ret += letters[random.randint(0, len(letters) - 1)]

    encrypted = caesar_encrypt(ret, 13)
    decrypted = caesar_decrypt(encrypted, 13)

    assert ret == decrypted
