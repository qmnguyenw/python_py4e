Python | Maximum absolute difference list of list



This particular article focuses on a problem that has utility in competitive
as well as day-day programming. Sometimes, we need to get the maximum
difference between the like indices when compared with the next list. The
maximum difference between the like elements in that index is returned. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingmax() + abs() + zip() \+ list comprehension**  
This particular problem can also be solved using the combination of the above
4 operations. Here zip function does the dual task of pairing the list and
also pairing the like indices for difference, to be computed by abs function
and then maximum is found using max function, all bounded by list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum absolute difference list of list

# using max() + abs() + zip() + list comprehension

 

# initializing list 

test_list = [[3, 4, 5], [4, 6, 8], [1, 9,
2], [3, 7, 10]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using max() + abs() + zip() + list comprehension

# Maximum absolute difference list of list

res = [max(abs(i - j) for i, j in zip(*ele))

 for ele in zip(test_list, test_list[1:])]

 

# print result

print("The maximum difference sublist : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 4, 5], [4, 6, 8], [1, 9, 2], [3, 7, 10]]
    The maximum difference sublist : [3, 6, 8]
    

**Method #2 : Usingmax() + map() + abs + zip()**  
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

# Maximum absolute difference list of list

# using max() + map() + abs + zip()

 

# initializing list 

test_list = [[3, 4, 5], [4, 6, 8], [1, 9,
2], [3, 7, 10]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using max() + map() + abs + zip()

# Maximum absolute difference list of list

res = [max(map(abs, (i - j for i, j in zip(x,
y))))

 for x, y in zip(test_list, test_list[1:])]

 

# print result

print("The maximum difference sublist : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 4, 5], [4, 6, 8], [1, 9, 2], [3, 7, 10]]
    The maximum difference sublist : [3, 6, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

