Python – Retain first N Elements of a String and Replace the Remaining by K



Given a String, retain first N elements and replace rest by K.

>  **Input** : test_str = ‘geeksforgeeks’, N = 5, K = “@”  
> **Output** : geeks@@@@@@@@  
> **Explanation** : First N elements retained and rest replaced by K.
>
>  **Input** : test_str = ‘geeksforgeeks’, N = 5, K = “*”  
> **Output** : geeks********  
> **Explanation** : First N elements retained and rest replaced by K.

 **Method #1 : Using * operator + len() + slicing**

In this, slicing is used to retain N, and then the length of remaining is
extracted by subtracting the total length extracted by len(), from N, and then
repeat K char using * operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain N and Replace remaining by K

# Using * operator + len() + slicing

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing length needed

N = 4

 

# initializing remains char

K = "@"

 

# using len() and * operator to solve problem

res = test_str[:N] + K * (len(test_str) - N)

 

# printing result

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeksforgeeks
    The resultant string : geek@@@@@@@@@
    

**Method #2 : Using ljust() + slicing + len()**

In this, the task of assigning remaining characters is done using ljust,
rather than the * operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain N and Replace remaining by K

# Using ljust() + slicing + len()

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing length needed

N = 4

 

# initializing remains char

K = "@"

 

# ljust assigns K to remaining string

res = test_str[:N].ljust(len(test_str), K)

 

# printing result

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeksforgeeks
    The resultant string : geek@@@@@@@@@
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

