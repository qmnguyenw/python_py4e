Python Program to replace elements of a list based on the comparison with a
number



Given a list, the task here is to write a Python program to replace its
elements after comparing them with another number here described using K.

For the example depicted in this article, any number greater than K will be
replaced with the value given in high and any number less than or equal to K
will be replaced with the value given in low.

>  **Input :** test_list = [7, 4, 3, 2, 6, 8, 9, 1], low = 2, high = 9, K = 5
>
>  **Output :** [9, 2, 2, 2, 9, 9, 9, 2]
>
>  **Explanation :** Elements less than K substituted by 2, rest are by 9.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [7, 4, 3, 2, 6, 8, 9, 1], low =2, high = 8, K = 5
>
>  **Output :** [8, 2, 2, 2, 8, 8, 8, 2]
>
>  **Explanation :** Elements less than K substituted by 2, rest are by 8.

 **Method 1 :** _Using_ _loop_

In this, we perform replacements using conditional statements and iteration is
performed using loop.

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

test_list = [7, 4, 3, 2, 6, 8, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# initializing low and high Replacement Replacement

low, high = 2, 9

 

res = []

for ele in test_list:

 

 # conditional tests

 if ele > K:

 res.append(high)

 else:

 res.append(low)

 

# printing result

print("List after replacement ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [7, 4, 3, 2, 6, 8, 9, 1]
>
>  
>
>
>  
>
>
> List after replacement ? : [9, 2, 2, 2, 9, 9, 9, 2]

 **Method 2 :** _Using list comprehension_

Similar to the method above, only difference is this is a one liner solution
and a compact alternative using list comprehension.

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

test_list = [7, 4, 3, 2, 6, 8, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# initializing low and high Replacement Replacement

low, high = 2, 9

 

# list comprehension for shorthand solution

res = [high if ele > K else low for ele in test_list]

 

# printing result

print("List after replacement ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [7, 4, 3, 2, 6, 8, 9, 1]
>
> List after replacement ? : [9, 2, 2, 2, 9, 9, 9, 2]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

