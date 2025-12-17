import pytest
from main import is_valid_email

# Эерэг тестүүд
def test_valid_email():
    assert is_valid_email("user@example.com") == True

def test_valid_email_without_test_com():
    assert is_valid_email("valid_user@example.com") == True

# Сөрөг тестүүд
def test_email_without_at_symbol():
    assert is_valid_email("invalidemail.com") == False

def test_email_with_test_com():
    assert is_valid_email("user@test.com") == False

def test_email_with_trailing_spaces():
    assert is_valid_email("user@example.com ") == True

# Edge-case тестүүд
def test_empty_email():
    assert is_valid_email("") == False

def test_only_at_symbol():
    assert is_valid_email("@") == False

def test_email_with_multiple_at_symbols():
    assert is_valid_email("user@@example.com") == True

def test_email_with_special_characters():
    assert is_valid_email("user+test@example.com") == True
