Python program to find GSoC organisations that use a Particular Programming
Language



Currently, it’s not possible to sort GSoC participating organizations by the
programming languages they use in their code. This results in students
spending a lot of time going through each organization’s page and manually
sorting through them.

This article introduces a way for students to write their own **Python
script** using the BeautifulSoup4 library. Using this script the students can
find the organization that uses the language they desire to contribute in.

 **You will learn the following through this article:**

  * How to use Requests library to send HTTPS requests to webpages
  * How to use BeautifulSoup4 library in python to parse HTML code
  * Output data in the form of a spreadsheet (eg. MS Excel) using OpenPyXL

#### Installation

The above module does not come pre-installed with Python. To install them type
the below command in the terminal.

    
    
    pip install requests
    pip install beautifulsoup4
    pip install openpyxl

 **Note:** Only beginner level knowledge of Python 3 is required for following
this article. For more information, refer to Python Programming Language

  

  

#### Getting Started

 **Step 1:** Import the required libraries

 __

 __  
 __

 __

 __  
 __  
 __

import requests, bs4, openpyxl  
  
---  
  
 __

 __

 **Step 2:** Create a response object using Requests. We will be using the
Archive page as our source

 __

 __  
 __

 __

 __  
 __  
 __

# Replace "YEAR" by the year you

# want to get data from. Eg. "2018"

url = 'https://summerofcode.withgoogle.com/archive/YEAR/organizations/'

 

# Creating a response object 

# from the given url

res = requests.get(url)

 

# We'll be using the Archive page

# of GSoC's website as our source.

# Checking the url's status

res.raise_for_status()  
  
---  
  
 __

 __

 **Step 3:** Create a BeautifulSoup object

From the Archive page’s source code:

 __

 __  
 __

 __

 __  
 __  
 __

<li class="organization-card__container"

 layout

 flex-xs="100"

 flex-sm="50"

 flex="33"

 aria-label="AerospaceResearch.net">

 ...

 ...

 <div class="organization-card__footer md-padding">

 

 <h4 class="organization-card__name font-
black-54">AerospaceResearch.net</h4>

 

 </div>

 ...

 ...

</li>  
  
---  
  
 __

 __

We can see that the Orgs’s name is in aH4 tag with class name
“organization-card__name font-black-54” .

Using BS4, we can search for this particular tag in the HTML code and store
the text in a list.

 __

 __  
 __

 __

 __  
 __  
 __

# Specify the language you

# want to search for

language = 'python'

 

# BS4 object to store the 

# html text We use res.text 

# to get the html code in text format

soup = bs4.BeautifulSoup(res.text, 'html.parser')

 

# Selecting the specific tag 

# with class name

orgElem = soup.select('h4[class ="organization-card__name font-
black-54"]')

 

 

# Similarly finding the links 

# for each org's gsoc page

orgLink = soup.find_all("a", class_="organization-
card__link")

languageCheck = ['no'] * len(orgElem)

orgURL = ['none'] * len(orgElem)  
  
---  
  
 __

 __

 **Step 4:** Opening each Orgs’s GSoC page and finding the languages used

 __

 __  
 __

 __

 __  
 __  
 __

item= 0

# Loop to go through each organisation

for link in orgLink:

 

 # Gets the anchor tag's hyperlink

 presentLink = link.get('href') 

 

 url2 = 'https://summerofcode.withgoogle.com' + presentLink 

 print(item)

 print(url2)

 orgURL[item] = url2

 res2 = requests.get(url2)

 res2.raise_for_status()

 

 soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')

 tech = soup2.find_all("li",

 class_="organization__tag organization__tag--technology")

 

 # Finding if the org uses 

 # the specified language

 for name in tech:

 

 if language in name.getText():

 languageCheck[item] = 'yes'

 

 item = item + 1  
  
---  
  
 __

 __

 **Step 5:** Writing the list to a spreadsheet

Using the openpyxl library, we first a create a workbook. In this workbook
we open a sheet using wb[‘Sheet’], where we will actually write the data.
Using the cell().value function, we can directly write values to each cell.
Finally we save the workbook using save() function.

 __

 __  
 __

 __

 __  
 __  
 __

wb= openpyxl.Workbook()

sheet = wb['Sheet']

 

for i in range(0, len(orgElem)):

 sheet.cell(row = i + 1, column = 1).value =
orgElem[i].getText()

 sheet.cell(row = i + 1, column = 2).value =
languageCheck[i]

 sheet.cell(row = i + 1, column = 3).value = orgURL[i]

 

wb.save('gsocOrgsList.xlsx')  
  
---  
  
 __

 __

 **Note:** The spreadsheet will be stored in the same directory as the Python
file

#### Troubleshooting

Due to repeated requests to the website, the server may block your IP address
after repeated attempts. Using a VPN will solve this issue.  
If the problem still persists, add the following to your code:

 __

 __  
 __

 __

 __  
 __  
 __

from fake_useragent import UserAgent

 

ua = UserAgent()

header = {

 "User-Agent": ua.random

 }  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

