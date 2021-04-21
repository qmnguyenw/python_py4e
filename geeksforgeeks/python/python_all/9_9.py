Python Program to check whether Characters of all string elements are in
lexical order or not



Given a list with string elements, the task is to write a Python program to
return True if all list elements are sorted. The point of caution here is to
keep in mind we are comparing characters of a string list element with other
characters of the same list element and not string elements with each other.

**Examples:**

>  **Input :** test_list = [“dent”, “flop”, “most”, “cent”]
>
>  **Output :** True
>
>  **Explanation :** All characters are sorted.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [“dent”, “flop”, “mist”, “cent”]
>
>  **Output :** False
>
>  **Explanation :** m > i in mist, hence unordered. So, False is returned.

 **Method 1 :** _Using_ _loop_ _and_ _sorted()_

In this, we iterate for each String and test if all the Strings are ordered
using sorted(), if any string is not sorted/ordered, the result is flagged
off.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["dent", "flop", "most", "cent"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = True

for ele in test_list:

 

 # check for ordered string

 if ele != ''.join(sorted(ele)):

 res = False

 break

 

# printing result

print("Are all strings ordered ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘dent’, ‘flop’, ‘most’, ‘cent’]
>
>  
>
>
>  
>
>
> Are all strings ordered ? : True

 **Method 2 :** _Using_ _all()_ _and_ _sorted()_

In this, loop is avoided and all the strings to be sorted is checked using
all(), which returns True if all the elements return true for certain
condition.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["dent", "flop", "most", "cent"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using all() to check all elements to be sorted

res = all(ele == ''.join(sorted(ele)) for ele in
test_list)

 

# printing result

print("Are all strings ordered ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘dent’, ‘flop’, ‘most’, ‘cent’]
>
> Are all strings ordered ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

