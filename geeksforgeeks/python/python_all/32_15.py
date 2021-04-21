Python program to extract Strings between HTML Tags



Given a String and HTML tag, extract all the strings between the specified
tag.

>  **Input** : ‘<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.’
> , tag = “br”  
> **Output** : [‘Gfg’, ‘Best’, ‘Reading CS’]  
>  **Explanation** : All strings between “br” tag are extracted.
>
>  **Input** : ‘<h1>Gfg</h1> is <h1>Best</h1> I love <h1>Reading CS</h1>’ ,
> tag = “h1”  
> **Output** : [‘Gfg’, ‘Best’, ‘Reading CS’]  
> **Explanation** : All strings between “h1” tag are extracted.  
>

Using **re module** this task can be performed. In this we employ, findall()
function to extract all the strings by matching appropriate regex built using
tag and symbols.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing re module

import re

 

# initializing string

test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from
it.'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing tag

tag = "b"

 

# regex to extract required strings

reg_str = "<" + tag + ">(.*?)</" + tag + ">"

res = re.findall(reg_str, test_str)

 

# printing result

print("The Strings extracted : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original string is : <b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b>
> from it.  
> The Strings extracted : [‘Gfg’, ‘Best’, ‘Reading CS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

