Build a COVID19 Vaccine Tracker Using Python



As we know the world is facing an unprecedented challenge with communities and
economies everywhere affected by the COVID19. So, we are going to do some fun
during this time by tracking their vaccine. Let’s see a simple Python script
to improve for tracking the COVID19 vaccine.

### Modules Needed

  *  **bs4** : Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files. This module does not comes built-in with Python. To install this type the below command in the terminal.

    
    
    pip install bs4

  *  **requests** : Requests allows you to send HTTP/1.1 requests extremely easily. This module also does not comes built-in with Python. To install this type the below command in the terminal.

    
    
    pip install requests

 **Approach:**

  * Extract data form given URL
  * Scrape the data with the help of requests and Beautiful Soup
  * Convert that data into html code.
  * Find the required details and filter them.

 **Let’s see the stepwise execution of the script**

 **Step 1:** Import all dependence

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import requests

from bs4 import BeautifulSoup  
  
---  
  
 __

 __

