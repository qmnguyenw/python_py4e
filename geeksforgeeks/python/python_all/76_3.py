Python – Rearrange list by other list order



Sometimes, while working with Python lists, we can have problem in which we
need to perform sorting of lists according to other list ordering. This can
have applications in many domains including day-day programming and school
programming. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using List comprehension**  
This task can be performed using list comprehension. In this, we iterate the
sort order list and simply append if list is present in target list. The
indices are similar as per the sort order list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rearrange list by other list order

# Using list comprehension

 

# initializing lists

test_list1 = [5, 6, 7, 4, 8, 9, 2]

test_list2 = [9, 6, 4]

 

# printing original list

print("The original list 1 is : " + str(test_list1))

 

# printing original list

print("The original list 2 is : " + str(test_list2))

 

# Rearrange list by other list order

# Using list comprehension

res = [ele for ele in test_list1 if ele in test_list2]

 

# printing result 

print("The list after sorting is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list 1 is : [5, 6, 7, 4, 8, 9, 2]
    The original list 2 is : [9, 6, 4]
    The list after sorting is : [6, 4, 9]
    

**Method #2 : Using sorted +index()**  
The combination of above functions can also be used to perform this task. In
this we use sort function with index as key to sort according to other list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rearrange list by other list order

# Using sorted + index()

 

# initializing lists

test_list1 = [5, 6, 7, 4, 8, 9, 2]

test_list2 = [9, 6, 4]

 

# printing original list

print("The original list 1 is : " + str(test_list1))

 

# printing original list

print("The original list 2 is : " + str(test_list2))

 

# Rearrange list by other list order

# Using sorted + index()

res = sorted(test_list2, key = test_list1.index)

 

# printing result 

print("The list after sorting is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list 1 is : [5, 6, 7, 4, 8, 9, 2]
    The original list 2 is : [9, 6, 4]
    The list after sorting is : [6, 4, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

