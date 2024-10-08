import pytest
from Caesar_Cipher import encrypt, unencrypt

def test_basic_message():
    result = encrypt("hello", 5)
    assert result == "mjqqt"

def test_with_overflow():
    result = encrypt("hello", 13)
    assert result == "uryyb"

def test_full_loop():
    result = encrypt("hello", 26)
    assert result == "hello"

def test_with_space():
    result = encrypt("good morning", 7)
    assert result == "nvvk tvyupun"

def test_full_alphabet():
    result = encrypt("abcdefghijklmnopqrstuvwxyz", 1)
    assert result == "bcdefghijklmnopqrstuvwxyza"

def test_basic_message_reverse():
    result = unencrypt("mjqqt", 5)
    assert result == "hello"

def test_with_overflow_reverse():
    result = unencrypt("uryyb", 13)
    assert result == "hello"

def test_full_loop_reverse():
    result = unencrypt("hello", 26)
    assert result == "hello"

def test_with_space_reverse():
    result = unencrypt("nvvk tvyupun", 7)
    assert result == "good morning"

def test_full_alphabet_reverse():
    result = unencrypt("bcdefghijklmnopqrstuvwxyza", 1)
    assert result == "abcdefghijklmnopqrstuvwxyz"