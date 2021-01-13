from bs4 import BeautifulSoup
import requests
import sys
import csv

link_list = []

with open("unicode_pages_2nd_tier.csv") as f:
    for subpage in map(str.strip,f):      # Number of pages plus one
        url = "http://www.unicode.org/{}".format(subpage)

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
                writer.writerow([subpage, alink])

                print(subpage, alink)
        # # story_table = soup.find_all("td", attrs = {"style" : "border: 0px solid rgb(116, 116, 116);"})
        # #
        # # for table_row in story_table:
        # #     a_row = table_row.find_all("table", attrs = {"width" : "98%"})
        # #
        # #     for row in a_row:
        # #         a_link = row.find_all("a")
        # #
        # for the_link in page_links:
        #     a_link = the_link.find_all("href")
        #     link_list.append(a_link)
#CURRENTLY: (NOON 6/30) IS NOT WRITING TO A LIST, JUST LOOPING THROUGH AND LOOKING.
#NEED TO GET JUST THE HREF, WITHOUT AN IDIOT ERROR.
#WHY

#
            # print(link.get("href")) this successfully prints the links
# #

#okay, it just needs to be inside another loop so it doesn't overwrite, and I think you'll have it
