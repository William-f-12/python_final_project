#! python3
# SearchTools.py - some useful searching tools

def Usage():
    print("""
Usage:
    #1
    Search(question: "the question you want to search")

    ==> search the question in some websites
    """)

from selenium import webdriver

def Search(question: str):
    """search the question in some websites"""

    if type(question) != str:
        raise TypeError("input has to be a string")
    browser = webdriver.Firefox()

    browser.get("about:preferences")
    box = browser.find_element_by_id("linkTargeting")
    if not box.get_attribute("checked"):
        box.click()

    # search it in google
    browser.get("https://www.google.com/search?client=firefox-b-d&q={}".format(question))

    # search it in google scolar
    js = 'window.open(' + '"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C14&q=' + question + '");'
    browser.execute_script(js)

    # search it in bilibili
    js = 'window.open(' + '"https://search.bilibili.com/all?keyword=' + question + '");'
    browser.execute_script(js)

    # search it in CSDN
    js = 'window.open(' + '"https://so.csdn.net/so/search?q=' + question + '");'
    browser.execute_script(js)

    # search it in youtube
    js = 'window.open(' + '"https://www.youtube.com/results?search_query=' + question + '");'
    browser.execute_script(js)


if __name__ == "__main__":
    Usage()
    Search("Gradient descent")
    
    
