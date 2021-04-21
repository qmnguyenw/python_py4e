Python | Finding strings with given substring in list



The classical problem that can be handled quite easily by Python and has been
also dealt with many times is finding if a string is substring of other. But
sometimes, one wishes to extend this on list of strings, and hence then
requires to traverse the entire container and perform the generic algorithm.

Let’s discuss certain ways to find strings with given substring in list.

 **Method #1 : Usinglist comprehension**  
List comprehension is an elegant way to perform any particular task as it
increases readability in a long run. This task can be performed using naive
method and hence can be reduced to list comprehension as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find strings with substrings 

# using list comprehension 

 

# initializing list 

test_list = ['GeeksforGeeks', 'Geeky', 'Computers',
'Algorithms']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing substring

subs = 'Geek'

 

# using list comprehension 

# to get string with substring 

res = [i for i in test_list if subs in i]

 

# printing result 

print ("All strings with given substring are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
    All strings with given substring are : ['GeeksforGeeks', 'Geeky']
    

  
**Method #2 : Usingfilter() \+ lambda**  
This function can also perform this task of finding the strings with the help
of lambda. It just filters out all the strings matching the particular
substring and then adds it in a new list.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find strings with substrings 

# using filter() + lambda

 

# initializing list 

test_list = ['GeeksforGeeks', 'Geeky', 'Computers',
'Algorithms']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing substring

subs = 'Geek'

 

# using filter() + lambda 

# to get string with substring 

res = list(filter(lambda x: subs in x, test_list))

 

# printing result 

print ("All strings with given substring are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
    All strings with given substring are : ['GeeksforGeeks', 'Geeky']
    

  
**Method #3 : Usingre + search()**  
Regular expressions can be used to perform many task in python. To perform
this particular task also, regular expressions can come handy. It finds all
the matching substring using search() and returns result.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to find strings with substrings 

# using re + search()

import re

 

# initializing list 

test_list = ['GeeksforGeeks', 'Geeky', 'Computers',
'Algorithms']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing substring

subs = 'Geek'

 

# using re + search()

# to get string with substring 

res = [x for x in test_list if re.search(subs, x)]

 

# printing result 

print ("All strings with given substring are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
    All strings with given substring are : ['GeeksforGeeks', 'Geeky']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

