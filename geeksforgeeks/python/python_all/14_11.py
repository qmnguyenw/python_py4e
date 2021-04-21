Python – Mean deviation of Elements



Given a list, the task is to write a Python program to compute how deviated
are each of them from its list mean.

**Examples:**

>  **Input** : test_list = [7, 5, 1, 2, 10, 3]  
> **Output** : [2.333333333333333, 0.33333333333333304, 3.666666666666667,
> 2.666666666666667, 5.333333333333333, 1.666666666666667]  
> **Explanation** : Mean is 4.66667, related differences are computed.  
>
>
> **Input** : test_list = [1, 2, 3, 4, 5]  
> **Output** : [2, 1, 0, 1, 2]  
> **Explanation** : Mean is 3, related differences are computed.

**Method #1 : Using loop + mean() + abs()**

  

  

In this, we perform iteration of each element and compute deviation from mean
using abs(), the computation of mean is done using mean().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mean deviation of Elements

# Using loop + mean() + abs()

from statistics import mean

 

# initializing list

test_list = [7, 5, 1, 2, 10, 3]

 

# printing original lists

print("The original list is : " + str(test_list))

 

res = []

 

# getting mean

mean_val = mean(test_list)

 

for ele in test_list:

 

 # getting deviation

 res.append(abs(ele - mean_val))

 

# printing result

print("Mean deviations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [7, 5, 1, 2, 10, 3]  
> Mean deviations : [2.333333333333333, 0.33333333333333304,
> 3.666666666666667, 2.666666666666667, 5.333333333333333, 1.666666666666667]

 **Method #2 : Using list comprehension + mean()**

In this similar functionalities are used as above function, difference being
list comprehension is used as one-liner to solve this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mean deviation of Elements

# Using list comprehension + mean()

from statistics import mean

 

# initializing list

test_list = [7, 5, 1, 2, 10, 3]

 

# printing original lists

print("The original list is : " + str(test_list))

 

res = []

 

# getting mean

mean_val = mean(test_list)

 

# list comprehension used for 1 liner

res = [abs(ele - mean_val) for ele in test_list]

 

# printing result

print("Mean deviations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [7, 5, 1, 2, 10, 3]  
> Mean deviations : [2.333333333333333, 0.33333333333333304,
> 3.666666666666667, 2.666666666666667, 5.333333333333333, 1.666666666666667]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

