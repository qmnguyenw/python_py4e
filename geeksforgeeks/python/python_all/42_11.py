Python – Replace Consonents by i, Vowels by j



Given a String, perform replacement of all the vowels with i, and all the
consonents using j.

>  **Input** : test_str = ‘geeksforgeeks’, i, j = “A”, “B”  
>  **Output** : BAABBBABBAABB  
>  **Explanation** : All vowels replaced by A and consonents by B.
>
>  **Input** : test_str = ‘gfg’, i, j = “A”, “B”  
>  **Output** : BBB  
>  **Explanation** : Only consonents present and replaced by B.

 **Method #1 : Using sub() + regex**

In this, we use sub function and pass regex for consonents and vowel to
perform appropriate replacement.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Consonents by i, Vowels by j

# Using Using sub() + regex

import re

 

# initializing strings

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing i, j

i, j = "V", "C"

 

# the negation of vowel regex is a consonent, denoted by "^"

res = re.sub("[^aeiouAEIOU]", j, test_str)

res = re.sub("[aeiouAEIOU]", i, res)

 

# printing result 

print("The string after required replacement : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The string after required replacement : CVVCCCVCCVVCC
    

**Method #2 : Using maketrans() + symmetric difference**

In this, we first get consonents using symmetric difference of vowels and
maketrans is function that is used to perform the task of replacement of
Strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Consonents by i, Vowels by j

# Using maketrans() + symmetric difference

import string

 

# initializing strings

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing i, j

i, j = "V", "C"

 

# extracting voweks and consonents

Vows = 'aeiouAEIOU'

 

# using sym. diff to get consonents

Cons = ''.join(set(string.ascii_letters).difference(set(Vows)))

 

# initializing translation

translation = str.maketrans(Vows + Cons, i * len(Vows) +
j * len(Cons))

 

res = test_str.translate(translation)

 

# printing result 

print("The string after required replacement : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The string after required replacement : CVVCCCVCCVVCC
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

