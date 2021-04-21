Python Program to Find Most common elements set



Given a List of sets, the task is to write a Python program tocompare elements
with argument set, and return one with maximum matching elements.

 **Examples:**

>  **Input :** test_list = [{4, 3, 5, 2}, {8, 4, 7, 2}, {1, 2, 3, 4}, {9, 5,
> 3, 7}], arg_set = {9, 6, 5, 3}
>
>  **Output :** {9, 3, 5, 7}
>
>  **Explanation :** Resultant set has maximum matching elements.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [{4, 3, 5, 2}, {8, 4, 7, 2}, {1, 2, 3, 4}, {9, 5,
> 3, 7}], arg_set = {4, 6, 5, 3}
>
>  **Output :** {2, 3, 4, 5}
>
>  **Explanation :** Resultant set has maximum matching elements.

 **Method 1: Using** **loop** **+** **set.intersection()**

In this, we perform task of getting all the common elements with argument set
using intersection(), and get its length using len(), and maximum length and
set is compared and updated during iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Most common elements set

# Using loop + intersection()

 

# initializing list

test_list = [{4, 3, 5, 2}, {8, 4, 7, 2},

 {1, 2, 3, 4}, {9, 5, 3, 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing arg_set

arg_set = {9, 6, 5, 3}

 

res = set()

max_len = 0

 

for sub in test_list:

 

 # updating max value on occurrence

 if len(sub.intersection(arg_set)) > max_len:

 max_len = len(sub.intersection(arg_set))

 res = sub

 

# printing result

print("Max Set intersection : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [{2, 3, 4, 5}, {8, 2, 4, 7}, {1, 2, 3, 4}, {9, 3, 5, 7}]
    Max Set intersection : {9, 3, 5, 7}

 **Method 2 : Using** **max()** **+** **list comprehension** **+**
**intersection()**

In this, initial step is to check for the lengths of all intersected set
results and get maximum using max(). Next, task of getting set which matches
required length is extracted.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Most common elements set

# Using loop + intersection()

 

# initializing list

test_list = [{4, 3, 5, 2}, {8, 4, 7, 2},

 {1, 2, 3, 4}, {9, 5, 3, 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing arg_set

arg_set = {9, 6, 5, 3}

 

# getting maximum length 

max_len = max(len(sub.intersection(arg_set)) for sub in
test_list)

 

# getting element matching length

res = [sub for sub in test_list if
len(sub.intersection(arg_set)) == max_len][0]

 

# printing result

print("Set intersection : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [{2, 3, 4, 5}, {8, 2, 4, 7}, {1, 2, 3, 4}, {9, 3, 5, 7}]
    Max Set intersection : {9, 3, 5, 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

