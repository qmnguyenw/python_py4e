Python – Test if Kth character is digit in String



Given a String, check if Kth index is a digit.

>  **Input** : test_str = ‘geeks9geeks’, K = 5  
>  **Output** : True  
>  **Explanation** : 5th idx element is 9, a digit, hence True.
>
>  **Input** : test_str = ‘geeks9geeks’, K = 4  
>  **Output** : False  
>  **Explanation** : 4th idx element is s, not a digit, hence False.

 **Method #1 : Using in operator**

In this, we create a string of numerics and then use in operator to check if
Kth digit lies in that numeric string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Kth charater is digit in String

# Using in operator

 

# initializing string

test_str = 'geeks4geeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing K

K = 5

 

# checking if Kth digit is string 

# getting numeric str

num_str = "0123456789"

res = test_str[K] in num_str

 

# printing result 

print("Is Kth element String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks
    Is Kth element String : True
    

**Method #2 : Using isdigit()**

In this, we use inbuilt Py. function to solve this problem, and check if Kth
element is digit.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Kth character is digit in String

# Using isdigit()

 

# initializing string

test_str = 'geeks4geeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing K

K = 5

 

# isdigit checks for digit

res = test_str[K].isdigit()

 

# printing result 

print("Is Kth element String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks
    Is Kth element String : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

