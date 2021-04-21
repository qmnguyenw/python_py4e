Python – Access element at Kth index in given String



Given a String, access element at Kth index.

>  **Input** : test_str = ‘geeksforgeeks’, K = 4  
>  **Output** : s  
>  **Explanation** : s is 4th element
>
>  **Input** : test_str = ‘geeksforgeeks’, K = 24  
>  **Output** : string index out of range  
>  **Explanation** : Exception as K > string length.

 **Method #1 : Using [] operator**

This is basic way in which this task is performed. In this, we just enclose
Kth index in square brackets. If K can be greater then length of string, its
recommended to enclose in try-except block.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Access element at Kth index in String

# Using [] 

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 7

 

# try-except block for error handling

try :

 

 # access Kth element

 res = test_str[K]

except Exception as e :

 res = str(e)

 

# printing result 

print("Kth index element : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    Kth index element : r
    

**Method #2 : Using Negative index + len() + [] operator**

This is yet another way in which this task can be performed. In this, we
compute length of string and subtract K from it, it results in Kth index from
beginning, and negative indexed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Access element at Kth index in String

# Using Negative index + len() + [] operator

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 7

 

# try-except block for error handling

try :

 

 # access Kth element

 # using negative index

 res = test_str[-(len(test_str) - K)]

except Exception as e :

 res = str(e)

 

# printing result 

print("Kth index element : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    Kth index element : r
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

