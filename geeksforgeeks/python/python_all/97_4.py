Python | Selective indices Summation



Accessing an element from its index is easier task in python, just using the
[] operator in a list does the trick. But in certain situations we are
presented with tasks when we have more than once indices and we need to get
all the elements corresponding to those indices and then perform the
summation. Lets discuss certain ways to achieve this task.

 **Method #1 : Using List comprehension +sum()**  
This task is easy to perform with a loop, and hence shorthand for it is the
first method to start with this task. Iterating over the index list to get the
corresponding elements from list into new list is brute method to perform this
task. The task of summation is performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Selective indices Summation

# using list comprehension + sum()

 

# initializing lists 

test_list = [9, 4, 5, 8, 10, 14] 

index_list = [1, 3, 4] 

 

# printing original lists 

print ("Original list : " + str(test_list)) 

print ("Original index list : " + str(index_list)) 

 

# using list comprehension + sum() to 

# Selective indices Summation

res_list = sum([test_list[i] for i in index_list]) 

 

# printing result 

print ("Resultant list : " + str(res_list))   
  
---  
  
__

__

**Output :**

    
    
    Original list : [9, 4, 5, 8, 10, 14]
    Original index list : [1, 3, 4]
    Resultant list : 22
    

**Method #2 : Usingmap() + __getitem__ + sum()**  
Yet another method to achieve this particular task is to map one list with
other and get items of indexes and get corresponding matched elements from the
search list. This is quite quick way to perform this task. The task of
summation is performed using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Selective indices Summation

# using map() + __getitem__ + sum()

 

# initializing lists 

test_list = [9, 4, 5, 8, 10, 14] 

index_list = [1, 3, 4] 

 

# printing original lists 

print ("Original list : " + str(test_list)) 

print ("Original index list : " + str(index_list)) 

 

# using map() + __getitem__ + sum() to 

# Selective indices Summation

res_list = sum(list(map(test_list.__getitem__, index_list)))

 

# printing result 

print ("Resultant list : " + str(res_list))   
  
---  
  
__

__

**Output :**

    
    
    Original list : [9, 4, 5, 8, 10, 14]
    Original index list : [1, 3, 4]
    Resultant list : 22
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

