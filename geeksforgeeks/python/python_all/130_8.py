Python | Lexicographically smallest string in mixed list



Sometimes, we can also encounter a problem in which we are given a mixed list
and require to find the lexicographically smallest string that occur in list.
This problem can find it’s application day-day programming. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Usingmin() + isinstance() \+ list comprehension**  
This task can be performed using the combination of above functions. In this,
the min() functions performs the task of finding smallest string and
isinstance() is used to check for string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Lexicographically smallest string in mixed list

# Using min() + isinstance() + list comprehension

 

# initializing list

test_list = [1, 2, 4, "GFG", 5, "IS", 7,
"BEST"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Lexicographically smallest string in mixed list

# Using min() + isinstance() + list comprehension

res = min(sub for sub in test_list if isinstance(sub,
str))

 

# printing result 

print("The Lexicographically smallest string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 2, 4, 'GFG', 5, 'IS', 7, 'BEST']
    The Lexicographically smallest string is : BEST
    

**Method #2 : Usingmin() \+ lambda + filter()**  
The combination of above functions can also be used to perform this particular
task. In this we perform the task of list comprehension using filter() and
lambda and min function is used to performed the usual task of finding
smallest string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Lexicographically smallest string in mixed list

# Using min() + lambda + filter()

 

# initializing list

test_list = [1, 2, 4, "GFG", 5, "IS", 7,
"BEST"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Lexicographically smallest string in mixed list

# Using min() + lambda + filter()

res = min(filter(lambda s:isinstance(s, str),
test_list))

 

# printing result 

print("The Lexicographically smallest string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 2, 4, 'GFG', 5, 'IS', 7, 'BEST']
    The Lexicographically smallest string is : BEST
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

