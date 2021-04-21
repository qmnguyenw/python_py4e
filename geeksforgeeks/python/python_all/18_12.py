Python – Extract rows with Complex data types



Given Matrix, extract rows with complex data types.

**Examples:**

>  **Input** : test_list = [[4, 2, 5], [1, [3, 4], 9], [5], [7, (2, 3), 3, 9]]  
> **Output** : [[1, [3, 4], 9], [7, (2, 3), 3, 9]]  
> **Explanation** : Rows have lists and tuples respectively.  
>
>
> **Input** : test_list = [[4, 2, [5]], [1, [3, 4], 9], [5], [7, (2, 3), 3,
> 9]]  
> **Output** : [[4, 2, [5]], [1, [3, 4], 9], [7, (2, 3), 3, 9]]  
> **Explanation** : Rows have lists and tuples respectively.

**Method #1: Using** **list comprehension** **+** **isinstance()** **+**
**any()**

  

  

In this, we check for each element of row to be of dictionary, tuple, set or
list datatype using isinstance(), if any element is found to have that
instance, the row is added in result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract rows with Complex data types

# Using list comprehension + isinstance() + any()

 

# initializing list

test_list = [[4, 2, 5], [1, [3, 4], 9],
[5], [7, (2, 3), 3, 9]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for any of list, set, tuple or

# dictionary as complex structures

res = [row for row in test_list if any(isinstance(ele,
list) or isinstance(ele, tuple)

 or isinstance(ele, dict) or isinstance(ele, set) for
ele in row)]

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 2, 5], [1, [3, 4], 9], [5], [7, (2, 3), 3, 9]]  
> Filtered Rows : [[1, [3, 4], 9], [7, (2, 3), 3, 9]]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ isinstance()**

In this, we perform task of filtering using filter and lambda, checking for
data type is done using isinstance().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract rows with Complex data types

# Using filter() + lambda + isinstance()

 

# initializing list

test_list = [[4, 2, 5], [1, [3, 4], 9],
[5], [7, (2, 3), 3, 9]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for any of list, set, tuple or dictionary as complex structures

res = list(filter(lambda row: any(isinstance(ele,
list) or isinstance(ele, tuple)

 or isinstance(ele, dict) or isinstance(ele, set) for
ele in row), test_list))

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 2, 5], [1, [3, 4], 9], [5], [7, (2, 3), 3, 9]]  
> Filtered Rows : [[1, [3, 4], 9], [7, (2, 3), 3, 9]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

