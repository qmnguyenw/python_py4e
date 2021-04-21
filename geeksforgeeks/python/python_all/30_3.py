Python – Remove all digits before given Number



Given a String, remove all numeric digits before K number.

 **Method #1 : Using split() + enumerate() + index() + list comprehension**

This is one of the ways in which this task can be performed. In this, we
perform task of split() to get all words, getting index of K number using
index() and list comprehension can be used to extract digits only after the K
Number.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove digits before K Number

# Using split() + enumerate() + index() + list comprehension

 

# initializing string

test_str = 'geeksforgeeks 2 6 is 4 geeks 5 and CS8'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 4

 

# get K Number index

idx = test_str.split().index(str(K))

 

# isdigit() used to check for number 

res = [ele for i, ele in enumerate(test_str.split()) if
not (i < idx and ele.isdigit())]

res = ' '.join(res)

 

 

# printing result 

print("String after removing digits before K : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks 2 6 is 4 geeks 5 and CS8
    String after removing digits before K : geeksforgeeks is 4 geeks 5 and CS8
    
    

**Method #2 : Using regex() + index()**

  

  

In this method, regex is used to remove all the elements before the required
index, and then strings are joined pre and post index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove digits before K Number

# Using regex() + index()

import re

 

# initializing string

test_str = 'geeksforgeeks 2 6 is 4 geeks 5 and CS8'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 4

 

# using regex to achieve task 

res = re.sub('[023456789]', '', test_str[0 :
test_str.index(str(K))]) + test_str[test_str.index(str(K)):]

 

# printing result 

print("String after removing digits before K : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks 2 6 is 4 geeks 5 and CS8
    String after removing digits before K : geeksforgeeks   is 4 geeks 5 and CS8
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

