Python – Extract Percentages from String



Given a String, extract all the numbers that are percentages.

>  **Input** : test_str = ‘geeksforgeeks 20% is 100% way to get 200% success’  
>  **Output** : [‘20%’, ‘100%’, ‘200%’]  
>  **Explanation** : 20%, 100% and 200% are percentages present.
>
>  **Input** : test_str = ‘geeksforgeeks is way to get success’  
>  **Output** : []  
>  **Explanation** : No percentages present.

 **Method #1 : Using findall() + regex**

In this, we employ appropriate regex having “%” symbol in suffix and use
findall() to get all occurrences of such numbers from String.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Percentages from String 

# Using regex + findall()

import re

 

# initializing strings

test_str = 'geeksforgeeks is 100 % way to get 200 % success'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting required result from string 

res = re.findall('\d*%', test_str)

 

# printing result 

print("The percentages : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is 100% way to get 200% success
    The percentages : ['100%', '200%']
    

**Method #2 : Using re.sub() + split()**

In this, we perform split of all words, and then from words that have %, we
remove all non-numeric strings. This can be buggy in cases, we have different
ordering of % and numbers in string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Percentages from String 

# Using re.sub() + split()

import re

 

# initializing strings

test_str = 'geeksforgeeks is 100 % way to get 200 % success'

 

# printing original string

print("The original string is : " + str(test_str))

 

# extracting words

temp = test_str.split()

 

# using 

res = []

for sub in temp:

 if '%' in sub:

 

 # replace empty string to all non-number chars

 res.append(re.sub(r'[^\d, %]', '', sub))

 

 

# printing result 

print("The percentages : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is 100% way to get 200% success
    The percentages : ['100%', '200%']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

