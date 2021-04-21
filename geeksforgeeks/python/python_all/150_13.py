Python | Removing strings from tuple



Sometimes we can come across the issue in which we receive data in form of
tuple and we just want the numbers from it and wish to erase all the strings
from them. This has a useful utility in Web-Development and Machine Learning
as well. Let’s discuss certain ways in which this particular task can be
achieved.

 **Method #1 : Using list comprehension +type()**

The combination of above 2 functions can be used to solve this particular
problem. The list comprehension does the task of reconstruction of the
modified list and type function helps us to filter the strings.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove string from tuples

# using list comprehension + type()

 

# initializing list

test_list = [('Geeks', 1, 2), ('for', 4,
'Geeks'), (45, 'good')]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + type()

# Remove string from tuples

res = [tuple([j for j in i if type(j) != str])

 for i in test_list]

 

# print result

print("The list after string removal is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('Geeks', 1, 2), ('for', 4, 'Geeks'), (45, 'good')]
    The list after string removal is : [(1, 2), (4, ), (45, )]
    

  

  

**Method #2 : Using list comprehension + isinstance()**

This is almost a similar method to perform this particular task but the change
here is just to use the isinstance function to check for the string data type,
and rest of the formulations remains mostly similar.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove string from tuples

# using list comprehension + isinstance()

 

# initializing list

test_list = [('Geeks', 1, 2), ('for', 4,
'Geeks'), (45, 'good')]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + isinstance()

# Remove string from tuples

res = [tuple(j for j in i if not isinstance(j,
str))

 for i in test_list]

 

# print result

print("The list after string removal is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('Geeks', 1, 2), ('for', 4, 'Geeks'), (45, 'good')]
    The list after string removal is : [(1, 2), (4, ), (45, )]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

