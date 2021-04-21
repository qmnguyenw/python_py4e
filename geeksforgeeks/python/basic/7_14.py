Corona Virus Live Updates for India – Using Python



As we know the whole world is being affected by the COVID-19 pandemic and
almost everyone is working from home. We all should utilize this duration at
best, to improve our technical skills or writing some good Pythonic scripts.  
Let’s see a simple Python script to demonstrate the state-wise coronavirus
cases in India. This Python script fetches the live data from the Ministry of
Health Affairs Official Website. Then data is represented in the horizontal
bar graph.  
To run this script follow the below installation –  

    
    
    $ pip install bs4
    $ pip install tabulate
    $ pip install matplotlib
    $ pip install numpy 
    $ pip install requests
    

  
Let’s try to execute the script step-by-step.  
**Step #1:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import requests

from bs4 import BeautifulSoup

from tabulate import tabulate

import os

import numpy as np

import matplotlib.pyplot as plt  
  
---  
  
 __

 __

  
**Step #2:**  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

extract_contents= lambda row: [x.text.replace('\n', '') for x
in row]

URL = 'https://www.mohfw.gov.in/'

 

SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed(Including
Foreign Confirmed)','Cured','Death']

 

response = requests.get(URL).content

soup = BeautifulSoup(response, 'html.parser')

header = extract_contents(soup.tr.find_all('th'))

stats = []

all_rows = soup.find_all('tr')

for row in all_rows:

 stat = extract_contents(row.find_all('td'))

 

 if stat:

 if len(stat) == 4:

 # last row

 stat = ['', *stat]

 stats.append(stat)

 elif len(stat) == 5:

 stats.append(stat)

stats[-1][0] = len(stats)

stats[-1][1] = "Total Cases"  
  
---  
  
__

__

