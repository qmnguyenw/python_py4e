Python | Split strings in list with same prefix in all elements



Sometimes we face a problem in which we have a list of strings and there are
some garbage/unwanted letters at its prefix or suffix or at the specified
position uniformly, i.e this extends to all the strings in the list. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension + list slicing**

This task can be performed using list comprehension and list slicing. List
slicing can be used to remove the unwanted letters and list comprehension can
be used to extend the logic to the entire string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split strings in list

# Using list comprehension + list slicing

 

# initializing list

test_list = ['Rs.25', 'Rs.100', 'Rs.143', 'Rs.12',
'Rs.4010']

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + list slicing

# Split strings in list

res = [sub[3:] for sub in test_list]

 

# print result

print("The list after string slicing : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Rs.25', 'Rs.100', 'Rs.143', 'Rs.12', 'Rs.4010']
    The list after string slicing : ['25', '100', '143', '12', '4010']
    

  

  

**Method #2 : Usingmap() \+ slicing + lambda**

This particular task can be performed using map function as well. The task of
performing the same for each string is handled by lambda function and map
function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split strings in list

# Using map() + slicing + lambda

 

# initializing list

test_list = ['Rs.25', 'Rs.100', 'Rs.143', 'Rs.12',
'Rs.4010']

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + slicing + lambda

# Split strings in list

res = list(map(lambda sub: sub[3:], test_list))

 

# print result

print("The list after string slicing : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Rs.25', 'Rs.100', 'Rs.143', 'Rs.12', 'Rs.4010']
    The list after string slicing : ['25', '100', '143', '12', '4010']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

