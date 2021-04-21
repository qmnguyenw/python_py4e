How to Clone webpage Using pywebcopy in Python?



Some times we need a handy web page on your local hard drive. So, here we are
going to write a simple Python script to Scrap a web page. Web scraping used
for extracting data from websites for offline reading, Storage or whatever
reason. Before writing the script we need to know **pywebcopy. pywebcopy** is
available on **PyPi** and is easily installable using **pip.** Type the below
command in the terminal to install this module

    
    
    pip install pywebcopy

 **pywebcopy** Python package for cloning complete webpages and websites to
local storage.

 **Approach:**

  * Import pywebcopy
  * Pass the argument into the **save_webpage(url=”…”,project_folder=”path/download”,kwargs)**
  * Cheak on your given location.

Below is the implementation.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from pywebcopy import save_webpage

 

kwargs = {'project_name': 'site folder'}

 

save_webpage(

 

 # url pf the website

 url='https://www.geeksforgeeks.org/data-structures/linked-list/',

 

 # folder where the copy will be saved

 project_folder='F:/ro/geek',

 **kwargs

)  
  
---  
  
 __

 __

