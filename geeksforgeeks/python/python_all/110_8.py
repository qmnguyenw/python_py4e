Python | Maximize Column in Records List



Sometimes, we encounter a problem where we deal with a complex type of matrix
column maximization in which we are given a tuple and we need to perform the
maximization of its like elements. This has a good application in Machine
Learning domain. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingzip() \+ list comprehension**  
This problem can be resolved using the list comprehension which could perform
the column maximization logic and zip function is used to bind the elements as
a result and also at the time of vertical maximization.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximize Column in Records List

# using list comprehension + zip()

 

# initializing list 

test_list = [[(1, 4), (2, 3), (5, 2)], [(3,
7), (1, 9), (10, 5)]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + zip()

# Maximize Column in Records List

res = [tuple(max(j) for j in zip(*i)) for i
in zip(*test_list)]

 

# print result

print("The maximization of columns of tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[(1, 4), (2, 3), (5, 2)], [(3, 7), (1, 9), (10, 5)]]
    The maximization of columns of tuple list : [(3, 7), (2, 9), (10, 5)]
    

**Method #2 : Usingzip() + map()**  
The task of binding the column elements can also be performed using the map
function and the zip function performs the task of binding the maximized
tuples. Both logics bound by list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximize Column in Records List

# using zip() + map()

 

# initializing list 

test_list = [[(1, 4), (2, 3), (5, 2)], [(3,
7), (1, 9), (10, 5)]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using zip() + map()

# Maximize Column in Records List

res = [tuple(map(max, zip(*i))) for i in
zip(*test_list)]

 

# print result

print("The maximization of columns of tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[(1, 4), (2, 3), (5, 2)], [(3, 7), (1, 9), (10, 5)]]
    The maximization of columns of tuple list : [(3, 7), (2, 9), (10, 5)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

