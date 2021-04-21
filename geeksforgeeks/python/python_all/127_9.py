Python | Check if string matches regex list



Sometimes, while working with Python, we can have a problem we have list of
regex and we need to check a particular string matches any of the available
regex in list. Let’s discuss a way in which this task can be performed.

 **Method : Using join regex + loop +re.match()**  
This task can be performed using combination of above functions. In this, we
create a new regex string by joining all the regex list and then match the
string against it to check for match using match() with any of the element of
regex list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if string matches regex list

# Using join regex + loop + re.match()

import re

 

# initializing list 

test_list = ["gee*", "gf*", "df.*", "re"]

 

# printing list 

print("The original list : " + str(test_list))

 

# initializing test_str 

test_str = "geeksforgeeks"

 

# Check if string matches regex list

# Using join regex + loop + re.match()

temp = '(?:% s)' % '|'.join(test_list)

res = False

if re.match(temp, test_str):

 res = True

 

# Printing result

print("Does string match any of regex in list ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : ['gee*', 'gf*', 'df.*', 're']
    Does string match any of regex in list ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

