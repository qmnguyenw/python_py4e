html.unescape() in python



With the help of **html.unescape()** method, we can convert the ascii string
into html script by replacing ascii characters with special characters by
using html.escape() method.

>  **Syntax :** html.unescape(String)  
>  **Return :** Return a html script.

 **Example #1 :**  
In this example we can see that by using html.unescape() method, we are able
to convert the ascii string into html script by using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# import html

import html

 

s = '<html><head></head><body><h1>This is python</h1></body></html>'

temp = html.escape(s)

# Using html.unescape() method

gfg = html.unescape(temp)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> # This is python

 **Example #2 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import html

import html

 

s = '<html><head></head><body><h1>GeeksForGeeks</h1></body></html>'

temp = html.escape(s)

# Using html.unescape() method

gfg = html.unescape(temp)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> # GeeksForGeeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

