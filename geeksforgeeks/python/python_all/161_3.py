Python | Convert list of tuples to list of strings



The interconversion between datatypes is quite useful utility and many
articles have been written to perform the same. This article discusses the
interconversion between a tuple of characters to individual strings. This kind
of interconversion is useful in Machine Learning in which we need to give the
input to train model in a specific format. Let’s discuss certain ways in which
this can be done.

 **Method #1 : Using list comprehension +join()**  
The list comprehension performs the task of iterating the entire list of
tuples and join function performs the task of aggregating the elements of
tuple into a one list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# conversion of list of tuple to list of list 

# using list comprehension + join()

 

# initializing list 

test_list = [('G', 'E', 'E', 'K', 'S'), ('F',
'O', 'R'),

 ('G', 'E', 'E', 'K', 'S')]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using list comprehension + join()

# conversion of list of tuple to list of list 

res = [''.join(i) for i in test_list]

 

# printing result

print ("The list after conversion to list of string : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(‘G’, ‘E’, ‘E’, ‘K’, ‘S’), (‘F’, ‘O’, ‘R’), (‘G’,
> ‘E’, ‘E’, ‘K’, ‘S’)]  
> The list after conversion to list of string : [‘GEEKS’, ‘FOR’, ‘GEEKS’]

  

  

**Method #2 : Usingmap() + join()**  
The task performed by the list comprehension can be performed by the map
function which can perform extension of logic of one tuple to all tuple in
list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# conversion of list of tuple to list of list 

# using map() + join()

 

# initializing list 

test_list = [('G', 'E', 'E', 'K', 'S'), ('F',
'O', 'R'),

 ('G', 'E', 'E', 'K', 'S')]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using map() + join()

# conversion of list of tuple to list of list 

res = list(map(''.join, test_list))

 

# printing result

print ("The list after conversion to list of string : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(‘G’, ‘E’, ‘E’, ‘K’, ‘S’), (‘F’, ‘O’, ‘R’), (‘G’,
> ‘E’, ‘E’, ‘K’, ‘S’)]  
> The list after conversion to list of string : [‘GEEKS’, ‘FOR’, ‘GEEKS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

