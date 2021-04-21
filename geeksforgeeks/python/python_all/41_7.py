Python – Remove K length Duplicates from String



Given a String remove all K length duplicates.

>  **Input** : test_str = ‘geeksforfreeksfo’, K = 3  
>  **Output** : geeksforfree  
>  **Explanation** : eek, eks, ksf, sfo already in string, hence removed.
>
>  **Input** : test_str = ‘geeksforg’, K = 3  
>  **Output** : geeksforg  
>  **Explanation** : No repeated string, nothing removed.

 **Method : Using loop + slicing**

In this, we keep track of all the K length substrs encountered, extracted
using slicing, and check each time for recurrence, if occurred they are
removed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K length Duplicates from String

# Using loop + slicing 

 

# initializing strings

test_str = 'geeksforfreeksfo'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 3

 

memo = set()

res = []

for idx in range(0, len(test_str) - K):

 

 # slicing K length substrings

 sub = test_str[idx : idx + K]

 

 # checking for presence

 if sub not in memo:

 memo.add(sub)

 res.append(sub)

 

res = ''.join(res[ele] for ele in range(0, len(res),
K))

 

# printing result 

print("The modified string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforfreeksfo
    The modified string : geeksforfree
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

