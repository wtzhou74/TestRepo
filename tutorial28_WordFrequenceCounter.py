import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    # extract content included in tag a where class is index_singleListingTitles
    for post_text in soup.findAll('a', {'class':'index_singleListingTitles'}):
        content = post_text.string  # get the string content
        words = content.lower().split()
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)
    # clean up word list
    clean_up_list(word_list)

# clean up word list
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%&*()+\"][}{"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            # print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

# create a dictionary
def create_dictionary(clean_word_list):
    word_count = {} # dictionary
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # sort the dictionary based on word's frequence
    # itemgetter(1) means that the dictionary was sorted based on value
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

start('https://buckysroom.org...')