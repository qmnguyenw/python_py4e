Python | Pair summation of list elements



Sometimes, while working with Python list, one can have a problem in which one
needs to find perform the summation of list in pair form. This is useful as a
subproblem solution of bigger problem in web development and day-day
programming. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop**  
This is the brute force method to perform this particular task. In this, we
just iterate the list till last element in skipped manner to get all the pair
sums in other list in an iterative way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Pair summation of list

# Using loop

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Pair summation of list

# Using loop

res = []

for ele in range(0, len(test_list), 2):

 res.append(test_list[ele] + test_list[ele + 1])

 

# Printing result

print("Pair summation of list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10, 17]
    Pair summation of list : [9, 17, 27]
    

**Method #2 : Usingzip() \+ list comprehension**  
This task can also be performed using the combination of above
functionalities. In this, we just iterate the list and the task of combining
pairs is performed by zip(). Works only on Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Pair summation of list

# zip() + list comprehension

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Pair summation of list

# zip() + list comprehension

res = [i + j for i, j in zip(test_list,
test_list[1:])[::2]]

 

# Printing result

print("Pair summation of list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10, 17]
    Pair summation of list : [9, 17, 27]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

