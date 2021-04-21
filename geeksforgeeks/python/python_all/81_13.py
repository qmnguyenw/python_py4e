Python | Extract characters except of K string



Sometimes, while working with Python strings, we can have a problem in which
we require to extract all the elements of string except those which present in
a substring. This is quite common problem and has application in many domains
including those of day-day and competitive programming. Lets discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force approach to this problem. In this we employ not operator
to test for element presence in master string and extract it if the element is
not present in K string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract characters except of K string

# Using loop

 

# initializing strings

test_str1 = "geeksforgeeks is best"

test_str2 = "fes"

 

# printing original strings

print("The original string 1 is : " + test_str1)

print("The original string 2 is : " + test_str2)

 

# Extract characters except of K string

# Using loop

res = []

for ele in test_str1:

 if ele not in test_str2:

 res.append(ele)

res = ''.join(res)

 

# printing result 

print("String after removal of substring elements : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string 1 is : geeksforgeeks is best
    The original string 2 is : fes
    String after removal of substring elements : gkorgk i bt
    

**Method #2 : Using set operations**  
This task can also be performed by including set operations. One can perform a
set difference to get difference of elements. The drawbacks are that order is
not preserved and duplicates are removed.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract characters except of K string

# Using set operations

 

# initializing strings

test_str1 = "geeksforgeeks is best"

test_str2 = "fes"

 

# printing original strings

print("The original string 1 is : " + test_str1)

print("The original string 2 is : " + test_str2)

 

# Extract characters except of K string

# Using set operations

res = ''.join(list(set(test_str1) - set(test_str2)))

 

# printing result 

print("String after removal of substring elements : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string 1 is : geeksforgeeks is best
    The original string 2 is : fes
    String after removal of substring elements : oti krbg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

