get_attribute() element method – Selenium Python



Selenium’s Python Module is built to perform automated testing with Python.
Selenium Python bindings provides a simple API to write functional/acceptance
tests using Selenium WebDriver. To open a webpage using Selenium Python,
checkout – Navigating links using get method – Selenium Python. Just being
able to go to places isn’t terribly useful. What we’d really like to do is to
interact with the pages, or, more specifically, the HTML elements within a
page. There are multiple strategies to find an element using Selenium,
checkout – Locating Strategies

This article revolves around how to use get_attribute method in Selenium.
get_attribute method is used to get attributes of an element, such as
getting href attribute of anchor tag. This method will first try to return
the value of a property with the given name. If a property with that name
doesn’t exist, it returns the value of the attribute with the same name. If
there’s no attribute with that name, None is returned.

 **Syntax –**

    
    
    element.get_attribute("attribute name")

 **Example –**

 __

 __  
 __

 __

 __  
 __  
 __

<a href="https://www.geeksforgeeks.org/" id="link" />  
  
---  
  
 __

 __

To find an element one needs to use one of the locating strategies, For
example,

  

  

    
    
    element = driver.find_element_by_id("link")
    element = driver.find_element_by_xpath("//a[@id='link']")

Also, to find multiple elements, we can use –

    
    
    elements = driver.find_elements_by_id("link")

Now one can get attribute of this field with

    
    
    element.get_attribute('href')

## How to use get_attribute method in Selenium Python ?

Let’s use https://www.geeksforgeeks.org/ to illustrate this method in Selenium
Pythpn . Here we get href attribute of courses tab in navigation bar at
geeksforgeeks.  
 **Program –**

 __

 __  
 __

 __

 __  
 __  
 __

# import webdriver

from selenium import webdriver

 

# create webdriver object

driver = webdriver.Firefox()

 

# enter keyword to search

keyword = "geeksforgeeks"

 

# get geeksforgeeks.org

driver.get("https://www.geeksforgeeks.org/")

 

# get element 

element = driver.find_element_by_link_text("Courses")

 

# get href attribute

print(element.get_attribute('href'))  
  
---  
  
 __

 __

 **Output-**

![click-element-method-Selenium-Python](https://media.geeksforgeeks.org/wp-
content/uploads/20200420010502/click-element-method-Selenium-Python.png)

 **Terminal Output –**  
![get_attribute-element-method-Selenium-
Python](https://media.geeksforgeeks.org/wp-
content/uploads/20200420012257/get_attribute-element-method-Selenium-
Python.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

