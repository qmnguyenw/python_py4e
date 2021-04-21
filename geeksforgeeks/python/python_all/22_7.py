Python – Distinct Positive Integers Sum to K



Given a sum K then extracts distinct positive numbers that reach the sum.

>  **Input** : K = 17  
> **Output** : [1, 2, 3, 4, 7]  
> **Explanation** : List summation equals 17.
>
>  **Input** : K = 21  
> **Output** : [1, 2, 3, 4, 11]  
> **Explanation** : List summation equals 21.  
>

**Method #1 : Using loop**

In this, we take the smallest possible values that can reach K, for the last
value, we subtract the remaining value from K from summed valued till the
point.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Distinct Positive Integers Sum to K

# Using loop

 

# initializing K

K = 19

 

# printing K

print("The value of K : " + str(K))

 

res = []

idx = 0

for ele in range(1, K):

 idx += ele

 

 # checking for last element point 

 if K - idx < ele + 1:

 

 # appending initial elements

 res.extend(list(range(1, ele)))

 

 # appending last element left

 res.append(K - idx + ele)

 break

 

# printing result 

print("The Required elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The value of K : 19
    The Required elements : [1, 2, 3, 4, 9]
    
    

**Method #2 : Using combinations() + sum()**

In this, we get the elements using combinations(), and check for sum using
summation, this doesn’t perform in greedy but random way to get to the
required summation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Distinct Positive Integers Sum to K

# Using combinations() + sum()

from itertools import combinations

 

# initializing K

K = 19

 

# printing K

print("The value of K : " + str(K))

 

res = []

flag = 0

for idx in range(K - 1, 0, -1):

 

 # forming combinations

 for sub in combinations(range(1, K), idx):

 if sum(sub) == K and flag == 0:

 res.extend(list(sub))

 flag = 1

 break

 else:

 continue

 break

 

# printing result

print("The Required elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The value of K : 19
    The Required elements : [1, 2, 3, 4, 9]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

