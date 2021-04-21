Scraping Amazon Product Information using Beautiful Soup



 **Web scraping** is a data extraction method used to exclusively gather data
from websites. It is widely used for Data mining or collecting valuable
insights from large websites. Web scraping comes in handy for personal use as
well. Python contains an amazing library called **BeautifulSoup** **** to
allow web scraping. We will be using it __ to scrape product information and
save the details in a CSV file.

In this article, Needed the following are prerequisites.

> url.txt: A text file with few urls of amazon product pages to scrape
>
> Element Id: We need Id’s of objects we wish to web scrape, Will cover it
> soon…

Here, our text file looks like.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201109134441/Capture-660x160.PNG)

 **Module needed and installation:**

BeautifulSoup: Our primary module contains a method to access a webpage over
HTTP.

    
    
    pip install bs4
    

lxml: Helper library to process webpages in python language.

    
    
    pip install lxml
    

requests: Makes the process of sending HTTP requests flawless.the output of
the function

    
    
    pip install requests
    

**Approach:**

  * First, we are going to import our required libraries.
  * Then we will take the URL stored in our text file.
  * We will feed the URL to our soup object which will then extract relevant information from the given URL  
based on the element id we provide it and save it to our CSV file.

 **Let’s have a look at the code, We will see what’s happening at each
significant step.**

 **Step 1:** Initializing our program.

  

  

We import our beautifulsoup and requests, Create/Open a CSV file to save our
gathered data. We declared Header and added a user agent. This ensures that
the target website we are going to web scrape doesn’t consider traffic from
our program as spam and finally get blocked by them. There are plenty of user
agents available here.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from bs4 import BeautifulSoup

import requests

 

File = open("out.csv", "a")

 

HEADERS = ({'User-Agent':

 'Mozilla/5.0 (X11; Linux x86_64) 

 AppleWebKit/537.36 (KHTML, like Gecko) 

 Chrome/44.0.2403.157 Safari/537.36',

 'Accept-Language': 'en-US, en;q=0.5'})

 

webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")  
  
---  
  
 __

 __

 **Step 2:** Retrieving element Ids.

We identify elements by seeing the rendered web pages, but one can’t say the
same for our script. To pinpoint our target element, we will grab its element
id and feed it to the script.

Getting the id of an element is pretty simple. Suppose I need the element id
of the products name, All I have to do

  1. Get to the URL and inspect the text
  2. In the console, we grab the text next to id=

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201107001316/getelementbyid.png)

copy the element id

We feed it to soup.find and convert the function’s output into a string. We
remove commas from the string so that it won’t interfere with the CSV try-
except writing format.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

try:

 title = soup.find("span", 

 attrs={"id": 'productTitle'})

 title_value = title.string

 

 title_string = title_value

 .strip().replace(',', '')

 

except AttributeError:

 

 title_string = "NA"

 

 print("product Title = ", title_string)  
  
---  
  
 __

 __

 **Step 3:** Saving current information to a text file

We use our file object and write the string we just captured, and end the
string with a comma “,” to separate its column when it’s interpreted in a CSV
format.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

File.write(f"{title_string},")  
  
---  
  
 __

 __

 **Doing the above 2 steps with all of the attributes we wish to capture from
web**  
 **like Item price, availability etc.**  

**Step 4:** Closing the file.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

File.write(f"{available},\n")

 

# closing the file

File.close()  
  
---  
  
 __

 __

While writing the last bit of information, notice how we add “\n” to change
the line. Not doing so will give us all the required information in one very
long row. We close the file using File.close(). This is necessary, if we do
not do this we might get an error next time we open the file.

 **Step 5:** Calling the function we just created.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

if __name__ == '__main__':

 # openning our url file to access URLs

 file = open("url.txt", "r")

 

 # iterating over the urls

 for links in file.readlines():

 main(links)  
  
---  
  
 __

 __

We open the url.txt in reading mode and iterate over each of its lines until
we reach the last one. Calling the main function on each line.

 **This is how our entire code looks like:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from bs4 import BeautifulSoup

import requests

 

