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
    filtered_book = []
    for word in book:
        for c in word:
            word = ''.join([c for c in word if c.isalpha()])
        if word:
            filtered_book.append(word)
    print(filtered_book)
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
    print(trigram_dict)

# def generate_text(book_dict, num):
#     output_string = ''
    #start with first key of dict.
    #append it to the string
    #if key has multiple values - randomly choose one and append it to the string
        #else append value to string
    #break key into list of words, take 2nd word and add it to the value previously appended
    #make new key with those 2 words.
    #search dict for new key. -- repeat above if key in dict.