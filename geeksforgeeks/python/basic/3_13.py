Web Scraping Coronavirus Data into MS Excel



 **Prerequisites:** Web Scraping using BeautifulSoap

Coronavirus cases are increasing rapidly worldwide. This article will guide
you on how to web scrape Coronavirus data and into Ms-excel.

##  **What is Web Scrapping?**

If you’ve ever copy and pasted information from a website, you’ve performed
the same function as any web scraper, only on a microscopic, manual scale. Web
scraping, also known as online data mining, is the method of extracting or
scraping data from a website. This knowledge is gathered and then translated
to a medium that is more accessible to the user. It’s either a spreadsheet or
an API.

 **Approach:**

  1. Request for a response from the webpage.
  2. Parse and extract with the help of the _BeautifulsSoup()_ class method and _lxml_ module.
  3. Download and export the data with _pandas_ into Excel.

 **The Data Source:**

  

  

We need a webpage to fetch the coronavirus data. So we will be using the
Worldometer website here. Worldometer’s webpage will look something like this:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911223411/Screenshot13-300x286.png)

data source

## Programmatic Implementation

There are a few libraries you will need, so first, you need to install them.

Go to your command line and install them.

    
    
    pip install requests
    pip install lxml
    pip install bs4
    

Now let’s see what we can do with these libraries.

Below are the steps for Web Scraping Coronavirus Data into Excel:

 **Step 1)** Use the _requests_ library to grab the page.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required module

import requests

 

# Make requests from webpage

result =
requests.get('https://www.worldometers.info/coronavirus/country/india/')  
  
---  
  
 __

 __

The request library that we downloaded goes and gets a response, to get a
request from the webpage, we use requests.get(website URL) method. If the
request is successful, it will be stored as a giant python string. We will be
able to fetch the complete webpage source code when we run result.text. But
the code will not be structured.

  

  

 **Note:** This may fail if you have a firewall blocking _Python/Jupyter._
Sometimes you need to run this twice if it fails the first time.

 **Step 2)** Use _BeautifulSoap()_ method to extract data from websites.

_bs4_ library already has lots of built-in tools and methods to grab
information from a string of this nature (basically an HTML file). It is a
Python library for pulling data out of HTML and XML files. Using
_BeautifulSoup()_ method of _bs4_ module we can create a _soup_ object that
contains all the _ingredients_ of the webpage.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

import bs4

 

# Creating soap object

soup = bs4.BeautifulSoup(result.text,'lxml')  
  
---  
  
 __

 __

Importing _bs4_ is to create a _BeautifulSoup_ object. And we’re going to pass
on two things here, result.text string and _lxml_ as a string as a constructor
argument. _lxml_ goes through this HTML document and then figures out
different CSS _classes_ , _ids_ , HTML elements, and tags, etc.

 **Extracting the data,** to find the element, you need to right-click and hit
inspect on the number of cases. Refer to the attached snapshot below.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911224322/Screenshot17-300x273.png)

inspecting the website

We need to find the right class i.e. _class_= ‘maincounter-number’_ serves our
purpose. Refer to the attached snapshot below.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911224339/Screenshot16-300x139.png)

Finding the right class

The _BeautifulSoup_ object has been created in our Python script and the HTML
data of the website has been scraped off of the page. Next, we need to get the
data that we are interested in, out of the HTML code.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Searching div tags having maincounter-number class

cases = soup.find_all('div' ,class_= 'maincounter-number')  
  
---  
  
 __

 __

 **Input Screenshot (Inspect element):**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911224637/Screenshot18-300x76.png)

There is still a lot of HTML code that we do not want. Our desired data
entries is wrapped in the HTML div element and inside _class_= ‘maincounter-
number’_. We can use this knowledge to further clean up the scraped data.

 **Step 3)** Storing the data

We need to save the scraped data in some form that can be used effectively.
For this project, all the data will be saved in a Python list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# List to store number of cases

data = []

 

# Find the span and get data from it

for i in cases:

 span = i.find('span')

 data.append(span.string)

 

# Dispaly number of cases 

print(data)  
  
---  
  
 __

 __

 **Input Screenshot (inspect element):**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911224638/Screenshot19-300x51.png)

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911224640/Screenshot21-300x56.png)

We will use _span_ to fetch data from _div_. We need the number of cases only,
not the tags. So we will use _span.string_ to get those numbers, and then they
are stored in _data[]._

Now that we have the number of cases, we are ready to export our data into an
Excel file.

 **Step 4)** Processing the data

Our last step is to export the data to Ms-excel, for which we are going to use
the _pandas_ module. To load the _pandas_ module and start working with it,
import the package.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

# Creating dataframe

df = pd.DataFrame({"CoronaData": data})

 

# Naming the coloumns

df.index = ['TotalCases', ' Deaths', 'Recovered']  
  
---  
  
 __

 __

 _DataFrame_ is a 2D labeled data structure, potentially heterogeneous tabular
data structure with labeled axes (rows and columns).

 _df = pd.DataFrame({“CoronaData”: data})_ is used to create a _DataFrame_ and
give it a name and map it to the data list that we created earlier.

Next, we will give column names with _df.index_.

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911225032/Screenshot25-300x173.png)

**Step 5)** Exporting data into Excel

We are ready to export the data into Excel. We will use _df.to_csv()_ method
for this task.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Exporing data into Excel

df.to_csv('Corona_Data.csv')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200911225033/Screenshot26-300x135.png)

Below is the complete program from the above steps:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

import requests

import bs4

import pandas as pd

 

 

 

# Make requests from webpage

url = 'https://www.worldometers.info/coronavirus/country/india/'

result = requests.get(url)

 

 

 

# Creating soap object

soup = bs4.BeautifulSoup(result.text,'lxml')

 

 

 

# Searching div tags having maincounter-number class

cases = soup.find_all('div' ,class_= 'maincounter-number')

 

 

 

# List to store number of cases

data = []

 

# Find the span and get data from it

for i in cases:

 span = i.find('span')

 data.append(span.string)

 

# Dispaly number of cases 

print(data)

 

 

 

# Creating dataframe

df = pd.DataFrame({"CoronaData": data})

 

# Naming the coloumns

df.index = ['TotalCases', ' Deaths', 'Recovered']

 

 

 

# Exporing data into Excel

df.to_csv('Corona_Data.csv')  
  
---  
  
 __

 __

 **Final Result:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200916123608/covid19-300x141.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

