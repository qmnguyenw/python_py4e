Python | Adding K to each element in a list of integers



While working with the Python lists, we can come over a situation in which we
require to add the integer _k_ to each element in the list. We possibly need
to iterate and add _k_ to each element but that would increase the line of
code. Let’s discuss certain shorthands to perform this task.

 **Method #1 : Using List Comprehension**  
List comprehension is just the short way to perform the task we perform using
the naive method. This is mainly useful to save time and also is best among
others when it comes to readability of the code.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# adding K to each element

# using list comprehension

 

# initializing list 

test_list = [4, 5, 6, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# using list comprehension

# adding K to each element

res = [x + K for x in test_list]

 

# printing result 

print ("The list after adding K to each element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list after adding K to each element : [8, 9, 10, 7, 13]
    

**Method #2 : Usingmap() \+ lambda**  
map function can be used to pair each element with the lambda function which
performs the task of adding _K_ to each element in the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# adding K to each element

# using map() + lambda

 

# initializing list 

test_list = [4, 5, 6, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# using map() + lambda

# adding K to each element

res = list(map(lambda x : x + K, test_list))

 

# printing result 

print ("The list after adding K to each element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list after adding K to each element : [8, 9, 10, 7, 13]
    

**Method #3 : Usingmap() + operator.add**  
This is similar to the above function but uses the operator.add to add each
element to other element from the other list of _K_ formed before applying the
map function. It adds the similar index elements of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# adding K to each element

# using map() + operator.add

import operator

 

# initializing list 

test_list = [4, 5, 6, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K list

K_list = [4] * len(test_list)

 

# using map() + operator.add

# adding K to each element

res = list(map(operator.add, test_list, K_list))

 

# printing result 

print ("The list after adding K to each element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list after adding K to each element : [8, 9, 10, 7, 13]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

