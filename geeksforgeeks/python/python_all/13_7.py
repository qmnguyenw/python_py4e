Python – Convert HTML Characters To Strings



 **Prerequisites:** html module

Given a string with HTML characters, the task is to convert HTML characters to
a string. This can be achieved with the help of html.escape() method(for
Python 3.4 **+** ), we can convert the ASCII string into HTML script by
replacing ASCII characters with special characters by using html.escape()
method.

By this method we can decode the HTML entities into text.

 **Syntax:**

    
    
    html.unescape(String)

We can also use Beautiful Soup which handles entity conversion. In Beautiful
Soup 4, entities get decoded automatically.

  

  

 **Example 1:** Python 3.6+

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import html

import html

 

# Create Text

text = 'Γeeks for Γeeks'

 

# It Converts given text To String

print(html.unescape(text)) 

 

# It Converts given text to HTML Entities 

print(html.escape(text))   
  
---  
  
__

__

**Output:**

> Γeeks for Γeeks
>
> &Gamma;eeks for &Gamma;eeks

 **Example 2:** Python 2.6-3.3

We can use HTMLParser.unescape() from the standard library:

  * For Python 2.6-2.7 it’s in HtmlParser.
  * For Python 3 it’s in html.parser

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#import html

import html

 

try:

 # Python 2.6-2.7

 from HTMLParser import HTMLParser

except ImportError:

 # Python 3

 from html.parser import HTMLParser

 

# for python 3

h = html.parser

print(h.unescape('Γeeks for Γeeks'))   
  
---  
  
__

__

**Output:**

> Γeeks for Γeeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

