Python – Reverse Shift characters by K



Given a String, reverse shift each charater according to its alphabetic
position by K, including cyclic shift.

>  **Input** : test_str = ‘bccd’, K = 1  
>  **Output** : abbc  
>  **Explanation** : 1 alphabet before b is ‘a’ and so on.
>
>  **Input** : test_str = ‘bccd’, K = 2  
>  **Output** : zaab  
>  **Explanation** : 2 alphabets before b is ‘z’ (rounded) and so on.

 **Method : Using maketrans() + upper() + list comprehension + translate() +
slicing**

In this, we make translation table to each character to its K shifted version
using maketrans() and slicing. The upper() is used to handle all the upper
case characters, translate() is used to perform translation according to
lookup translation table created by maketrans().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Shift characters by K

# using maketrans() + upper() + list comprehension + translate() + slicing

 

# initializing string

test_str = 'GeeksForGeeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing K 

K = 10

 

alpha_chars = 'abcdefghijklmnopqrstuvwxyz'

 

# converted to uppercase

alpha_chars2 = alpha_chars.upper() 

 

# maketrans used for lowercase translation

lower_trans = str.maketrans(alpha_chars, alpha_chars[ -K:] +
alpha_chars[ : -K])

 

# maketrans used for uppercase translation

upper_trans = str.maketrans(alpha_chars2, alpha_chars2[ -K:] +
alpha_chars2[ : -K])

 

# merge lookups

lower_trans.update(upper_trans)

 

# make translation from lookups

res = test_str.translate(lower_trans)

 

# printing result 

print("The converted String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : GeeksForGeeks
    The converted String : WuuaiVehWuuai
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

