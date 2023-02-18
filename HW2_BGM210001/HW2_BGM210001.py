import sys     # to get the system parameter
import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import random


# preprocessing the input file
def preprocessing(input):
    # Tokenizing the lowercase and variable to store the stopwords
    tokens = word_tokenize(input.lower())
    wordStop = set(stopwords.words('english'))
    # choose the tokenizer ones that are greater than 5, alpha and not stopwords
    tokens = [t for t in tokens if t.isalpha() and t not in wordStop and len(t) > 5]
    # lemmatize the tokens and use set to make them unique lemmas
    uniqueLemmas = sorted(list(set([WordNetLemmatizer().lemmatize(r) for r in tokens])))
    # POS tagging on the unique lemmas and print the first 20 tagged items
    lemmasUniqueTags = nltk.pos_tag(uniqueLemmas)
    # create a list of only those lemmas that are nouns
    nounLemmas = list([x[0] for x in lemmasUniqueTags if x[1].startswith("N")])
    # print the output
    print("\nLexical diversity: %.2f" % (len(uniqueLemmas) / (len(tokens))))
    print('\nFirst 20 Tagged words:', lemmasUniqueTags[:20])
    print('\nlen fo tokens after preprocessing: ', len(tokens))
    print('\nlen for nouns after preprocessing: ', len(nounLemmas))
    # return tokens
    return tokens, nounLemmas

# Guessing game function
def guess_game(list):

    initial_score = 5
    # select one number from 50 chosen words
    random_picked = random.choice(list)[0]
    letter_found = []
    users_guess = []

    print("\nScore: ", initial_score, "\n")

    for element in random_picked:
        print('_', end=" ")

    # stop when the score is less than 0.
    while initial_score > -1:
        user_input = input('\n\nPlease enter a letter: ').lower()
        # if the input is not letter
        if not user_input.isalpha() and user_input != "!":
            print("\nError: Input valid letter.")
        # if the input is already tried
        elif user_input in users_guess:
            print("\nError: You already tried that.")
        # When user enters '!' game will ends such like when the score becomes negative
        elif user_input != "!":
            # All the guesses the user has made into a list
            users_guess.append(user_input)

            if user_input in random_picked:
                initial_score += 1
                letter_found.append(user_input)
                print("\nRight! Score is: ", initial_score)

            # if letter is not in word subtract 1 from score
            else:
                initial_score -= 1
                print("Sorry, guess again. Score is ", initial_score)

            # update score and print current status of game
            count = 0
            for element in random_picked:
                if element in letter_found:
                    print(element, end=" ")
                    count += 1
                else:
                    print('_', end=" ")

            # after each try show user the score
            print("\nYour Score:", initial_score)

            # If word is guessed game over.
            if count == len(random_picked):

                retry_game = input("\n\nYou made it through! Play again? (Y/N) ")
                if retry_game.lower() == "y":
                    guess_game(list)
                else:
                    print("\nThank you for playing!")
                    sys.exit(0)

        else:
            print("\nThanks for playing!")
            sys.exit(0)

    # Show user score if the lost.. show the word.
    print("\n\nYou lost by score")
    print("The word was:", random_picked)

    retry_game = input("\nDo you want to play again? (Y/N) ")
    if retry_game.lower() == "y":
        guess_game(list)
    else:
        print("\nThanks for playing!")
        sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        print('Input file: ', input_file)

        with open('anat19.txt', 'r') as f:
            raw_text = f.read()

        tokens, noun_lemmas = preprocessing(raw_text)
        common_list =[]

        counts = {t: tokens.count(t)
        for t in noun_lemmas}
        words_sorted = sorted(counts.items(), key= lambda x: x[1], reverse = True)  # saving to be used in the game
        print("50 most common words: ")
        for i in range(50):
            common_list.append(words_sorted[i])
            print(words_sorted[i])

        guess_game(common_list)
    else:
        print('ERROR: File name is missing.')