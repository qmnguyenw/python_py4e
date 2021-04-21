Python – First K consecutive digits in String



Given a String and number K, extract first K consecutive digits making number.

>  **Input** : test_str = “geeks5geeks43best”, K = 2  
>  **Output** : 43  
>  **Explanation** : 43 is first 2 consecutive digits.
>
>  **Input** : test_str = “geeks5gee2ks439best”, K = 3  
>  **Output** : 439  
>  **Explanation** : 439 is first 3 consecutive digits.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we run a loop
through the list and check if valid N consecutive elements are present for
current digit, if yes, we return those N elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# First K consecutive digits in String

# Using loop

 

# initializing string

test_str = "geeks5geeks43isbest"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 2

 

# using loop to run through characters 

res = ""

for idx in range(len(test_str) - K + 1):

 is_num = True

 

 # check for valid number of consecutives

 for j in range(K):

 is_num = is_num & test_str[idx + j].isdigit()

 

 # extracting numbers 

 if is_num :

 res = ""

 for j in range(K):

 res += test_str[idx + j]

 

# printing result 

print("Required character digits : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks5geeks43isbest
    Required character digits : 43
    

**Method #2 : Using regex()**

This is yet another way in which this task can be performed. In this, we apply
valid regex expression and after processing, the result is returned as
occurrences, the first one is returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# First K consecutive digits in String

# Using regex()

import re

 

# initializing string

test_str = "geeks5geeks43isbest"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 2

 

# using regex() to solve problem

temp = re.search('\d{% s}'% K, test_str)

res = (temp.group(0) if temp else '')

 

# printing result 

print("Required character digits : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks5geeks43isbest
    Required character digits : 43
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

