Python – Extract K length substrings



There are many problems in which we require to get all K length substrings of
a string. This particular utility is very popular in competitive programming
and having shorthands to solve this problems can always be handy. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension + string slicing**  
The combination of list comprehension and string slicing can be used to
perform this particular task. This is just brute force method to perform this
task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract K length substrings

# Using list comprehension + string slicing

 

# initializing string 

test_str = "Geeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# initializing K 

K = 3

 

# Extract K length substrings

# Using list comprehension + string slicing

res = [test_str[i: j] for i in range(len(test_str)) for
j in range(i + 1, len(test_str) + 1) if
len(test_str[i:j]) == K]

 

# printing result 

print("All K length substrings of string are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks
    All K length substrings of string are : ['Gee', 'eek', 'eks']
    

**Method #2 : Usingitertools.combinations()**  
This particular task can also be performed using the inbuilt function of
combinations, which helps to get all K length the possible combinations i.e
the substrings from a string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract K length substrings

# Using itertools.combinations()

from itertools import combinations

 

# initializing string 

test_str = "Geeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# initializing K 

K = 3

 

# Extract K length substrings

# Using itertools.combinations()

res = [test_str[x:y] for x, y in
combinations(range(len(test_str) + 1), r = 2) if
len(test_str[x:y]) == K ]

 

# printing result 

print("All K length substrings of string are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks
    All K length substrings of string are : ['Gee', 'eek', 'eks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

