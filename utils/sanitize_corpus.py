# Utilize this entry point to sanitize a file of all punctuation, stop words 
#(by a flag), set characters to lowercase, and remove numbers.

import re

# Description: Non-helper method to call for sanitizing an input text corpus.
#
# Arguments: 
#   corpus: Input array of sentences
#   save_stopwords: flag for whether or not to leave stopwords
#
# Return: Corpus: Array of sanitized sentences
def sanitize_corpus(corpus, save_stopwords = False):

    # remove all stopwords if the flag is set
    if (not remove_stopwords):
        corpus = remove_stopwords(corpus)

    # remove all punctuation (TODO: decide whether to remove periods)
    corpus = remove_punctuation(corpus)

    # remove all numerals
    corpus = remove_numbers(corpus)

    # strip all extraneous whitespace
    corpus = reduce_whitespace(corpus)

    # all to lowercase
    corpus = corpus.lower()

    return corpus

# TODO: Implement
def remove_stopwords(corpus):
    return corpus

# TODO: Implement, decide whether to save periods
def remove_punctuation(corpus):
    return corpus

def remove_numbers(corpus):
    corpus = re.sub(r'\d+', '', corpus)

    return corpus

# TODO: Implement
def reduce_whitespace(corpus):
    return corpus
