Python | Consecutive Pair Minimums



Sometimes, while working with Python list, one can have a problem in which one
needs to find perform the minimum of list in pair form. This is useful as a
subproblem solution of bigger problem in web development and day-day
programming. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop**  
This is the brute force method to perform this particular task. In this, we
just iterate the list till last element in skipped manner to get all the pair
minimum in other list in iterative way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Pair Minimums

# Using loop

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Consecutive Pair Minimums

# Using loop

res = []

for ele in range(0, len(test_list), 2):

 res.append(min(test_list[ele], test_list[ele + 1]))

 

# Printing result

print("Pair minimum of list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 8, 9, 10, 17]
    Pair minimum of list : [4, 8, 10]
    

**Method #2 : Usingzip() + min() \+ list comprehension**  
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

# Consecutive Pair Minimums

# zip() + list comprehension + min()

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Consecutive Pair Minimums

# zip() + list comprehension + min()

res = [min(i, j) for i, j in zip(test_list,
test_list[1:])[::2]]

 

# Printing result

print("Pair minimum of list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 8, 9, 10, 17]
    Pair minimum of list : [4, 8, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

