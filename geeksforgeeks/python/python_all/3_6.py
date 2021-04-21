Python Program to get K length groups with given summation



Given a list, our task is to write a Python program to extract all K length
sublists with lead to given summation.

> **Input :** test_list = [6, 3, 12, 7, 4, 11], N = 21, K = 4
>
>  **Output :** [(6, 6, 6, 3), (6, 6, 3, 6), (6, 3, 6, 6), (6, 7, 4, 4), (6,
> 4, 7, 4), (6, 4, 4, 7), (3, 6, 6, 6), (3, 3, 3, 12), (3, 3, 12, 3), (3, 3,
> 4, 11), (3, 3, 11, 4), (3, 12, 3, 3), (3, 7, 7, 4), (3, 7, 4, 7), (3, 4, 3,
> 11), (3, 4, 7, 7), (3, 4, 11, 3), (3, 11, 3, 4), (3, 11, 4, 3), (12, 3, 3,
> 3), (7, 6, 4, 4), (7, 3, 7, 4), (7, 3, 4, 7), (7, 7, 3, 4), (7, 7, 4, 3),
> (7, 4, 6, 4), (7, 4, 3, 7), (7, 4, 7, 3), (7, 4, 4, 6), (4, 6, 7, 4), (4, 6,
> 4, 7), (4, 3, 3, 11), (4, 3, 7, 7), (4, 3, 11, 3), (4, 7, 6, 4), (4, 7, 3,
> 7), (4, 7, 7, 3), (4, 7, 4, 6), (4, 4, 6, 7), (4, 4, 7, 6), (4, 11, 3, 3),
> (11, 3, 3, 4), (11, 3, 4, 3), (11, 4, 3, 3)]
>
>  **Explanation :** All groups of length 4 and sum 21 are printed.
>
>  **Input :** test_list = [6, 3, 12, 7, 4, 11], N = 210, K = 4
>
>  
>
>
>  
>
>
>  **Output :** []
>
>  **Explanation :** Since no 4 size group sum equals 210, no group is printed
> as result.

 **Method : Using** **sum()** **\+ product() +** **loop** ****

In this all possible sublists of length K are computed using product(), sum()
is used to compare the sublist’s sum with the required summation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K length groups with given summation

# Using sum + product()

from itertools import product

 

# initializing list

test_list = [6, 3, 12, 7, 4, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Summation 

N = 21

 

# initializing size 

K = 4

 

# Looping for each product and comparing with required summation

res = []

for sub in product(test_list, repeat = K):

 if sum(sub) == N:

 res.append(sub)

 

# printing result

print("The sublists with of given size and sum : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [6, 3, 12, 7, 4, 11]
>
> The sublists with of given size and sum : [(6, 6, 6, 3), (6, 6, 3, 6), (6,
> 3, 6, 6), (6, 7, 4, 4), (6, 4, 7, 4), (6, 4, 4, 7), (3, 6, 6, 6), (3, 3, 3,
> 12), (3, 3, 12, 3), (3, 3, 4, 11), (3, 3, 11, 4), (3, 12, 3, 3), (3, 7, 7,
> 4), (3, 7, 4, 7), (3, 4, 3, 11), (3, 4, 7, 7), (3, 4, 11, 3), (3, 11, 3, 4),
> (3, 11, 4, 3), (12, 3, 3, 3), (7, 6, 4, 4), (7, 3, 7, 4), (7, 3, 4, 7), (7,
> 7, 3, 4), (7, 7, 4, 3), (7, 4, 6, 4), (7, 4, 3, 7), (7, 4, 7, 3), (7, 4, 4,
> 6), (4, 6, 7, 4), (4, 6, 4, 7), (4, 3, 3, 11), (4, 3, 7, 7), (4, 3, 11, 3),
> (4, 7, 6, 4), (4, 7, 3, 7), (4, 7, 7, 3), (4, 7, 4, 6), (4, 4, 6, 7), (4, 4,
> 7, 6), (4, 11, 3, 3), (11, 3, 3, 4), (11, 3, 4, 3), (11, 4, 3, 3)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

