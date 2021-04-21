Python – Replace all numbers by K in given String



Given a string containing numbers, replace each number by K.

>  **Input** : test_str = ‘G4G is 4 all No. 1 Geeks’, K = ‘#’  
>  **Output** : G#G is # all No. # Geeks  
>  **Explanation** : All numbers replaced by K.
>
>  **Input** : test_str = ‘G4G is 4 all No. Geeks’, K = ‘#’  
>  **Output** : G#G is # all No. Geeks  
>  **Explanation** : All numbers replaced by K.

 **Method #1 : Using replace() + isdigit()**

In this, we check for numerics using isdigit() and replace() is used to
perform the task of replacing the numbers by K.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace numbers by K in String

# Using replace() + isdigit()

 

# initializing string

test_str = 'G4G is 4 all No. 1 Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = '@'

 

# loop for all characters

for ele in test_str:

 if ele.isdigit():

 test_str = test_str.replace(ele, K)

 

# printing result 

print("The resultant string : " + str(test_str))   
  
---  
  
__

__

**Output**

    
    
    The original string is : G4G is 4 all No. 1 Geeks
    The resultant string : G@G is @ all No. @ Geeks
    

**Method #2 : Using regex() + sub()**

In this, appropriate regex is used to identify digits and sub() is used to
perform replace.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace numbers by K in String

# Using regex() + sub()

import re

 

# initializing string

test_str = 'G4G is 4 all No. 1 Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = '@'

 

# using regex expression to solve problem 

res = re.sub(r'\d', K, test_str)

 

# printing result 

print("The resultant string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : G4G is 4 all No. 1 Geeks
    The resultant string : G@G is @ all No. @ Geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

