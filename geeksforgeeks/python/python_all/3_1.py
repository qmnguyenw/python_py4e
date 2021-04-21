Python – Remove non-increasing elements



Given a list, our task is to write a Python program to remove all the non-
increasing elements from the list.

>  **Input :** test_list = [5, 3, 4, 5, 7, 3, 9, 10, 3, 10, 12, 13, 3, 16, 1]
>
>  **Output :** [5, 5, 5, 7, 9, 10, 10, 12, 13, 16]
>
>  **Explanation :** 3, 4 are omitted as 5, (greater element) had occurred
> before them. Applies to all other omitted elements.
>
>  **Input :** test_list = [5, 3, 4, 5, 7, 3, 9]
>
>  
>
>
>  
>
>
>  **Output :** [5, 5, 5, 7, 9]
>
>  **Explanation :** 3, 4 are omitted as 5, (greater element) had occurred
> before them. Applies to all other omitted elements.

 **Method #1 : Using** **loop**

In this, the previous element is checked before populating the further list,
if the greater element is found, it’s appended, else it’s dropped using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove non-increasing elements

# Using loop

 

# initializing list

test_list = [5, 3, 4, 5, 7, 3, 9, 10,
3, 10, 12, 13, 3, 16, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = [test_list[0]]

for ele in test_list:

 

 # checking preceeding element to decide for greater element

 if ele >= res[-1]:

 res.append(ele)

 

# printing result

print("The list after removing non-increasing elements : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, 3, 4, 5, 7, 3, 9, 10, 3, 10, 12, 13, 3, 16, 1]
>
> The list after removing non-increasing elements : [5, 5, 5, 7, 9, 10, 10,
> 12, 13, 16]

 **Method #2 : Using** **list comprehension** **+** **max** **+** **zip** **()
+** **accumulate**

In this, maximum elements are zipped till the current element, and then list
comprehension is used to check if a higher element occurs than the current, if
yes it’s added, else the new element is omitted from the result in runtime
iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove non-increasing elements

# Using list comprehension + max + zip() + accumulate

from itertools import accumulate

 

# initializing list

test_list = [5, 3, 4, 5, 7, 3, 9, 10,
3, 10, 12, 13, 3, 16, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for each element with curr maximum computed using zip

res = [idx for idx, ele in zip(test_list, accumulate(test_list,
max)) if idx == ele]

 

# printing result

print("The list after removing non-increasing elements : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, 3, 4, 5, 7, 3, 9, 10, 3, 10, 12, 13, 3, 16, 1]
>
> The list after removing non-increasing elements : [5, 5, 5, 7, 9, 10, 10,
> 12, 13, 16]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

