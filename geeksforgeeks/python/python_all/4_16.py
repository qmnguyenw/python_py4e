Python Program to check if elements to the left and right of the pivot are
smaller or greater respectively



Given a list and an index, the task is to write a Python program to first
select the element at that index as the pivot element and then test if
elements are greater to its right and smaller to its left or not.

 **Examples:**

>  **Input :** test_list = [4, 3, 5, 6, 9, 16, 11, 10, 12], K = 4
>
>  **Output :** True
>
>  **Explanation :** Elements at Kth index is 9, elements before that are
> smaller and next are greater.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [4, 3, 5, 6, 9, 16, 11, 10, 1], K = 4
>
>  **Output :** False
>
>  **Explanation :** Elements at Kth index is 9, elements before that are
> smaller but 1 is after 4th index, less than 9.

 **Method 1 :** _Using_ _loop_ _and_ _enumerate()_

In this, we iterate through elements using loop and enumerate is used to get
indices and check if index is greater or smaller than K, to toggle testing
condition.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [4, 3, 5, 6, 9, 16, 11, 10,
12]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

res = True

for idx, ele in enumerate(test_list):

 

 # checking for required conditions

 if (idx > K and ele < test_list[K]) or (idx < K and ele >
test_list[K]):

 res = False

 

# printing result

print("Is condition met ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 3, 5, 6, 9, 16, 11, 10, 12]
>
>  
>
>
>  
>
>
> Is condition met ? : True

 **Method 2 :** _Using_ _all()_ _and_ _enumerate()_

Similar task is performed using all(), which can test for required condition
using single line generator expression to provide a more compact solution.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [4, 3, 5, 6, 9, 16, 11, 10,
12]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# all() used to check for condition using one liner

res = all(not ((idx > K and ele < test_list[K]) or (

 idx < K and ele > test_list[K])) for idx, ele in
enumerate(test_list))

 

# printing result

print("Is condition met ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 3, 5, 6, 9, 16, 11, 10, 12]
>
> Is condition met ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

