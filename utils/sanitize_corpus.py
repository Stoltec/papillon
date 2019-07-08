# Utilize this entry point to sanitize a file of all punctuation, stop words 
#(by a flag), set characters to lowercase, and remove numbers.


import csv
import re
import sys

import pandas as pd

csv.field_size_limit(sys.maxsize)

# Description: Non-helper method to call for sanitizing an input text entry.
#
# Arguments: 
#   entry: Input array of sentences
#   save_stopwords: flag for whether or not to leave stopwords
#
# Return: data: Array of sanitized sentences
def sanitized_dataset(data, min_frequency = 50, save_stopwords = False):

    freq = []

    for e, row in enumerate(data):
        # remove all punctuation (TODO: decide whether to remove periods)
        #entry = remove_punctuation(entry)
    
        # remove all numerals
        data[e] = remove_numbers(date[e])
        
        # strip all extraneous whitespace
        data[e] = reduce_whitespace(data[e])
    
        # all to lowercase
        data[e] = data[e].lower()
        
        # remove all stopwords if the flag is set
        if (not remove_stopwords):
            data[e] = remove_stopwords(data[e])
    
        print(data[e])
        print('\n')

    return data

# TODO: Implement
def remove_stopwords(entry):
    return entry

# TODO: Implement, decide whether to save periods
def remove_punctuation(entry):
    return entry

def remove_numbers(entry):
    return re.sub(r'\d+', '', entry)

# TODO: Implement
def reduce_whitespace(entry):
    return re.sub(" +", " ", entry)

