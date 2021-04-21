Python – Replace all occurrences of a substring in a string



Sometimes, while working with Python strings, we can have a problem in which
we need to replace all occurrences of a substring with other.

> Input : test_str = “geeksforgeeks”  
> s1 = “geeks”  
> s2 = “abcd”  
> Output : test_str = “abcdsforabcds”  
> Explanation : We replace all occurrences of s1 with s2 in test_str.
>
> Input : test_str = “geeksforgeeks”  
> s1 = “for”  
> s2 = “abcd”  
> Output : test_str = “geeksabcdgeeks”

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We use maketrans() and translate(). This is inbuild way to perform this task.
This function maintains the table internally and performs the task of
swapping.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swap Binary substring

# Using translate()

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Swap Binary substring

# Using translate()

temp = str.maketrans("geek", "abcd")

test_str = test_str.translate(temp)

 

# printing result 

print("The string after swap : " + str(test_str))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : geeksforgeeks
    The string after swap : accdsforaccds
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

