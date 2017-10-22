"""Test that the trigrams algorithm produces proper output."""
import pytest


def get_book():
    with open('sherlock.txt', 'r') as book:
        book = book.read()
    return book


book = get_book()


# @pytest.mark.parametrize('book, result', BOOKS_TABLE)
def test_words_are_only_alpha():
    """Test all non-alpha characters have been removed from text"""
    from trigrams import convert_book_to_list_of_words
    assert  ''.join(convert_book_to_list_of_words(book)).isalpha()



