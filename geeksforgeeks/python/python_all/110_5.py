Python – Maximum value in record list as tuple attribute



Many times, while dealing with containers in any language we come across lists
of tuples in different forms, tuples in themselves can have sometimes more
than native datatypes and can have list as their attributes. This article
talks about the max of list as tuple attribute. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using list comprehension +max()**  
This particular problem can be solved using list comprehension combined with
the max function in which we use max function to find the max of list as a
tuple attribute and list comprehension to iterate through the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Records element list Maximum

# using list comprehension + max()

 

# initializing list

test_list = [('key1', [3, 4, 5]), ('key2', [1,
4, 2]), ('key3', [9, 3])]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + max()

# Records element list Maximum

res = [(key, max(lst)) for key, lst in test_list]

 

# print result

print("The list tuple attribute maximum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]
    The list tuple attribute maximum is : [('key1', 5), ('key2', 4), ('key3', 9)]
    

**Method #2 : Using map + lambda +max()**  
The above problem can also be solved using the map function to extend the
logic to the whole list and max function can perform the similar task as the
above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Records element list Maximum

# using map() + lambda + max()

 

# initializing list

test_list = [('key1', [3, 4, 5]), ('key2', [1,
4, 2]), ('key3', [9, 3])]

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + lambda + max()

# Records element list Maximum

res = list(map(lambda x: (x[0], max(x[1])),
test_list))

 

# print result

print("The list tuple attribute maximum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]
    The list tuple attribute maximum is : [('key1', 5), ('key2', 4), ('key3', 9)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

