Python – Extract String till all occurrence of characters from other string



Given a string, the task is to write a Python program to extract till all
characters from other strings are found.

>  **Input :** test_str = “geeksforgeeks is best for all geeks”, check_str =
> “freak”
>
>  **Output :** geeksforgeeks is best for a
>
>  **Explanation :** a is last letter in freak to be present in string. The
> string is printed till first occurrence of a.
>
>  **Input :** test_str = “geeksforgeeks is best for all geeks”, check_str =
> “geeki”
>
>  
>
>
>  
>
>
>  **Output :** geeksforgeeks i
>
>  **Explanation :** i is last letter in freak to be present in string. The
> string is printed till first occurrence of i.

 **Method #1 : Using** **all()** **+** **slicing** **+** **loop**

In this, the substring is constructed till the current index in a loop, then
from the string, all the elements from other strings are checked using all().
If all are present, the substring is returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract String till all occurrence of characters from other string

# Using all() + slicing + loop

 

# initializing string

test_str = "geeksforgeeks is best for all geeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing check string

check_str = "freak"

 

for idx in range(1, len(test_str)):

 temp = test_str[:idx]

 

 # checking for all chars of check_str in substring

 if all([char in temp for char in check_str]):

 res = temp

 break

 

# printing result

print("String till all characters occurred : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks is best for all geeks
    String till all characters occurred : geeksforgeeks is best for a

 **Method #2 : Using** **find()** **+** **max()** **+** **slicing**

In this, each character in the check string is iterated, the index of all are
checked and the maximum of those is recorded. The substring sliced till the
max index is required answer.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract String till all occurrence of characters from other string

# Using find() + max() + slice

 

# initializing string

test_str = "geeksforgeeks is best for all geeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing check string

check_str = "freak"

 

# max() find maximum index of all characters

res = test_str[:max([test_str.find(idx) for idx in
check_str]) + 1]

 

# printing result

print("String till all characters occurred : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks is best for all geeks
    String till all characters occurred : geeksforgeeks is best for a

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

