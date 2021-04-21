Python | Test if string is subset of another



Sometimes, while working with strings, we can have a problem in which we need
to test if a string is a subsequence of another. This can have possible
application in many domains including data science and day-day programming.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using all()**  
This is one of the by which we can solve this problem. In this, we employ
all() to check if all the characters of one string are present in another.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if string is subset of another

# Using all()

 

# initializing strings

test_str1 = "geeksforgeeks"

test_str2 = "gfks"

 

# printing original string

print("The original string is : " + test_str1)

 

# Test if string is subset of another

# Using all()

res = all(ele in test_str1 for ele in test_str2)

 

# printing result 

print("Does string contains all the characters of other list? : " +
str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    Does string contains all the characters of other list? : True
    

**Method #2 : Usingissubset()**  
Using an inbuilt function is one of the ways in which this task can be
performed. In this, we just employ the function and it returns the result
after internal processing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if string is subset of another

# Using issubset()

 

# initializing strings

test_str1 = "geeksforgeeks"

test_str2 = "gfks"

 

# printing original string

print("The original string is : " + test_str1)

 

# Test if string is subset of another

# Using issubset()

res = set(test_str2).issubset(test_str1)

 

# printing result 

print("Does string contains all the characters of other list? : " +
str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    Does string contains all the characters of other list? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

