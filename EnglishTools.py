#! python3
# EnglishTools.py - some helpful english tools

def Usage():
    print("""
Usage:
    #1
    Thesaurus(word: "the word you want to search")

    ==> open thesaurus.com to find the thesaurus for the word

    #2
    Dictionary(word: "the word you want to search")

    ==> open dictionary.com to find the definition of the word
    """)

import requests, bs4
from selenium import webdriver

def Thesaurus(word: str):
    """open thesaurus.com to find the thesaurus for the word"""

    if type(word) != str:
        raise TypeError("input has to be a string")
    word = word.lower()

    res = requests.get(r"http://www.thesaurus.com/browse/{}".format(word))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    word_list = soup.select("li > a[data-linkid='nn1ov4']")[:5]

    for i in range(len(word_list)):
        word_list[i] = word_list[i].getText()

    return word_list

    
def Dictionary(word: str):
    """open dictionary.com to find the definition of the word"""

    if type(word) != str:
        raise TypeError("input has to be a string")
    word = word.lower()

    browser = webdriver.Firefox()
    browser.get(r"http://www.dictionary.com/browse/{}".format(word))


if __name__ == "__main__":
    Usage()
    print(Thesaurus("cat"))
    # Dictionary("colic")
