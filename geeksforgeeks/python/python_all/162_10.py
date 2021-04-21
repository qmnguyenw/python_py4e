Python | Join tuple elements in a list



Now days, data is something that is backbone of any Machine Learning
technique. The data can come in any form and its sometimes required to be
extracted out to be processed. This article deals with the issue of extracting
information which is present in tuples in list. Let’s discuss certain ways in
which this can be performed.

 **Method #1 : Usingjoin() + list comprehension**  
The join function can be used to join each tuple elements with each other and
list comprehension handles the task of iterating through the tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# joining tuple elements

# using join() + list comprehension

 

# initializing tuple list 

test_list = [('geeks', 'for', 'geeks'),

 ('computer', 'science', 'portal')]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using join() + list comprehension

# joining tuple elements 

res = [' '.join(tups) for tups in test_list]

 

# printing result 

print ("The joined data is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘geeks’, ‘for’, ‘geeks’), (‘computer’, ‘science’,
> ‘portal’)]  
> The joined data is : [‘geeks for geeks’, ‘computer science portal’]

 **Output :**

  

  

  
**Method #2 : Usingmap() + join()**  
The functionality of list comprehension in the above method can also be done
using the map function. This reduces the size of the code increasing its
readability.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# joining tuple elements

# using join() + map()

 

# initializing tuple list 

test_list = [('geeks', 'for', 'geeks'),

 ('computer', 'science', 'portal')]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using join() + map()

# joining tuple elements 

res = list(map(" ".join, test_list))

 

# printing result 

print ("The joined data is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘geeks’, ‘for’, ‘geeks’), (‘computer’, ‘science’,
> ‘portal’)]  
> The joined data is : [‘geeks for geeks’, ‘computer science portal’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

