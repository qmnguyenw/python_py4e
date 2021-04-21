Python Program to Extract Rows of a matrix with Even frequency Elements



Given a Matrix, the task is to write a Python program to extract all the rows
which have even frequencies of elements.

 **Examples:**

>  **Input:** [[4, 5, 5, 2], [4, 4, 4, 4, 2, 2], [6, 5, 6, 5], [1, 2, 3, 4]]
>
>  **Output:** [[4, 4, 4, 4, 2, 2], [6, 5, 6, 5]]
>
>  **Explanation:**
>
>  
>
>
>  
>
>
>   * frequency of 4-> 4 which is even
>   * frequency of 2-> 2 which is even
>   * frequency of 6-> 2 which is even
>   * frequency of 5-> 2 which is even
>

 **Method 1 :** _Using_ _list comprehension_ _,_ _Counter()_ _and_ _all()_

In this, count is maintained using Counter(), and all() is used to check if
all frequencies are even, if not, row is not entered in result list.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

# initializing list

test_list = [[4, 5, 5, 2], [4, 4, 4, 4,
2, 2],

 [6, 5, 6, 5], [1, 2, 3, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Counter() gets the required frequency

res = [sub for sub in test_list if all(

 val % 2 == 0 for key, val in
list(dict(Counter(sub)).items()))]

 

# printing result

print("Filtered Matrix ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 5, 2], [4, 4, 4, 4, 2, 2], [6, 5, 6, 5], [1,
> 2, 3, 4]]
>
> Filtered Matrix ? : [[4, 4, 4, 4, 2, 2], [6, 5, 6, 5]]

 **Method 2 :** _Using_ _filter()_ _,_ _Counter()_ _and items()_

Similar to above method, difference being filter() and lambda function is used
for the task of filtering even frequency rows.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

# initializing list

test_list = [[4, 5, 5, 2], [4, 4, 4, 4,
2, 2], 

 [6, 5, 6, 5], [1, 2, 3, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Counter() gets the required frequency

# filter() used to perform filtering

res = list(filter(lambda sub: all(val % 2 == 0
for key,

 val in list(dict(Counter(sub)).items())), test_list))

 

# printing result

print("Filtered Matrix ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 5, 2], [4, 4, 4, 4, 2, 2], [6, 5, 6, 5], [1,
> 2, 3, 4]]
>
> Filtered Matrix ? : [[4, 4, 4, 4, 2, 2], [6, 5, 6, 5]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

