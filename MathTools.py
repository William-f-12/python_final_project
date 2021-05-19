#! python3
# MathTools.py - some helpful math tools.

def Usage():
    print("""
Usage:
    #1
    GraphingCalculator(function: a math function)

    ==> to open the graphing calculator and copy the function

    #2
    Wolfarm(input: "an input to enter in wolfarm alpha")

    ==> open wolfarm alpha and search for the input

    #3
    Mathematics(question: "question you want to ask")

    ==> search the question in stackexchange.com
    """)

import pyperclip
from selenium import webdriver

def GraphingCalculator(function: str):
    """recive a function and find its graph"""

    browser = webdriver.Firefox()
    browser.get(r"https://www.desmos.com/calculator")
    pyperclip.copy(function)

def Wolfarm(input: str):
    """open wolfarm alpha and search for the input"""

    browser = webdriver.Firefox()
    browser.get(r"https://www.wolframalpha.com/")
    bar = browser.find_element_by_class_name("_2oXzi")
    bar.send_keys(input)
    bar.submit()

def Mathematics(question: str):
    """search the question in stackexchange.com"""

    if type(question) != str:
        raise TypeError("input has to be a string")

    browser = webdriver.Firefox()
    browser.get(r"https://math.stackexchange.com/search?q={}".format(question))


if __name__ == "__main__":
    Usage()
