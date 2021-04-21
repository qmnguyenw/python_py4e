Python program to extract rows from Matrix that has distinct data types



Given a Matrix, the task is to write a python program to extract rows with has
no repeated data types.

 **Examples:**

>  **Input :** test_list = [[4, 3, 1], [“gfg”, 3, {4:2}], [3, 1, “jkl”], [9,
> (2, 3)]]
>
>  **Output :** [[‘gfg’, 3, {4: 2}], [9, (2, 3)]]
>
>  **Explanation :** [4, 3, 1] are all integers hence omitted. [9, (2, 3)] has
> integer and tuple, different data types, hence included in results.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [[4, 3, 1], [“gfg”, 3, {4:2}, 4], [3, 1, “jkl”],
> [9, (2, 3)]]
>
>  **Output :** [[9, (2, 3)]]
>
>  **Explanation :** [4, 3, 1] are all integers hence omitted. [9, (2, 3)] has
> integer and tuple, different data types, hence included in results.

 **Method : Using** **type()** **+** **list comprehension**

In this, we use type() to check for data types of each element of rows, and if
the data type repeats, the row is not included in the result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Distinct Data Type Rows

# Using type() + list comprehension

 

# initializing list

test_list = [[4, 3, 1], ["gfg", 3, {4: 2}],
[3, 1, "jkl"], [9, (2, 3)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 # get Distinct types size

 type_size = len(list(set([type(ele) for ele in
sub])))

 

 # if equal get result

 if len(sub) == type_size:

 res.append(sub)

 

# printing result

print("The Distinct data type rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 3, 1], [‘gfg’, 3, {4: 2}], [3, 1, ‘jkl’], [9,
> (2, 3)]]
>
> The Distinct data type rows : [[‘gfg’, 3, {4: 2}], [9, (2, 3)]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

