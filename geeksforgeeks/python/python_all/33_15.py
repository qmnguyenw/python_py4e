Python program to extract N largest dictionaries keys



Given a dictionary, extract the largest N dictionaries keys in descending
order.

>  **Input** : test_dict = {6 : 2, 8: 9, 3: 9, 10: 8}, N = 3  
> **Output** : [10, 8, 6]  
> **Explanation** : Max. N keys extracted in descending order.
>
>  **Input** : test_dict = {6 : 2, 8: 9, 3: 9, 10: 8}, N = 2  
> **Output** : [10, 8]  
> **Explanation** : Max. N keys extracted in descending order.

**Method #1 : Using sorted() + lambda + reverse**

The combination of the above functions can be used to solve this problem. In
this, we perform sort by keys using sorted() + lambda and reverse is used to
perform reverse sort for getting required ordering.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract top N Dictionaries by Key

# Using sorted() + lambda + reverse

 

# initializing dictionary

test_dict = {6 : 2, 8: 9, 3: 9, 10: 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing N 

N = 4

 

res = []

 

# 0 in lambda used for keys, list sliced till N for top N values

for key, val in sorted(test_dict.items(), key = lambda x:
x[0], reverse = True)[:N]:

 res.append(key)

 

# printing result 

print("Top N keys are: " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {6: 1, 8: 9, 3: 9, 10: 8}
    Top N keys are: [10, 8, 6, 3]
    
    

**Method #2 : Using nlargest() + lambda**

This is yet another way in which this task can be performed. In this, maximum
values are extracted using nlargest(), and lambda function is used to drive
the keys extraction and comparison logic.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract top N Dictionaries by Key

# Using nlargest() + lambda

from heapq import nlargest

 

# initializing dictionary

test_dict = {6 : 2, 8: 9, 3: 9, 6: 1,
10: 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing N 

N = 4

 

res = []

 

# Using nlargest() to get maximum keys 

for key, val in nlargest(N, test_dict.items(), key = lambda ele:
ele[0]):

 res.append(key)

 

# printing result 

print("Top N keys are: " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {6: 1, 8: 9, 3: 9, 10: 8}
    Top N keys are: [10, 8, 6, 3]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

