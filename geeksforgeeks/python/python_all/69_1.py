Scraping Covid-19 statistics using BeautifulSoup



Coronavirus, one of the biggest pandemic has brought all the world to Danger.
Along with this, it is one of the trending News, everyone has this day. In
this article, we will be scraping data and printing Covid-19 statistics in
human-readable form. The data will be scraped from this website  
 **Prerequisites:**  

  * The libraries ‘requests’, ‘bs4’, and ‘texttable’ have to be installed –  

    
    
    pip install bs4
    pip install requests
    pip install texttable
    

**Project :** Let’s head over to code, create a file called run.py.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing modules

import requests

from bs4 import BeautifulSoup

# URL for scrapping data

url = 'https://www.worldometers.info/coronavirus/countries-where-
coronavirus-has-spread/'

# get URL html

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

data = []

# soup.find_all('td') will scrape every

# element in the url's table

data_iterator = iter(soup.find_all('td'))

# data_iterator is the iterator of the table

# This loop will keep repeating till there is

# data available in the iterator

while True:

 try:

 country = next(data_iterator).text

 confirmed = next(data_iterator).text

 deaths = next(data_iterator).text

 continent = next(data_iterator).text

 # For 'confirmed' and 'deaths',

 # make sure to remove the commas

 # and convert to int

 data.append((

 country,

 int(confirmed.replace(', ', '')),

 int(deaths.replace(', ', '')),

 continent

 ))

 # StopIteration error is raised when

 # there are no more elements left to

 # iterate through

 except StopIteration:

 break

# Sort the data by the number of confirmed cases

data.sort(key = lambda row: row[1], reverse = True)  
  
---  
  
 __

 __

To print the data in human-readable format, we will use the library ‘
_texttable_ ‘  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# create texttable object

import texttable as tt

table = tt.Texttable()

# Add an empty row at the beginning for the headers

table.add_rows([(None, None, None, None)] + data)

# 'l' denotes left, 'c' denotes center,

# and 'r' denotes right

table.set_cols_align(('c', 'c', 'c', 'c')) 

table.header((' Country ', ' Number of cases ', ' Deaths ', '
Continent '))

print(table.draw())  
  
---  
  
 __

 __

