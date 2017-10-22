"""Implement trigrams algorithm to create new text.

Use trigrams algorithm to randomly generate text based on an
an input text file, and given a number of words to generate.
"""


def read_book_from_file():
    """."""
    with open('text.txt', 'r') as book:
        book_contents = book.read()
    return book_contents


def convert_book_to_list_of_words(book):
    """Remove whitespace and punctuation from word list.

    and return list.
    """
    book = book.replace('\n', ' ')
    book = book.split(' ')
    book = [w[0:-1] if not w.isalpha() else w for w in book]
    return book[0: -1]
