# Utilize this entry point to sanitize a file of all punctuation, stop words 
#(by a flag), set characters to lowercase, and remove numbers.


import csv
import nltk
import re
import string
import sys

import pandas as pd

from nltk.corpus import stopwords

csv.field_size_limit(sys.maxsize)

# Description: Non-helper method to call for sanitizing an input text entry.
#
# Return: data: Array of sanitized sentences
def sanitize_data(data, min_frequency = 10, remove_stopwords = True,
        save_sanitized = False, sanitized_name = 'default_sanitized.csv',
        save_word_freq = False, word_freq_name = 'word_freq.csv',
        save_letter_freq = False, letter_freq_name = 'letter_freq.csv'):

    stopwords = {*()}
    word_freq = {}
    letter_freq = {}
    final_word_freq = {}
    final_letter_freq = {}

    # load list of stopwords
    if (remove_stopwords):
        with open('data/stopwords.txt', 'r') as s:
            for word in s:
                stopwords.add(word[:-1])
    print(stopwords)

    for e, row in data.iterrows():
        # all to lowercase
        data.iat[e, 0] = remove_uppercase(data.iat[e, 0])
        
        # attempt to remove non-english characters by encoding to 
        # ascii back to unicode again and ignoring failures
        data.iat[e, 0] = remove_nonenglish(data.iat[e, 0])

        # remove all punctuation (TODO: decide whether to remove periods)
        # remove all numerals
        data.iat[e, 0] = remove_numbers(data.iat[e, 0])
        
        # strip all extraneous whitespace
        data.iat[e, 0] = reduce_whitespace(data.iat[e, 0])
    
        # remove whatever punctuation that string can match
        data.iat[e, 0] = remove_punctuation(data.iat[e, 0])
    
        # remove single character words (also non-english?)
        data.iat[e, 0] = remove_single(data.iat[e, 0])
        
        # get the frequencies of each letter and word
        word_freq, letter_freq = find_frequency(data.iat[e, 0], 
                word_freq, letter_freq)

        # remove words that do not meet frequency requirements and
        # strip out the stopwords as enumerated by nltk
        data.iat[e, 0] = remove_frequency_and_stopwords(data.iat[e, 0], 
                word_freq, min_frequency, stopwords)

        # get the frequencies of each letter and word
        final_word_freq, final_letter_freq = find_frequency(data.iat[e, 0], 
                final_word_freq, final_letter_freq)

    if (save_sanitized):
        data.columns = ['content']
        data.to_csv('data/' + sanitized_name, mode = 'a', header = True, index = False)

    if (save_word_freq):
        with open('data/' + word_freq_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in final_word_freq.items():
                writer.writerow([key, value])

    if (save_letter_freq):
        with open('data/' + letter_freq_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in final_letter_freq.items():
                writer.writerow([key, value])

    return data

def remove_nonenglish(entry):
    return entry.encode('ascii', 'ignore').decode('utf-8', 'ignore')

def remove_stopwords(entry):
    for word in stopwords.words('english'):
        entry = re.sub('\s+'+ word + '\s+', '', entry)

    return entry

def remove_uppercase(entry):
    return entry.lower()

# Code from: 'https://stackoverflow.com/questions/265960/
# best-way-to-strip-punctuation-from-a-string'
def remove_punctuation(entry):
    return entry.translate(str.maketrans('', '', string.punctuation))

def remove_numbers(entry):
    return re.sub(r'\d+', '', entry)

def reduce_whitespace(entry):
    entry = re.sub('\s+', ' ', entry)
    return re.sub(' +', ' ', entry)

def remove_single(entry):
    return re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', entry)

def find_frequency(entry, word_freq, letter_freq):
    words = entry.split(' ')

    for word in words:
        if (word in word_freq.keys()):
            word_freq[word] += 1
        else:
            word_freq[word] = 1

        for letter in word:
            if (letter in letter_freq):
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    return word_freq, letter_freq

def remove_frequency_and_stopwords(entry, word_freq, min_freq, stopwords):
    words = entry.split(' ')

    clean_entry = ''

    for i, word in enumerate(words):
        if (word_freq[word] >= min_freq and word not in stopwords):
            clean_entry += word
            if (not i == len(words) - 1):
                clean_entry += ' '
        
    return clean_entry
