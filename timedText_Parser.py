#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from get_http_timed_text import timedtext_url



if __name__ == '__main__':
    timedtext_obj = timedtext_url(input('Input youtube_url: ') )
    timedtext_url = timedtext_obj.get_timedtext_url()
    r = requests.get(timedtext_url)
    soup = BeautifulSoup(r.text, features='lxml')
    print(soup.get_text())  # prints html text
    # L = [text for text in soup.stripped_strings] # text is stripped and put in list



    # f = open("timedtext.txt","w")
    # f.write(' '.join(L))
