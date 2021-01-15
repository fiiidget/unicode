from bs4 import BeautifulSoup
import requests
import sys
import csv

link_list = []
url = ("https://www.unicode.org/")

#with open("2021 peek.csv") as f:
#for subpage in map(str.strip,f):      # Number of pages plus one

uni_page = requests.get(url)

if uni_page.status_code != 200:
    print ("there was an error with", url)


page_html = uni_page.text

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

unilinks = soup.find_all("a")
#do this for loop, and then add a second one to get the hrefs.

for link in unilinks:
    alink = link.get('href')

    for lnk in alink:



                #print(url, alink)
print("something is happening here")
