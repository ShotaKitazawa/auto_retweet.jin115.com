import sys
import json
import requests
import re
from bs4 import BeautifulSoup


def scraping(url):
    response = requests.get(url)
    if response.status_code == 404:
        print("NotFound")
        return
    html = response.text.encode(response.encoding, "ignore")
    soup = BeautifulSoup(html, "lxml")
    sources = soup.select(".twitter-tweet")
    print(sources)


if __name__ == '__main__':
    argvs = sys.argv
    # if len(argvs) != 2:
    #    print("Usage: python {0} [url] ".format(argvs[0]))
    #    exit()
    url = argvs[1]
    #url = "http://jin115.com/archives/52165633.html"

    scraping(url)
