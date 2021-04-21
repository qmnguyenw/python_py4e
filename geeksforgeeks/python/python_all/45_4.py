Python – Frequency of K in sliced String



Given a String, find frequency of certain character in index range.

>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, i = 3, j = 9, K =
> ‘e’  
>  **Output** : 0  
>  **Explanation** : No occurrence of ‘e’ between 4th [s] and 9th element.[e].
>
>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, i = 0, j = 9, K =
> ‘e’  
>  **Output** : 2  
>  **Explanation** : e present as 2nd and 3rd element.

 **Method #1 : Using slicing and count()**

In this, we perform slicing of required string using slice operation, then
coun() is used to get count of K in that sliced String.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of K in sliced String

# Using slicing + count()

 

# initializing strings

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing i, j

i, j = 3, 20

 

# initializing K 

K = 'e'

 

# slicing String 

slc = test_str[i : j]

 

# using count() to get count of K 

res = slc.count(K)

 

# printing result 

print("The required Frequency : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks
    The required Frequency : 3
    

**Method #2 : Using Counter() + slicing**

In this, we perform the task of getting count using Counter(), and slicing is
used to perform slice of ranges.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of K in sliced String

# Using Counter() + slicing 

from collections import Counter

 

# initializing strings

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing i, j

i, j = 3, 20

 

# initializing K 

K = 'e'

 

# slicing String 

slc = test_str[i : j]

 

# Counter() is used to get count 

res = Counter(slc)[K]

 

# printing result 

print("The required Frequency : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks
    The required Frequency : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

