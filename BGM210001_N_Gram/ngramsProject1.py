#######
# File: ngramsProject1.py
# Author: Gebresilassie Takele (gtt210000)
#       : Biruk Mamo    (bgm210001)
# Date: 3/04/2023
# course: CS 4395.001 - Portfolio Assignmet 4 (Program 1)
#######

import pickle
from nltk.util import ngrams
from nltk import word_tokenize


# create a function with a filename as argument
def process_file(raw_file):
    
    f = open(raw_file, 'r', encoding='utf-8')
    # b. read in the text and remove newlines
    raw_text = ''.join(f.read().splitlines())
    f.close()

    # c. tokenize the text
    tokens = word_tokenize(raw_text)

    # d-e. use nltk to create a bigrams list and unigrams list
    # f. use the bigram list to create a bigram dictionary of bigrams and counts
    # g. use the unigram list to create a unigram dictionary of unigrams and counts
    unigrams = tokens
    bigrams = list(ngrams(tokens, 2))
    unigram_dictionary = {t: unigrams.count(t) for t in set(unigrams)}
    bigram_dictionary = {b: bigrams.count(b) for b in set(bigrams)}

    # h. return the unigram dictionary and bigram dictionary from the function
    return unigram_dictionary, bigram_dictionary


# Main function
def main():
    # create file names
    english_file = 'LangId.train.English'
    french_file = 'LangId.train.French'
    italian_file = 'LangId.train.Italian'

    # Get the unigram and bigram dictionaries for all 3 files and
    # Save the dictionaries as a pickle file
    english_unigram, english_bigram = process_file(english_file)
    pickle.dump(english_unigram, open('english_unigram', 'wb'))
    pickle.dump(english_bigram, open('english_bigram', 'wb'))

    french_unigram, french_bigram = process_file(french_file)
    pickle.dump(french_unigram, open('french_unigram', 'wb'))
    pickle.dump(french_bigram, open('french_bigram', 'wb'))

    italian_unigram, italian_bigram = process_file(italian_file)
    pickle.dump(italian_unigram, open('italian_unigram', 'wb'))
    pickle.dump(italian_bigram, open('italian_bigram', 'wb'))

# Start here
main()
