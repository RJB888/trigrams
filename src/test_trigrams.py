"""Test that the trigrams algorithm produces proper output."""
import pytest
from trigrams import convert_book_to_list_of_words

def get_book():
    with open('sherlock.txt', 'r') as book:
        book = book.read()
    return book


book = get_book()
book_word_list = convert_book_to_list_of_words(get_book())


def test_read_book_from_file():
    """Test that book is converted to and returned as a string"""
    from trigrams import read_book_from_file
    assert type(read_book_from_file()) == str


# @pytest.mark.parametrize('book, result', BOOKS_TABLE)
def test_words_are_only_alpha():
    """Test all non-alpha characters have been removed from text"""
    from trigrams import convert_book_to_list_of_words
    assert  ''.join(convert_book_to_list_of_words(book)).isalpha()


def test_create_trigram_dict_returns_a_dict():
    """Test that a dict object is actually returned"""
    from trigrams import create_trigram_dict
    assert type(create_trigram_dict(book_word_list)) == dict


def test_create_trigram_dict_len_greater_than_one():
    """Test that dictionary is not empty"""
    from trigrams import create_trigram_dict
    assert len(create_trigram_dict(book_word_list)) > 0
