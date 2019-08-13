#! /usr/bin/env python3

from bs4 import BeautifulSoup

with open("timedtext.html") as fp:
    soup = BeautifulSoup(fp)
    # print(soup.get_text())  # prints html text
    L = [text for text in soup.stripped_strings] # text is stripped and put in list

    f = open("timedtext.txt","w")
    f.write(' '.join(L))
