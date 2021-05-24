#! python3
# Translate.py - translate!!

import requests, bs4

def Trans(text: str, input_lan: str="english", output_lan: str="chinese"):
    """input_lan: the language need to be translated; 
    output_lan: the language the text needs to be translated to;
    text: the text you want to translate"""

    url = r"https://translate.google.com/?sl={}&tl={}&text={}".format(input_lan, output_lan, text)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    result_text = soup.select("span[jsname='W297wb']")


    print(result_text)
    print(url)


if __name__ == "__main__":
    Trans("critical points")