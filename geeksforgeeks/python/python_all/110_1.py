Python – Consecutive Row summation in Matrix



This particular article focuses on a problem that has utility in competitive
as well as day-day programming. Sometimes, we need to get the sum between the
like indices when compared with the next list. The sum between the like
elements in that index is returned. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Usingsum() + abs() + zip() \+ list comprehension**  
This particular problem can also be solved using the combination of the above
4 operations. Here zip function does the dual task of pairing the list and
also pairing the like indices for sum, to be computed by abs function and then
sum is found using sum function, all bounded by list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Row summation in Matrix

# using sum() + abs() + zip() + list comprehension

 

# initializing list 

test_list = [[3, 4, 5], [4, 6, 8], [1, 9,
2], [3, 7, 10]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using sum() + abs() + zip() + list comprehension

# Consecutive Row summation in Matrix

res = [sum(abs(i + j) for i, j in zip(*ele))
for ele in zip(test_list, test_list[1:])]

 

# print result

print("The row summation sublist : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 4, 5], [4, 6, 8], [1, 9, 2], [3, 7, 10]]
    The row summation sublist : [30, 30, 32]
    

**Method #2 : Using sum() + map() + abs + zip()**  
This task can also be achieved using the combination of above functions, the
addition is map function that performs the task of binding of abs operation to
the whole list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Row summation in Matrix

# using sum() + map() + abs + zip()

 

# initializing list 

test_list = [[3, 4, 5], [4, 6, 8], [1, 9,
2], [3, 7, 10]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using sum() + map() + abs + zip()

# Consecutive Row summation in Matrix

res = [sum(map(abs, (i + j for i, j in zip(x,
y)))) for x, y in zip(test_list, test_list[1:])]

 

# print result

print("The row summation sublist : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 4, 5], [4, 6, 8], [1, 9, 2], [3, 7, 10]]
    The row summation sublist : [30, 30, 32]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

