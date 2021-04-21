Python program to find product of given number of consecutive elements



Given a List, the task is to write a python program that can construct a list
with products of consecutive elements for a given number of elements.

>  **Input :** test_list = [5, 6, 2, 1, 7, 5, 3], K = 3
>
>  **Output :** [60, 12, 14, 35, 105]
>
>  **Explanation :** 5 * 6 * 2 = 60, 6 * 2 * 1 = 12.. And so on.
>
>  **Input :** test_list = [5, 6, 2, 1, 7, 5, 3], K = 4
>
>  
>
>
>  
>
>
>  **Output :** [60, 84, 70, 105]
>
>  **Explanation** : 5 * 6 * 2 * 1 = 60, 6 * 2 * 1 * 7 = 84.. And so on.

 **Method 1 :** _Using_ _list slicing_ _and_ _loop_

In this, we perform task of getting K slice using list slicing and task of
getting product is done by an external function call.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# getting product

def prod(sub):

 res = 1

 for ele in sub:

 res = ele * res

 return res

 

 

# initializing lists

test_list = [5, 6, 2, 1, 7, 5, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

res = []

for idx in range(len(test_list) - K + 1):

 

 # getting product using external function

 res.append(prod(test_list[idx: idx + K]))

 

# printing result

print("Computed Products : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, 6, 2, 1, 7, 5, 3]
>
> Computed Products : [60, 12, 14, 35, 105]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _generator_ _,_ _slicing_ _,_ _reduce()_ _and_ _mul
operator_

In this, generator is used to compute and return intermediate result. Task of
getting sliced multiplication is done using inbuilt function reduce(), and mul
operator.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from functools import reduce

from operator import mul

 

# generator function

 

 

def sliced_prod(sub, K):

 for idx in range(len(sub) - K + 1):

 

 # slicing and returning intermediate product

 sliced = sub[idx: idx + K]

 yield reduce(mul, sliced)

 

# generator function

 

 

# initializing lists

test_list = [5, 6, 2, 1, 7, 5, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# calling fnc.

res = list(sliced_prod(test_list, K))

 

# printing result

print("Computed Products : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, 6, 2, 1, 7, 5, 3]
>
> Computed Products : [60, 12, 14, 35, 105]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

