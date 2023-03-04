#######
# File: ngramsProject1.py
# Author: Gebresilassie Takele (gtt210000)
#       : Biruk Mamo    (bgm210001)
# Date: 3/04/2023
# course: CS 4395.001 - Portfolio Assignmet 4 (Program 2)
#######

import pickle
from nltk.util import ngrams
from nltk import word_tokenize


def main():

    # store text into a list
    text = []
    with open('LangId.test', 'r', encoding='utf-8') as f:
        for line in f:
            text.extend([line[:-1]])

    languages = ['English', 'French', 'Italian']

    laplace(text, languages)

    # store correct languages into a list
    language = []
    with open('LangId.sol', 'r', encoding='utf-8') as f:
        for line in f:
            language.append(line.split()[-1])
    # store guesses into a list
    guesses = []
    with open('guesses.txt', 'r', encoding='utf-8') as f:
        for line in f:
            guesses.append(line.split()[-1])

    # compares guesses with the actual language
    accurate, mismatch = accuracy(guesses, language)
    print("Accuracy: " + str(int(accurate*100)) + "%")
    print("Lines wrongly classified: " + str(mismatch))


def load_languages(languages_used):
    vocabulary = 0
    # store the languages into a dictionary
    languages = {}
    # loops through the languages usd
    for language in languages_used:
        unigram = pickle.load(open(language.lower()+'_unigram', 'rb'))
        bigram = pickle.load(open(language.lower()+'_bigram', 'rb'))
        languages[language] = (bigram, unigram)
        # Adding to the total vocabulary for laplace algorithm
        vocabulary += len(unigram)

    return languages, vocabulary


# laplace will use the laplace algorithm to guess the language
# returns a list of the predictions for the languages
def laplace(text, languages_used):

    languages, vocabulary = load_languages(languages_used)

    f = open("guesses.txt", "w")

    for line in range(len(text)):
        unigrams = word_tokenize(text[line])
        bigrams = list(ngrams(unigrams, 2))

        max_prob = 0
        guess = 'English'

        # loops through each language
        for language in languages:
            current_prob = 1
            # loops through each bigram
            for b in bigrams:

                n = languages[language][0][b] if b in languages[language][0] else 0
                d = languages[language][1][b[0]] if b[0] in languages[language][1] else 0
                # laplace algorithm equation
                current_prob *= (n + 1) / (d + vocabulary)

            # check if guess needs to be changed
            if current_prob > max_prob:
                max_prob = current_prob
                guess = language
        f.write(str(line+1)+" "+guess+"\n")
    f.close()


def accuracy(guess, correct):
    wrong_lines = []
    inaccurate = 0
    # loops to see if the values are the same or not
    for index in range(len(guess)):
        if guess[index] != correct[index]:
            inaccurate += 1
            wrong_lines.append(index+1)
    return 1 - inaccurate/len(guess), wrong_lines


if __name__ == "__main__":
    main()
