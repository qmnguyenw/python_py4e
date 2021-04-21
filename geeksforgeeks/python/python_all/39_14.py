Python – Longest Substring Length of K



Given a String and a character K, find longest substring length of K.

>  **Input** : test_str = ‘abcaaaacbbaa’, K = b  
>  **Output** : 2  
>  **Explanation** : b occurs twice, 2 > 1.
>
>  **Input** : test_str = ‘abcaacccbbaa’, K = c  
>  **Output** : 3  
>  **Explanation** : Maximum times c occurs is 3.

 **Method #1 : Using loop**

This is brute way to solve this problem, in this, when K is encountered,
counter is maintained till other character occurs, and count is noted, the
maximum of these counts is kept and is returned as result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest Substring of K

# Using loop

 

# initializing string

test_str = 'abcaaaacbbaa'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing K 

K = 'a'

 

cnt = 0

res = 0

for idx in range(len(test_str)):

 

 # increment counter on checking

 if test_str[idx] == K:

 cnt += 1

 else:

 cnt = 0

 

 # retaining max

 res = max(res, cnt)

 

# printing result 

print("The Longest Substring Length : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : abcaaaacbbaa
    The Longest Substring Length : 4
    

**Method #2 : Using findall() + max()**

In this, we get all the possible substrings of K using findall() and max() is
used over it to get maximum length with len as key.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest Substring of K

# Using findall() + max()

import re

 

# initializing string

test_str = 'abcaaaacbbaa'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing K 

K = 'a'

 

# getting all substrings

res = re.findall(r'' + K + '+', test_str)

 

# getting maximum of substrings Length

res = len(max(res, key = len))

 

# printing result 

print("The Longest Substring Length : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : abcaaaacbbaa
    The Longest Substring Length : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

