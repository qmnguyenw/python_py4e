Python | Check for Whitespace in List



Sometimes, we might have a problem in which we need to check if the List of
strings has any of blank spaces. This kind of problem can be in Machine
Learning domain to get specific type of data set. Let’s discuss certain ways
in which this kind of problem can be solved.

 **Method #1 : Using regex + any()**  
This kind of problem can be solved using the regex utility offered by python.
By feeding the appropriate regex string in search(), we can check presence of
space in a string and iterate through entire list using any().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Whitespace in List

# Using regex and any()

import re

 

# initializing list 

test_list = ["Geeks forGeeks", "is", "best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Check for Whitespace in List

# Using regex and any()

res = any(bool(re.search(r"\s", ele)) for ele in
test_list)

 

# printing result 

print("Does any string contain spaces ? " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Geeks forGeeks', 'is', 'best']
    Does any string contain spaces ? True
    

**Method #2 : Usingin operator \+ any()**  
This task can also be performed using in operator. Just required to check for
a space in the string. The verdict returned is true even if a single space is
found in any of string of list and false otherwise.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Whitespace in List

# Using in operator + any()

import re

 

# initializing list 

test_list = ["Geeks forGeeks", "is", "best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Check for Whitespace in List

# Using in operator + any()

res = any('' in ele for ele in test_list)

 

# printing result 

print("Does any string contain spaces ? " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Geeks forGeeks', 'is', 'best']
    Does any string contain spaces ? True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

