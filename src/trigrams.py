"""Implement trigrams algorithm to create new text.

Use trigrams algorithm to randomly generate text based on an
an input text file, and given a number of words to generate.
"""


def read_book_from_file():
    """."""
    with open('sherlock.txt', 'r') as book:
        book_contents = book.read()
    return book_contents


def convert_book_to_list_of_words(book):
    """Remove whitespace and punctuation from word list.

    and return list.
    """
    book = book.replace('\n', ' ')
    book = book.split(' ')
    filtered_book = []
    for word in book:
        for c in word:
            word = ''.join([c for c in word if c.isalpha()])
        if word:
            filtered_book.append(word)
    return filtered_book
