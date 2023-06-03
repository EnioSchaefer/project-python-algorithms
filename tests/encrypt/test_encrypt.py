from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(message="abcabc", key="abc")

    with pytest.raises(TypeError):
        encrypt_message(message=123123, key=123)

    assert encrypt_message(message="random", key=999) == "modnar"

    assert encrypt_message(message="random", key=3) == "nar_mod"

    assert encrypt_message(message="random", key=2) == "modn_ar"
