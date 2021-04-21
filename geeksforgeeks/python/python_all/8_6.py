Python program to Convert Matrix to Dictionary Value List



Given Matrix, the task is to write a Python program to map each column’s
values as customized keys from another list.

>  **Input :** test_list = [[4, 5, 6], [1, 3, 5], [3, 8, 1], [10, 3, 5]],
> map_list = [4, 5, 6]
>
>  **Output :** {4: [4, 1, 3, 10], 5: [5, 3, 8, 3], 6: [6, 5, 1, 5]}
>
>  **Explanation :** 4 is mapped with all the 0th index of lists, 4, 1 ,3, 10.
>
>  **Input :** test_list = [[4, 5, 6], [1, 3, 5], [3, 8, 1]], map_list = [4,
> 5, 6]
>
>  
>
>
>  
>
>
>  **Output :** {4: [4, 1, 3], 5: [5, 3, 8], 6: [6, 5, 1]}
>
>  **Explanation :** 4 is mapped with all the 0th index of lists, 4, 1 ,3.

 **Method 1 : Using** **dictionary comprehension** **+** **zip()**

In this, mapping of columns with custom list index elements is done using
zip(), dictionary comprehension is done to assign extracted keys to mapping
values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to Dictionary Value List

# Using dictionary comprehension + zip()

from collections import defaultdict

 

# initializing list

test_list = [[4, 5, 6], [1, 3, 5], [3, 8,
1], [10, 3, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing map list 

map_list = [4, 5, 6]

 

# mapping column using zip(), dictionary comprehension for key

# converts to list of dictionary

temp = [{key : val for key, 

 val in zip(map_list, idx)} for idx in test_list]

 

# convert to dictionary value list 

res = defaultdict(list) 

{res[key].append(sub[key]) for sub in temp for key in sub}

 

# printing result

print("Converted Dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 6], [1, 3, 5], [3, 8, 1], [10, 3, 5]]
>
> Converted Dictionary : {4: [4, 1, 3, 10], 5: [5, 3, 8, 3], 6: [6, 5, 1, 5]}

 **Method 2 : Using** **dict()** **+** **list comprehension** **+** **zip()**

In this, the task of mapping values to dictionary keys and conversion is done
using dict() and zip() and dictionary comprehension. Rest functionalities are
similar to the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to Dictionary Value List

# Using dict() + list comprehension + zip()

from collections import defaultdict

 

# initializing list

test_list = [[4, 5, 6], [1, 3, 5], [3, 8,
1], [10, 3, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing map list 

map_list = [4, 5, 6]

 

# mapping column using zip() and conversion using using dict()

# converts to list of dictionary

temp = [dict(zip(map_list, sub)) for sub in test_list]

 

# convert to dictionary value list 

res = defaultdict(list) 

{res[key].append(sub[key]) for sub in temp for key in sub}

 

# printing result

print("Converted Dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 6], [1, 3, 5], [3, 8, 1], [10, 3, 5]]
>
> Converted Dictionary : {4: [4, 1, 3, 10], 5: [5, 3, 8, 3], 6: [6, 5, 1, 5]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

