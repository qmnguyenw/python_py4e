Python | Modifying tuple contents with list



In Python, tuples are immutable and hence no changes are required in them once
they are formed. This restriction makes their processing harder and hence
certain operations on tuples are quite useful to have knowledge of. This
article deals with modifying the second tuple element with the list given.
Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingzip() \+ list comprehension**  
In this method, we just take the first element of list of tuple and the
element at corresponding index and zip them together using the zip function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# modifying tuple elements

# using zip() + list comprehension

 

# initializing lists

test_list1 = [('Geeks', 1), ('for', 2), ('Geeks',
3)]

test_list2 = [4, 5, 6]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using zip() + list comprehension

# modifying tuple elements

res = [(i[0], j) for i, j in zip(test_list1, test_list2)]

 

# print result

print("The modified resultant list of tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [('Geeks', 1), ('for', 2), ('Geeks', 3)]
    The original list 2 : [4, 5, 6]
    The modified resultant list of tuple : [('Geeks', 4), ('for', 5), ('Geeks', 6)]
    

**Method #2 : Usingzip() + map() + operator.itemgetter()**  
The itemgetter function here does the task of fetching the constant of two
tuple elements which is then mapped with the corresponding index using the map
function. The zip function is used to extend this logic to the entire list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# modifying tuple elements

# using zip() + map() + operator.itemgetter()

import operator

 

# initializing lists

test_list1 = [('Geeks', 1), ('for', 2), ('Geeks',
3)]

test_list2 = [4, 5, 6]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using zip() + map() + operator.itemgetter()

# modifying tuple elements

temp = map(operator.itemgetter(0), test_list1)

res = list(zip(temp, test_list2))

 

# print result

print("The modified resultant list of tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [('Geeks', 1), ('for', 2), ('Geeks', 3)]
    The original list 2 : [4, 5, 6]
    The modified resultant list of tuple : [('Geeks', 4), ('for', 5), ('Geeks', 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

