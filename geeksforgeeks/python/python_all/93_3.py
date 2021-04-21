Python | Multiplying Selective Values



Accessing an element from its index is easier task in python, just using the
[] operator in a list does the trick. But in certain situations we are
presented with tasks when we have more than once indices and we need to get
all the elements corresponding to those indices and its product. Lets discuss
certain ways to achieve this task.

 **Method #1 : Using List comprehension + loop**  
This task is easy to perform with a loop, and hence shorthand for it is the
first method to start with this task. Iterating over the index list to get the
corresponding elements from list into new list is brute method to perform this
task. The task of performing product is performed by loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Multiplying Selective Values

# using list comprehension + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing lists

test_list = [9, 4, 5, 8, 10, 14]

index_list = [1, 3, 4]

 

# printing original lists

print ("Original list : " + str(test_list))

print ("Original index list : " + str(index_list))

 

# using list comprehension + loop to 

# Multiplying Selective Values

res_list = [test_list[i] for i in index_list]

res = prod(res_list)

 

# printing result

print ("Resultant product : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [9, 4, 5, 8, 10, 14]
    Original index list : [1, 3, 4]
    Resultant product : 320
    

**Method #2 : Usingmap() + __getitem__ \+ loop**  
Yet another method to achieve this particular task is to map one list with
other and get items of indexes and get corresponding matched elements from the
search list. This is quite quick way to perform this task. The task of
performing product is performed by loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Multiplying Selective Values

# using map() + __getitem__ + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing lists

test_list = [9, 4, 5, 8, 10, 14]

index_list = [1, 3, 4]

 

# printing original lists

print ("Original list : " + str(test_list))

print ("Original index list : " + str(index_list))

 

# using map() + __getitem__ + loop to 

# Multiplying Selective Values

res_list = prod(list(map(test_list.__getitem__, index_list)))

 

# printing result

print ("Resultant product : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [9, 4, 5, 8, 10, 14]
    Original index list : [1, 3, 4]
    Resultant product : 320
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

