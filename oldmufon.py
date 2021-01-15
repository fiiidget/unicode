from bs4 import BeautifulSoup
import requests
import sys
import csv

text_lists = []

url = ('http://www.mnmufon.org/abdinv.htm')

ufo_page = requests.get(url)

if ufo_page.status_code != 200:
    print ("there was an error with", url)


page_html = ufo_page.text

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

ufo_story = soup.find_all("pre")

for story in ufo_story:
    text_lists.append(story)

#print(len(text_lists))

with open('mnmufon100.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(text_lists)
