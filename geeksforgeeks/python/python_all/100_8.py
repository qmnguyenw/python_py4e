Python – Minimum in tuple list value



Many times, while dealing with containers in any language we come across lists
of tuples in different forms, tuples in themselves can have sometimes more
than native datatypes and can have list as their attributes. This article
talks about the minimum of list as tuple attribute. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using list comprehension +min()**  
This particular problem can be solved using list comprehension combined with
the min function in which we use min function to find the minimum of list as a
tuple attribute and list comprehension to iterate through the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum in tuple list value

# using list comprehension + min()

 

# initializing list

test_list = [('key1', [3, 4, 5]), ('key2', [1,
4, 2]), ('key3', [9, 3])]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + min()

# Minimum of list as tuple attribute

res = [(key, min(lst)) for key, lst in test_list]

 

# print result

print("The list tuple attribute minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]
    The list tuple attribute minimum is : [('key1', 3), ('key2', 1), ('key3', 3)]
    

**Method #2 : Using map + lambda + min()**  
The above problem can also be solved using the map function to extend the
logic to the whole list and min function can perform the similar task as the
above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum in tuple list value

# using map() + lambda + min()

 

# initializing list

test_list = [('key1', [3, 4, 5]), ('key2', [1,
4, 2]), ('key3', [9, 3])]

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + lambda + min()

# Minimum in tuple list value

res = list(map(lambda x: (x[0], min(x[1])),
test_list))

 

# print result

print("The list tuple attribute minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]
    The list tuple attribute minimum is : [('key1', 3), ('key2', 1), ('key3', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

