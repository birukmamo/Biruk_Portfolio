#######
# File: Wob Crawler
# Author: Gebresilassie Takele (gtt210000)
#       : Biruk Mamo    (bgm210001)
# Date: 3/11/2023
# course: CS 4395.001 - Portfolio Assignmet 6
#######

import re
import requests
import pickle
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords


#  Crawls through several URLs from starting URL; will stop when we get 15 relevant URLs.

def web_crawler(starting_url):
    urls_found = []

    r = requests.get(starting_url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    links_for_web = soup.find_all('a')

    with open('urls.txt', 'w') as file:
        for link in links_for_web:
            if len(urls_found) == 15:
                break

            link_string = str(link.get('href'))
            if 'titanic' in link_string or 'Titanic' in link_string:
                if link_string.startswith('http') and 'google' not in link_string and 'facebook' not in link_string and 'twitter' not in link_string and 'instagram' not in link_string and "britannica" not in link_string and "ny" not in link_string and "pinterest" not in link_string:
                    file.write(link_string + '\n')
                    urls_found.append(link_string)
    file.close()

    return urls_found

# Checks to see if an element is visible

def check_if_visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


def text_scrape(urls_visited):

    counter = 0

    for url in urls_visited:
        counter += 1
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'User-Agent': 'My User Agent 1.0'})
        html = urlopen(req, timeout=10)
        soup = BeautifulSoup(html, features='html.parser')
        data = soup.findAll(text=True)
        result = filter(check_if_visible, data)
        temp_list = list(result)
        text = ' '.join(temp_list)

        # Write text out to file
        with open(('rawfile{}'.format(counter)), 'w', encoding='utf-8') as file:
            file.write(text)
        file.close()


def cleanup_file():

    for counter in range(1, 16):
        with open("rawfile{}".format(counter), 'r', encoding='utf-8') as file:
            text = file.read()
        file.close()

        text = ' '.join(text.split())

        with open("cleanup_textfile{}".format(counter), 'w', encoding='utf-8') as file:
            file.write(text)
        file.close()


def find_important_terms():

    with open('text_reformatted.txt', 'w', encoding='utf-8') as file:
        for counter in range(1, 16):
            with open("cleanup_textfile{}".format(counter), 'r', encoding='utf-8') as f:
                text = f.read()
            f.close()
            file.write(text)
    file.close()

    with open('text_reformatted.txt', 'r', encoding='utf-8') as file:
        raw_text = file.read()
    file.close()

    all_text = word_tokenize(raw_text)
    tokens_all_text = [token.lower() for token in all_text]
    tokens_all_text = [token for token in tokens_all_text if token.isalpha() and
                            token not in stopwords.words('english')]

    with open('text_tokenized.txt', 'w', encoding='utf-8') as file:
        file.write(str(tokens_all_text))
    file.close()

    with open('text_tokenized.txt', 'r') as file:
        raw_text = file.read()
    file.close()

    tokens_all_text = word_tokenize(raw_text)
    unigrams = tokens_all_text
    unigram_dict = {token: unigrams.count(token) for token in set(unigrams)}

    sorted_unigrams = sorted(unigram_dict.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 40 most common terms in all 15 pages:")
    for counter in range(2, 42):
        print("{}.".format(counter - 1), sorted_unigrams[counter])

    # Pick 10 terms from the 40
    my_10_terms = ["film", "Ship", "Titanic", "Atlantic", "Sink",
                   "James", "Cameron", "story", "Ocean", "Dicaprio"]

    return my_10_terms


def build_knowledge_base(my_10_terms):

    with open('text_reformatted.txt', 'r', encoding='utf-8') as file:
        raw_text = file.read()
    file.close()

    sentences = sent_tokenize(raw_text)

    sentences_with_terms = []
    my_10_terms_dict = {"film": [], "Ship": [], "Titanic": [], "Atlantic": [], "Sink": [],
                        "James": [], "Cameron": [], "story": [], "Ocean": [], "Dicaprio": []}

    for term in my_10_terms:
        for sent in sentences:
            if term in sent:
                sentences_with_terms.append(sent)
        temp = sentences_with_terms
        my_10_terms_dict[term] += temp
        sentences_with_terms.clear()

    pickle.dump(my_10_terms_dict, open('my_10_terms_dict.p', 'wb'))
    my_10_terms_knowledge_base = pickle.load(open('my_10_terms_dict.p', 'rb'))

    with open('knowledge_base', 'w', encoding='utf-8') as file:
        for key, value in my_10_terms_knowledge_base.items():
            file.write(key)
            file.write(": ")
            file.write(str(value))
            file.write("\n")
    file.close()


if __name__ == "__main__":
    starting_url = "https://en.wikipedia.org/wiki/Titanic"

    # Crawl through URLs and get 15 relevant URLs
    visited_urls = web_crawler(starting_url)

    # Scrape text from each URL
    text_scrape(visited_urls)

    # Clean up text in files
    cleanup_file()

    # Find the 40 most important terms from the pages
    my_10_terms = find_important_terms()

    # Build knowledge base using 10 words chosen from previous 40
    build_knowledge_base(my_10_terms)