def main(URL):

 # openning our output file in append mode

 File = open("out.csv", "a")

 

 # specifying user agent, You can use other user agents

 # available on the internet

 HEADERS = ({'User-Agent':

 'Mozilla/5.0 (X11; Linux x86_64) 

 AppleWebKit/537.36 (KHTML, like Gecko) 

 Chrome/44.0.2403.157 Safari/537.36',

 'Accept-Language': 'en-US, en;q=0.5'})

 

 # Making the HTTP Request

 webpage = requests.get(URL, headers=HEADERS)

 

 # Creating the Soup Object containing all data

 soup = BeautifulSoup(webpage.content, "lxml")

 

 # retreiving product title

 try:

 # Outer Tag Object

 title = soup.find("span", 

 attrs={"id": 'productTitle'})

 

 # Inner NavigableString Object

 title_value = title.string

 

 # Title as a string value

 title_string = title_value.strip().replace(',', '')

 

 except AttributeError:

 title_string = "NA"

 print("product Title = ", title_string)

 

 # saving the title in the file

 File.write(f"{title_string},")

 

 # retreiving price

 try:

 price = soup.find(

 "span", attrs={'id': 'priceblock_ourprice'})

 .string.strip().replace(',', '')

 # we are omitting unnecessary spaces

 # and commas form our string

 except AttributeError:

 price = "NA"

 print("Products price = ", price)

 

 # saving

 File.write(f"{price},")

 

 # retreiving product rating

 try:

 rating = soup.find("i", attrs={

 'class': 'a-icon a-icon-star a-star-4-5'})

 .string.strip().replace(',', '')

 

 except AttributeError:

 

 try:

 rating = soup.find(

 "span", attrs={'class': 'a-icon-alt'})

 .string.strip().replace(',', '')

 except:

 rating = "NA"

 print("Overall rating = ", rating)

 

 File.write(f"{rating},")

 

 try:

 review_count = soup.find(

 "span", attrs={'id': 'acrCustomerReviewText'})

 .string.strip().replace(',', '')

 

 except AttributeError:

 review_count = "NA"

 print("Total reviews = ", review_count)

 File.write(f"{review_count},")

 

 # print availiblility status

 try:

 available = soup.find("div", attrs={'id':
'availability'})

 available = available.find("span")

 .string.strip().replace(',', '')

 

 except AttributeError:

 available = "NA"

 print("Availability = ", available)

 

 # saving the availibility and closing the line

 File.write(f"{available},\n")

 

 # closing the file

 File.close()

 

 

if __name__ == '__main__':

 # openning our url file to access URLs

 file = open("url.txt", "r")

 

 # iterating over the urls

 for links in file.readlines():

 main(links)  
  
---  
  
 __

 __

 **Output:**

> product Title = Dremel DigiLab 3D40 Flex 3D Printer w/Extra Supplies 30
> Lesson Plans Professional Development Course Flexible Build Plate Automated
> 9-Point Leveling PC & MAC OS Chromebook iPad Compatible  
> Products price = $1699.00  
> Overall rating = 4.1 out of 5 stars  
> Total reviews = 40 ratings  
> Availability = In Stock.  
> product Title = Comgrow Creality Ender 3 Pro 3D Printer with Removable Build
> Surface Plate and UL Certified Power Supply 220x220x250mm  
> Products price = NA  
> Overall rating = 4.6 out of 5 stars  
> Total reviews = 2509 ratings  
> Availability = NA  
> product Title = Dremel Digilab 3D20 3D Printer Idea Builder for Brand New
> Hobbyists and Tinkerers  
> Products price = $679.00  
> Overall rating = 4.5 out of 5 stars  
> Total reviews = 584 ratings  
> Availability = In Stock.  
> product Title = Dremel DigiLab 3D45 Award Winning 3D Printer w/Filament PC &
> MAC OS Chromebook iPad Compatible Network-Friendly Built-in HD Camera Heated
> Build Plate Nylon ECO ABS PETG PLA Print Capability  
> Products price = $1710.81  
> Overall rating = 4.5 out of 5 stars  
> Total reviews = 351 ratings  
> Availability = In Stock.

 **Here’s how our out.csv looks like.**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201109134748/Capture.PNG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

