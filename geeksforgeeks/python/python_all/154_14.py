Python | Convert list of tuples to list of list



This is a quite simple problem but can have a good amount of application due
to certain constraints of python language. Because tuples are immutable, they
are not easy to process whereas lists are always a better option while
processing. Let’s discuss certain ways in which we can convert a list of
tuples to list of list.

 **Method #1 : Using list comprehension**  
This can easily be achieved using the list comprehension. We just iterate
through each list converting the tuples to the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# convert list of tuples to list of list

# using list comprehension

 

# initializing list 

test_list = [(1, 2), (3, 4), (5, 6)]

 

# printing original list 

print("The original list of tuples : " + str(test_list))

 

# using list comprehension

# convert list of tuples to list of list

res = [list(ele) for ele in test_list]

 

# print result

print("The converted list of list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list of tuples : [(1, 2), (3, 4), (5, 6)]
    The converted list of list : [[1, 2], [3, 4], [5, 6]]
    

**Method #2 : Usingmap() \+ list**  
We can use the combination of map function and list operator to perform this
particular task. The map function binds each tuple and converts it into list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# convert list of tuples to list of list

# using map() + list

 

# initializing list 

test_list = [(1, 2), (3, 4), (5, 6)]

 

# printing original list 

print("The original list of tuples : " + str(test_list))

 

# using map() + list

# convert list of tuples to list of list

res = list(map(list, test_list))

 

# print result

print("The converted list of list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list of tuples : [(1, 2), (3, 4), (5, 6)]
    The converted list of list : [[1, 2], [3, 4], [5, 6]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

