Python – Split Dictionary values on size limit of values



Given a dictionary with string values, the task is to write a python program
to split values if the size of string exceeds K.

>  **Input :** {1 : “Geeksforgeeks”, 2 : “best for”, 3 : “all geeks”}, limit =
> 5
>
>  **Output :** {1: ‘Geeks’, 2: ‘forge’, 3: ‘eks’, 4: ‘best ‘, 5: ‘for’, 6:
> ‘all g’, 7: ‘eeks’}
>
>  **Explanation :** All string values are capped till length 5. New value is
> created post size limit.
>
>  **Input :** {1 : “Geeksforgeeks”, 2 : “best for”}, limit = 5
>
>  
>
>
>  
>
>
>  **Output :** {1: ‘Geeks’, 2: ‘forge’, 3: ‘eks’, 4: ‘best ‘, 5: ‘for’}
>
>  **Explanation :** All string values are capped till length 5. New value is
> created post size limit.

 **Method : Using** **dictionary comprehension** **+** **enumerate()** **+**
**list slicing**

In this, we perform the task of getting required value chunks using list
slicing and list comprehension on the iteration of values extracted using
values(). The next step is to reassign keys with new chunked values using list
comprehension and enumerate().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split Dictionary values on size limit

# Using dictionary comprehension + enumerate() + list slicing

 

# initializing dictionary

test_dict = {1: "Geeksforgeeks", 

 2: "best for", 3: 

 "all geeks"}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing limit

limit = 4

 

# cutting chunks of K

chunks = (sub[idx: idx + limit] for sub in
test_dict.values()

 for idx in range(0, len(sub), limit))

 

# re assigning dictionary with chunks

res = {key: val for key, val in enumerate(chunks, 1)}

 

# printing result

print("The extracted values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {1: ‘Geeksforgeeks’, 2: ‘best for’, 3: ‘all
> geeks’}
>
> The extracted values : {1: ‘Geek’, 2: ‘sfor’, 3: ‘geek’, 4: ‘s’, 5: ‘best’,
> 6: ‘ for’, 7: ‘all ‘, 8: ‘geek’, 9: ‘s’}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

