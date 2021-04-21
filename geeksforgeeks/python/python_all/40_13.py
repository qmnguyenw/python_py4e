Python – Get the indices of Uppercase characters in given string



Given a String extract indices of uppercase characters.

>  **Input** : test_str = ‘GeeKsFoRGeeks’  
>  **Output** : [0, 3, 5, 7, 8]  
>  **Explanation** : Returns indices of uppercase characters.
>
>  **Input** : test_str = ‘GFG’  
>  **Output** : [0, 1, 2]  
>  **Explanation** : All are uppercase.

 **Method #1 : Using list comprehension + range() + isupper()**

In this we iterate through the indices till string length, and check for
uppercase character using isupper(), if found, index is recorded.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase Indices

# Using list comprehension + range() + isupper()

 

# initializing string

test_str = 'GeeKsFoRGEEks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Uppercase check using isupper()

res = [idx for idx in range(len(test_str)) if
test_str[idx].isupper()]

 

# printing result 

print("Uppercase elements indices : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : GeeKsFoRGEEks
    Uppercase elements indices : [0, 3, 5, 7, 8, 9, 10]
    

**Method #2 : Using enumerate() + isupper()**

In this, the indices are captured using enumerate(), and isupper() does task
of uppercase check as in above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase Indices

# Using enumerate() + isupper()

 

# initializing string

test_str = 'GeeKsFoRGEEks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Uppercase check using isupper()

# enumerate() gets indices

res = [idx for idx, chr in enumerate(test_str) if
chr.isupper()]

 

# printing result 

print("Uppercase elements indices : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : GeeKsFoRGEEks
    Uppercase elements indices : [0, 3, 5, 7, 8, 9, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

