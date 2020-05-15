# install beautifulsoup4 bc more up to date than becautifulsoup
# also need a parser to parse html- reccomend lxml parser
# -- pip install lxml; can also use the html5lib parser -- pip install html5lib
# pip install requests

from bs4 import BeautifulSoup
import requests
import csv

# step 1. grab the website that you will be scraping
# this returns response object, you grab text of response object using .text
source = requests.get('https://blog.remodical.com/').text
# step 2. parse the contents of the website using beautiful soup
soup = BeautifulSoup(source, 'lxml')

# use prettify() to make the parsed content neat and well formatted
# print(soup.prettify())
# soup.title to get entire title tag
# or soup.title.text just to get the text.
# this will get you the first title tag (or any tag) in the page
# soup.find('div', class_='footer') will pull up the div tags with the class of footer

# create a numpy array to store all data
article_array = []
articles_array = []

# step 3. grab the text in the anchor tag containing the article content
# comment out/uncomment out multiple things using ctrl + /
for preview in soup.find_all('a', class_='post-link'):  # find() to get first entry only, find_all() to grab all instances on page
    article_array = []
    article_array.append(preview.text.strip())
    article_array.append('https://blog.remodical.com/' + preview['href'])
    articles_array.append(article_array)

#write to csv file
with open('article_list.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(articles_array)