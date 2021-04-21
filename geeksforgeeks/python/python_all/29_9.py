Python – Add K between case shifts



Given a String, add K when a case shift happens.

>  **Input** : test_str = ‘GeeKSforGeEKs’, K = ‘*’  
> **Output** : G*ee*KS*for*G*e*EK*s  
> **Explanation** : After G, lowercase character e is present, * is inserted
> in between. Same goes for each insertion.
>
>  **Input** : test_str = ‘GeeKS’, K = ‘*’  
> **Output** : G*ee*KS  
> **Explanation** : Inserted at case toggles, as explained.

**Method #1 : Using loop + isupper() + islower()**

In this, we iterate for each element and check at each element if next is of
different case, if yes, K is added in junction.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add K between case shifts

# Using loop + isupper() + islower()

import re

 

# initializing string

test_str = 'GeeKSforGeEKs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = '^'

 

res = ""

for idx in range(0, len(test_str) - 1):

 # checking for case shift

 if test_str[idx].isupper() and test_str[idx + 1].islower()
or test_str[idx].islower() and test_str[idx + 1].isupper():

 res = res + test_str[idx] + K

 else:

 res = res + test_str[idx]

res = res + test_str[-1]

 

# printing result

print("String after alteration : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : GeeKSforGeEKs
    String after alteration : G^ee^KS^for^G^e^EK^s
    
    

**Method #2 : Using list comprehension**

Another way to solve this problem, just provides shorthand to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add K between case shifts

# Using loop + isupper() + islower()

 

# initializing string

test_str = 'GeeKSforGeEKs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = '^'

 

# join() to get result string

res = ''.join([test_str[idx] + K if (test_str[idx].isupper()
and test_str[idx + 1].islower()) or

 (test_str[idx].islower() and test_str[idx + 1].isupper())
else test_str[idx] for idx in range(0, len(test_str)
- 1)])

 

res += test_str[-1]

 

# printing result

print("String after alteration : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : GeeKSforGeEKs
    String after alteration : G^ee^KS^for^G^e^EK^s
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

