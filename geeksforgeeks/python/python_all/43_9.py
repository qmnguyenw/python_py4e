Python – Non-Overlapping occurrences of N Repeated K character



Given a String, compute non-overlapping occurrences of N repeated K character.

>  **Input** : test_str = ‘aaabaaaabbaa’, K = “a”, N = 3  
>  **Output** : 2  
>  **Explanation** : “aaa” occurs twice as non-overlapping run.
>
>  **Input** : test_str = ‘aaabaaaabbbaa’, K = “b”, N = 3  
>  **Output** : 1  
>  **Explanation** : “bbb” occurs once as non-overlapping run.

 **Method #1 : Using sum() + split() [ Works only for bi-string ]**

In this, split, is performed at character other than K, and then each segment
is counted for Occurrences, and frequency summed using sum(). This works for
strings with contain only 2 unique characters.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Non-Overlapping occurrences of N Repeated K character

# Using split() + sum

 

# initializing string

test_str = 'aaabaaaabbaa'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "a"

 

# initializing N 

N = 2

 

# getting split char

spl_char = [ele for ele in test_str if ele != K][0]

 

# getting split list 

temp = test_str.split(spl_char)

 

# getting Non-Overlapping occurrences

res = sum( len(sub) // N for sub in temp)

 

# printing result 

print("The Non-Overlapping occurrences : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : aaabaaaabbaa
    The Non-Overlapping occurrences : 4
    

**Method #2 : Using re.findall()**

This is another way in which this task can be performed. This can handle all
type of strings and using regex() to solve this.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Non-Overlapping occurrences of N Repeated K character

# Using re.findall()

import re

 

# initializing string

test_str = 'aaabaaaabbaa'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "a"

 

# initializing N 

N = 2

 

# getting length using len()

# getting all occ. of substring

res = len(re.findall(K * N, test_str))

 

# printing result 

print("The Non-Overlapping occurrences : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : aaabaaaabbaa
    The Non-Overlapping occurrences : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

