Python – String with most unique characters



Sometimes, while working with python strings, we can have a problem in which
we desire to extract particular list which has most number of unique
characters. This kind of problem can have application in competitive
programming and web development domain. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using max() + dictionary comprehension**  
The combination of above functionalities can be used to perform this task. In
this, we firstly collect the frequency of each character using dictionary and
then employ max() to compute the string with most unique characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String with most unique characters

# using max() + dictionary comprehension

 

# Initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeksc']

 

# printing original list

print("The original list is : " + str(test_list))

 

# String with most unique characters

# using max() + dictionary comprehension

temp = {idx : len(set(idx)) for idx in test_list}

res = max(temp, key = temp.get)

 

# printing result 

print ("The string with most unique characters is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeksc']
    The string with most unique characters is : geeksc
    

**Method #2 : Usingmax() \+ key + lambda**  
The combination of above methods can be used to perform this task. In this, we
perform this task in similar way as above, just the difference is instead of
using comprehension we use lambda function to extend logic to each string for
computation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String with most unique characters

# using max() + key + lambda

 

# Initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeksc']

 

# printing original list

print("The original list is : " + str(test_list))

 

# String with most unique characters

# using max() + key + lambda

res = max(test_list, key = lambda sub: len(set(sub)),
default = None)

 

# printing result 

print ("The string with most unique characters is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeksc']
    The string with most unique characters is : geeksc
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

