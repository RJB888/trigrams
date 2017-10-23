"""Implement trigrams algorithm to create new text.

Use trigrams algorithm to randomly generate text based on an
an input text file, and given a number of words to generate.
"""
from random import sample
import sys


def read_book_from_file(book):
    """take a .txt file and read it into a string"""
    with open(book, 'r') as book:
        book_contents = book.read()
    return book_contents


def convert_book_to_list_of_words(book):
    """Remove whitespace and punctuation from word list and return list."""
    book = book.replace('\n', ' ')
    book = book.split(' ')
    filtered_book = []
    for word in book:
        for c in word:
            word = ''.join([c for c in word if c.isalpha()])
        if word:
            filtered_book.append(word)
    return filtered_book


def create_trigram_dict(book_word_list):
    """Generate dictionary of trigrams using filtered boook."""
    trigram_dict = {}
    for idx, word in enumerate(book_word_list):
        if len(book_word_list) > idx + 2:
            dict_key = book_word_list[idx] + ' ' + book_word_list[
                idx + 1]
            if dict_key in trigram_dict:
                trigram_dict[dict_key].append(book_word_list[idx + 2])
            else:
                trigram_dict[dict_key] = [book_word_list[idx + 2]]
    return trigram_dict


def generate_text(book_dict, num):
    """Generate new text with trigram algorithm"""
    new_key = ''.join(sample(list(book_dict), 1))
    output_list = new_key.split(' ')
    while len(output_list) < num:
        if new_key in book_dict:
            output_list.append(''.join(sample(book_dict[new_key], 1)))
            new_key = output_list[-2] + ' ' + output_list[-1]
    return ' '.join(output_list[0:num])


def main(book, num):
    """Call all necessary functions and return the new trigram text"""
    book_text = read_book_from_file(book)
    filtered_book = convert_book_to_list_of_words(book_text)
    trigram_dict = create_trigram_dict(filtered_book)
    return generate_text(trigram_dict, num)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("You used an incorrect number of arguments")
        sys.exit(1)

    try:
        output = main(sys.argv[1], int(sys.argv[2]))
    except RuntimeError:
        print("There was an issue. Try again with correct parameters")
        sys.exit()

    print(output)
