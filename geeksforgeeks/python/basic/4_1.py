Python – Extract records if Kth elements not in List



Given list of tuples, task is to extract all the tuples where Kth index
elements are not present in argument list.

>  **Input** : test_list = [(5, 3), (7, 4), (1, 3), (7, 8), (0, 6)], arg_list
> = [6, 8, 8], K = 1
>
>  **Output** : [(5, 3), (7, 4), (1, 3)]
>
>  **Explanation** : All the elements which have either 6 or 8 at 1st index
> are removed.
>
>  **Input** : test_list = [(5, 3), (7, 4)], arg_list = [3, 3, 3, 3], K = 1
>
>  
>
>
>  
>
>
>  **Output** : [(7, 4)]
>
>  **Explanation** : (5, 3) is removed as it has 3 at 1st index.

 **Method #1 : Using set() + loop**

This is one way in which this task can be. In this, we shorten the argument
list using set and then efficiently check for Kth index having any element
from arg. list and append accordingly.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract records if Kth elements not in List

# Using loop

 

# initializing list

test_list = [(5, 3), (7, 4), (1, 3), (7,
8), (0, 6)]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing arg. list

arg_list = [4, 8, 4]

 

# initializing K

K = 1

 

# Using set() to shorten arg list

temp = set(arg_list)

 

# loop to check for elements and append

res = []

for sub in test_list:

 if sub[K] not in arg_list:

 res.append(sub)

 

# printing result

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [(5, 3), (7, 4), (1, 3), (7, 8), (0, 6)]
    Extracted elements : [(5, 3), (1, 3), (0, 6)]
    
    

**Method #2 : Using list comprehension + set()**

This is yet another way in which this task can be performed. In this, we
compile both, task of filtering duplicates using set() and compiling elements
using conditionals inside list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract records if Kth elements not in List

# Using list comprehension + set()

 

# initializing list

test_list = [(5, 3), (7, 4), (1, 3), (7,
8), (0, 6)]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing arg. list

arg_list = [4, 8, 4]

 

# initializing K

K = 1

 

# Compiling set() and conditionals into single comprehension

res = [(key, val) for key, val in test_list if val not
in set(arg_list)]

 

# printing result

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [(5, 3), (7, 4), (1, 3), (7, 8), (0, 6)]
    Extracted elements : [(5, 3), (1, 3), (0, 6)]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

