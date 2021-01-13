from bs4 import BeautifulSoup
import requests
import sys
import csv

# link_list = []
#
# with open("unicode_pages_2nd_tier.csv") as f:
#     for subpage in map(str.strip,f):      # Number of pages plus one
url = "http://www.unicode.org/"

uni_page = requests.get(url)

if uni_page.status_code != 200:
    print ("there was an error with", url)


page_html = uni_page.text

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")
#
for link in soup.find_all("a"):
    alink = link.get('href')
    # for lnk in alink:
    with open('unicode_links_2nd.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([url, alink])

        print(url, alink)
