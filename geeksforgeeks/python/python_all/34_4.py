Python program to find the occurrence of substring in the string



Given a list of words, extract all the indices where those words occur in the
string.

>  **Input** : test_str = ‘geeksforgeeks is best for geeks and cs’, test_list
> = [“best”, “geeks”]  
> **Output** : [2, 4]  
> **Explanation** : best and geeks occur at 2nd and 4th index respectively.
>
>  **Input** : test_str = ‘geeksforgeeks is best for geeks and cs’, test_list
> = [“best”, “geeks”, “is”]  
> **Output** : [1, 2, 4]  
> **Explanation** : is, best and geeks occur at 1st, 2nd and 4th index
> respectively.  
>

**Method #1 : Using list comprehension + split() + index()**

In this, we perform the task of getting words from sentence using split(), and
then match words from the string list to extracted strings using index().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word occurrence positions in String

# Using list comprehension + split() + index()

 

# initializing string

test_str = 'geeksforgeeks is best for geeks and cs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing list 

test_list = ["best", "geeks", "cs"]

 

# using index() to get indices,

# list comprehension used to offer one liner

res = [test_str.split().index(ele) 

 for ele in test_str.split() if ele in test_list]

 

# printing result 

print("The indices list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeksforgeeks is best for geeks and cs
    The indices list : [2, 4, 6]
    

**Method #2 : Using list comprehension + enumerate() + split()**

This is yet another way in which this task can be performed. In this task of
getting indices is done using enumerate().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word occurrence positions in String

# Using list comprehension + enumerate() + split()

 

# initializing string

test_str = 'geeksforgeeks is best for geeks and cs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing list 

test_list = ["best", "geeks", "cs"]

 

# using enumerate() to get indices,

# list comprehension used to offer one liner

res = [idx for idx, ele in enumerate(test_str.split()) if
ele in test_list]

 

# printing result 

print("The indices list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeksforgeeks is best for geeks and cs
    The indices list : [2, 4, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

