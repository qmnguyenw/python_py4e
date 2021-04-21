Python – Filter float strings from String list



Sometimes, while working with Python list, we can have a problem in which we
need to separate the float values from valid strings. But problem arises when
float values are in form of strings. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop + Exception Handling**  
The combination of above functionalities can be used to perform this task. In
this, we loop through each element and try to convert each string into float
value, if it’s a success, means it’s a float, else it raises a ValueError and
we can get desired string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter float strings from String list

# using loop + Exception Handling

 

# initialize list 

test_list = ['gfg', '45.45', 'is', '87.5', 'best',
'90.34']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Filter float strings from String list

# using loop + Exception Handling

res = []

for ele in test_list:

 try:

 float(ele)

 except ValueError:

 res.append(ele)

 

# printing result

print("String list after filtering floats : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', '45.45', 'is', '87.5', 'best', '90.34']
    String list after filtering floats : ['gfg', 'is', 'best']
    

**Method #2 : Using regex + list comprehension**  
The combination of above functionalities can perform this task. In this, we
perform the task of filtering using regex created and list comprehension is
used to iterate over the list and apply the filter.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter float strings from String list

# using regex + list comprehension

import re

 

# initialize list 

test_list = ['gfg', '45.45', 'is', '87.5', 'best',
'90.34']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Filter float strings from String list

# using regex + list comprehension

temp = re.compile(r'\d+(?:\.\d*)')

res = [ele for ele in test_list if not temp.match(ele)]

 

# printing result

print("String list after filtering floats : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', '45.45', 'is', '87.5', 'best', '90.34']
    String list after filtering floats : ['gfg', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

