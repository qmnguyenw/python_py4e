Python | Search in Nth column in list of tuples



Sometimes, while working with Python list, we can have a data set that
consists of tuples and we have a problem in which we need to search the
element in Nth column of list. This has it’s applications in web development
domain. Let’s discuss certain ways in which this task can be performed.

 **Method : Usingenumerate() \+ list comprehension**  
In this technique we use the power of enumerate() to access index and value in
single iteration and then with the help of list comprehension we frame a
conditional statement in which we check for the valid value in given column.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Search in Nth column in list of tuples

# Using enumerate() + list comprehension

 

# initializing list 

test_list = [('gfg', 1, 9), ('is', 5, 10),
(8, 'best', 13)]

 

# printing list 

print("The original list : " + str(test_list))

 

# initializing Nth column

N = 2

 

# initializing num 

ele = 10

 

# Search in Nth column in list of tuples

# Using enumerate() + list comprehension

res = [idx for idx, val in enumerate(test_list) if val[N]
== ele]

 

# Printing result

print("Row of desired element is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [('gfg', 1, 9), ('is', 5, 10), (8, 'best', 13)]
    Row of desired element is : [1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

