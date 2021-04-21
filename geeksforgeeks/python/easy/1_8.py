Change the tag’s contents and replace with the given string using
BeautifulSoup



 **Prerequisites:**Beautifulsoup

Beautifulsoup is a Python library used for web scraping. This powerful python
tool can also be used to modify html webpages. This article depicts how
beautifulsoup can be employed to change contents within a tag and replace the
contents to be changed with the given string. For this, replace_with()
function of the module is used.

 **Syntax:**

> replace_with(“string”)

 **Approach:**

  

  

  * Import module
  * Scrap data from webpage
  * Parse the string scraped to html
  * Select tag within which replacement has to be performed
  * Add string in place of the existing one using replace_with() function
  * Print replaced content

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# impoting BeautifulSoup Module

from bs4 import BeautifulSoup

 

markup = '<a href="http://gfg.com/">Geeks for Geeks <i>gfg.com</i></a>'

 

# parsering string to HTML

soup = BeautifulSoup(markup, 'html.parser')

 

# tag to be replaced

old_tag = soup.a

 

# new tag

new_tag = soup.new_tag("p")

 

# input string

new_tag.string = "gfg.in"

 

'''replacing tag

#page_element.replace_with("string") removes a tag or string from the tree,

#and replaces it with the tag or string of your choice.'''

old_tag.i.replace_with(new_tag)

 

print(old_tag)  
  
---  
  
 __

 __

 **Output:**

> <a href=”http://gfg.com/”>Geeks for Geeks <p>gfg.in</p></a>

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

