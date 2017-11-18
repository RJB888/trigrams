# Trigrams

Authors: 
Rob Bronson
Darren Haynes

### Codefellows 401 Python Course Assignment

Objective: Take a piece of text of arbitrary size and create new text using trigrams. Trigram analysis is very simple. Look at each set of three adjacent words in a document. Use the first two words of the set as a key, and remember the fact that the third word followed that key. Once you’ve finished, you know the list of individual words that can follow each two word sequence in the document. These words are then implemented in an heuristics algorithm to create new text.

Reads a book of text from a file, replaces any newlines with a space character. Then it splits the text on spaces into a list.  We then iterate over each word and keep only the alpha characters - effectively stripping any punctuation out of the text, leaving only actual words.
We then create a key of 2 words from the list and start a dictionary consisting of the key words and the next word as their value.  Any repeated 2-word key accumulates a list of "3rd words" to be chosen from.  We then build trigrams from that dictionary.  If we run out of possibilities for keys before we have reached the desired ooutput text length, we re-randomize the key and continue to generate trigrams.

