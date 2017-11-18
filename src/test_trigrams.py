"""Test that the trigrams algorithm produces proper output."""
import pytest
from trigrams import convert_book_to_list_of_words, create_trigram_dict


def get_book():
    with open('sherlock_small.txt', 'r') as book:
        book = book.read()
    return book


book = get_book()
book_word_list = convert_book_to_list_of_words(get_book())
trigrams = create_trigram_dict(book_word_list)

TRIGRAM_TABLE = [
    (trigrams, 1),
    (trigrams, 10),
    (trigrams, 11),
    (trigrams, 17),
    (trigrams, 99),
    (trigrams, 100),
    (trigrams, 500),
    (trigrams, 5000),
    (trigrams, 50000),
    (trigrams, 500000),
]


def test_read_book_from_file():
    """Test that book is converted to and returned as a string"""
    from trigrams import read_book_from_file
    assert type(read_book_from_file('sherlock.txt')) == str


def test_words_are_only_alpha():
    """Test all non-alpha characters have been removed from text"""
    from trigrams import convert_book_to_list_of_words
    assert ''.join(convert_book_to_list_of_words(book)).isalpha()


def test_create_trigram_dict_returns_a_dict():
    """Test that a dict object is actually returned"""
    from trigrams import create_trigram_dict
    assert type(create_trigram_dict(book_word_list)) == dict


def test_create_trigram_dict_len_greater_than_one():
    """Test that dictionary is not empty"""
    from trigrams import create_trigram_dict
    assert len(create_trigram_dict(book_word_list)) > 0


def test_generate_text_function_returns_a_str():
    """Test 'generate_text()' function returns a string"""
    from trigrams import generate_text
    assert type(generate_text(trigrams, 50)) == str


@pytest.mark.parametrize('trigrams, num', TRIGRAM_TABLE)
def test_generate_text_function_creates_correct_num_of_words(trigrams, num):
    """Test generated text matches parameter int passed in as arg"""
    from trigrams import generate_text
    assert len(generate_text(trigrams, num).split(' ')) == num
