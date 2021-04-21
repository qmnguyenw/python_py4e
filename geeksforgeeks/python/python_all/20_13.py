Python program to equal character frequencies



Given a String, ensure it has equal character frequencies, if not, equate by
adding required characters.

>  **Input** : test_str = ‘geeksforgeeks’  
> **Output** : geeksforgeeksggkkssfffooorrr  
> **Explanation** : Maximum characters are 4 of ‘e’. Other character are
> appended of frequency 4 – (count of chars).
>
>  **Input** : test_str = ‘geksforgeeks’  
> **Output** : geeksforgeeksggksffoorr  
> **Explanation** : Maximum characters are 3 of ‘e’. Other character are
> appended of frequency 3 – (count of chars).  
>

**Method #1 : Using count() + max() + loop**

In this, we get the frequency of maximum occurring character, and then append
each character to match maximum character frequency.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Equal character frequencies

# Using max() + count() + loop

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting maximum frequency character 

max_freq = max([test_str.count(ele) for ele in test_str])

 

# equating frequencies 

res = test_str

for chr in test_str:

 

 # if frequencies don't match max_freq

 if res.count(chr) != max_freq:

 res += chr * (max_freq - test_str.count(chr))

 

# printing result 

print("Equal character frequency String : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : geeksforgeeks
    Equal character frequency String : geeksforgeeksggkkssfffooorrr

 **Method #2 : Using Counter() + loop**

Similar to above, the difference being Counter() is used to get the maximum
element count.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Equal character frequencies

# Using Counter() + loop 

from collections import Counter

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting maximum frequency character 

# using Counter()

freq_dict = Counter(test_str) 

max_freq = test_str.count(max(freq_dict, key = freq_dict.get)) 

 

# equating frequencies 

res = test_str

for chr in test_str:

 

 # if frequencies don't match max_freq

 if res.count(chr) != max_freq:

 res += chr * (max_freq - test_str.count(chr))

 

# printing result 

print("Equal character frequency String : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : geeksforgeeks
    Equal character frequency String : geeksforgeeksggkkssfffooorrr

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

