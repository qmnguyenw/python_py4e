Python – Extract range characters from String



Given a String, extract characters only which lie between given letters.

>  **Input** : test_str = ‘geekforgeeks is best’, strt, end = “g”, “s”  
>  **Output** : gkorgksiss  
>  **Explanation** : All characters after g and before s are retained.
>
>  **Input** : test_str = ‘geekforgeeks is best’, strt, end = “g”, “r”  
>  **Output** : gkorgki  
>  **Explanation** : All characters after g and before r are retained.

 **Method #1 : Using list comprehension**

In this, we check for character in range using comparison operation and list
comprehension does task of iteration and creation of new list. Then join() can
be employed to reconvert to string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract range characters from String

# Using list comprehension

 

# initializing string

test_str = 'geekforgeeks is best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing range letters 

strt, end = "f", "s"

 

# join() to get result in string 

res = ''.join([chr for chr in test_str if chr >= strt
and chr <= end])

 

# printing result 

print("Extracted String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks is best
    Extracted String : gkforgksiss
    

**Method #2 : Using filter() + lambda + join()**

Another way to solve this, in this, we perform task of comparision using
lambda, and filter() used lambda function to get required characters.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract range characters from String

# Using filter() + lambda + join()

 

# initializing string

test_str = 'geekforgeeks is best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing range letters 

strt, end = "f", "s"

 

# join() to get result in string 

res = ''.join(list(filter(lambda chr : chr >= strt
and chr <= end, test_str)))

 

# printing result 

print("Extracted String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks is best
    Extracted String : gkforgksiss
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

