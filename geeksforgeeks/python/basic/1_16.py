Opening and Closing Tabs Using Selenium



Selenium is a tool which is used to automate browser instructions. It is
utilitarian for all programs, deals with all significant OS and its contents
are written in different languages i.e Python, Java, C# etc.

In this article, we are using **Python** as the language and **Chrome** as the
WebDriver.

### Installation

Python selenium module can be installed using the below command:

    
    
    pip install selenium

Chrome Driver can be downloaded from Chrome Driver (version == 87.0.4).

## Opening a Tab Using Selenium

In order to open a tab, a web driver is needed. In this, we are using Chrome
Webdriver. After providing the driver path, use **.get(URL)** method to open a
tab.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import module

from selenium import webdriver

 

# Create object

driver = webdriver.Chrome()

 

# Assign URL

url = "https://www.geeksforgeeks.org/"

 

# Fetching the Url

driver.get(url)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210115194409/bandicam-2021-01-15-19-36-34-776.mp4

## Opening a New tab using Selenium

In order to open a new tab, a javascript function to open a tab in a new
window can be used. In order to use the functionality of javascript .
**executescript()** method of selenium can be used. After executing the script
we can switch to the window using **.switch_to_window()** method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

from selenium import webdriver

 

# Create object

driver = webdriver.Chrome()

 

# Assign URL

url = "https://www.geeksforgeeks.org/"

 

# New Url

new_url = "https://www.facebook.com/"

 

# Opening first url

driver.get(url)

 

# Open a new window

driver.execute_script("window.open('');")

 

# Switch to the new window and open new URL

driver.switch_to.window(driver.window_handles[1])

driver.get(new_url)  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210115194412/bandicam-2021-01-15-19-39-16-121.mp4

## Closing the Tab using Selenium:

In order to close the tab, **.close()** method is used.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import module

from selenium import webdriver

 

# Create object

driver = webdriver.Chrome()

 

# Fetching the Url

url = "https://www.geeksforgeeks.org/"

 

# Opening first url

driver.get(url)

 

# Closing the tab

driver.close()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210115194414/bandicam-2021-01-15-19-40-51-839.mp4

## Closing a Tab and switching to a new Tab using Selenium:

In the case of multiple tabs, after closing the tab using **.close()** method
we can switch to the tab which is not closed using **.switch_to_window()**
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import module

from selenium import webdriver

 

# Create object

driver = webdriver.Chrome()

 

# Fetching the Url

url = "https://www.geeksforgeeks.org/"

 

# New Url

new_url = "https://www.facebook.com/"

 

# Opening first url

driver.get(url)

 

# Open a new window

driver.execute_script("window.open('');")

 

# Switch to the new window and open new URL

driver.switch_to.window(driver.window_handles[1])

driver.get(new_url)

 

# Closing new_url tab

driver.close()

 

# Switching to old tab

driver.switch_to.window(driver.window_handles[0])  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20210115194416/bandicam-2021-01-15-19-42-19-582.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

