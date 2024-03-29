# Biruk_Portfolio
link for Portfolio assessment 0 
https://github.com/birukmamo/Biruk_Portfolio/blob/main/Biruk_Mamo%20(2).pdf

Natural Language Processing (NLP) is a branch of AI that studies how computers and human languages interact, enabling computers to comprehend, decipher, and produce human language. NLU and NLG are subfields of NLP, with NLU focusing on comprehension and NLG on language generation. Modern NLP applications include emotion detection, language translation, and chatbot systems. There are three main approaches to NLP: rule-based, statistical, and neural. The rule-based approach uses predetermined rules and patterns, while the statistical approach uses machine learning methods, and the neural approach uses neural networks. The writer is interested in NLP and wishes to expand their knowledge for personal and professional use, including sentiment analysis and chatbot building.

Link for Portfolio Assessment 1 
https://github.com/birukmamo/Biruk_Portfolio/tree/main/Homework_1

This project is essentially a simple data validation and processing program that reads employee data from a file in CSV format, validates the data, and adds it to a unique list for future reference. The program requires the user to enter an employee ID and phone number in specific formats, which are checked for validity before being added to the list.

Python is a popular language for text processing, as it has built-in libraries and tools for handling and manipulating text data. However, it may not be the fastest language for processing large amounts of text, which could be a potential weakness.

In this project, the program serves as a review of basic programming concepts, such as file input/output, string manipulation, and data validation. Additionally, it highlights the importance of clear communication when explaining technical concepts, as the program's instructions and prompts need to be easily understood by a broad audience. Overall, this project is a practical example of how programming can be used to process and manage data efficiently.

Link for Portfolio Assessment 2
https://github.com/birukmamo/Biruk_Portfolio/tree/main/HW2_BGM210001

I use a Python program that performs natural language processing and a guessing game. Firstly, I preprocess an input file by tokenizing it, removing stop words, lemmatizing the remaining words, and filtering out non-nouns. Then, I display the lexical diversity, tag the unique lemmas, and print the first 20 tagged items, the length of tokens after preprocessing, and the length of nouns after preprocessing. Secondly, I play a guessing game where I randomly pick a word from a list of the 50 most common nouns in the preprocessed text and ask the user to guess the word by entering one letter at a time. The user gets a score, which is initially 5 and decreases with each incorrect guess, and the game ends when the score becomes negative or the user guesses the word. If the user wins, they can choose to play again, and if they lose, I show the word and offer the option to play again. The program takes an input file as a command-line argument, and if one is not provided, it displays an error message.

Link for Portfolio Assessment 3
https://github.com/birukmamo/Biruk_Portfolio/blob/main/Portofolio_Chapter7_wordnet.ipynb%20-%20Colaboratory.pdf

It provides a comprehensive resource for natural language processing applications by organizing words into a hierarchy of semantic relationships, and by including detailed information about word usage in context.

The core of WordNet is a set of synsets, or groups of words that are considered to be synonyms in certain contexts. Each synset is assigned a unique identifier and contains a list of words that are related in meaning. For example, the synset for "car" might include related words such as "automobile", "vehicle", and "motorcar".

In addition to synsets, WordNet also includes detailed information about the relationships between words, such as hypernyms (words that are more general than a given word, e.g. "vehicle" is a hypernym of "car"), hyponyms (words that are more specific than a given word, e.g. "sedan" is a hyponym of "car"), and meronyms (parts that make up a whole, e.g. "wheel" is a meronym of "car").

Overall, the WordNet project has had a significant impact on the field of natural language processing, providing researchers and developers with a powerful tool for analyzing and understanding the structure of language.

Link for Portfolio Assessment 4
https://github.com/birukmamo/Biruk_Portfolio/tree/main/BGM210001_N_Gram

N-grams are a fundamental concept in natural language processing (NLP), which involves the use of computational methods to analyze and understand human language. N-grams refer to contiguous sequences of N items, which can be words, letters, or even phonemes (the smallest units of sound in a language). For example, in the sentence "The cat sat on the mat", the 2-grams (also known as bigrams) are "The cat", "cat sat", "sat on", "on the", and "the mat".

N-grams are widely used in NLP to create language models, which are statistical models that estimate the likelihood of a word given a series of preceding words. Language models are important in many NLP applications, such as speech recognition, machine translation, and text generation. N-gram models are simple yet powerful, and can be easily computed from large amounts of text data.

The basic idea behind N-gram language modeling is to use the frequency of N-grams in a training corpus to estimate the probability of the next word in a sequence, given the previous N-1 words. For example, if the 2-gram "The cat" occurs frequently in the training data, then the model will assign a high probability to the word "sat" following "cat" in a test sequence.

Overall, N-grams and language models are key concepts in NLP, and are essential tools for building systems that can process and generate human language.

Link for Portfolio Assessment 5
https://github.com/birukmamo/Biruk_Portfolio/blob/main/BGM210001_SentenceParsing.pdf

The PSG tree, dependency parsing, and SRL parsing are three different methods of analyzing the structure of a sentence. The PSG tree provides a list of parts of speech but does not analyze grammatical structure. Dependency parsing analyzes relationships between words but can be challenging. SRL parsing recognizes different actors and aspects of an action but does not provide information on the role of each word. Each method has its pros and cons and is useful for different applications.

Link for Portfolio Assessment 6
https://github.com/birukmamo/Biruk_Portfolio/blob/main/web_crawler_Assignment6.py

This is a Python code for web scraping that extracts text from 15 URLs related to the Titanic and builds a knowledge base of 10 relevant terms. The script consists of several functions that perform different tasks, including crawling through the URLs, scraping text from the web pages, cleaning up the text, and finding the 10 most important terms.

The first function, web_crawler(), takes a starting URL and crawls through the web pages, looking for links that contain the word "Titanic". It stops when it has found 15 relevant URLs and writes them to a file.

The second function, text_scrape(), takes the list of URLs found by web_crawler() and scrapes the text from each page. It removes any HTML tags and writes the cleaned text to a separate file for each page.

The third function, cleanup_file(), reads in the cleaned text files and removes any extra whitespace. It then writes the cleaned text to a new file for each page.

The fourth function, find_important_terms(), reads in the cleaned text files and tokenizes the text. It then removes any stop words and generates a list of the most common terms across all 15 pages. It prints out the top 40 most common terms and returns a list of the 10 most important terms.

The fifth function, build_knowledge_base(), reads in the cleaned text files and tokenizes the text into sentences. It then searches each sentence for the 10 most important terms and adds the relevant sentences to a dictionary for each term. It saves the resulting dictionary as a pickle file, which can be loaded later to build the knowledge base.

Overall, the script provides a basic example of how to perform web scraping and build a knowledge base from the scraped text. However, it has some limitations, such as relying on hardcoded terms and not accounting for variations in the text that may refer to the same concept.

