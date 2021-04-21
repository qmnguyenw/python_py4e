Python program to Flatten Nested List to Tuple List



Given a list of tuples with each tuple wrapped around multiple lists, our task
is to write a Python program to flatten the container to a list of tuples.

>  **Input :** test_list = [[[(4, 6)]], [[[(7, 4)]]], [[[[(10, 3)]]]]]
>
>  **Output :** [(4, 6), (7, 4), (10, 3)]
>
>  **Explanation :** The surrounded lists are omitted around each tuple.
>
>  **Input :** test_list = [[[(4, 6)]], [[[(7, 4)]]]]
>
>  
>
>
>  
>
>
>  **Output :** [(4, 6), (7, 4)]
>
>  **Explanation :** The surrounded lists are omitted around each tuple.

 **Method #1 : Using** **recursion** **+** **isinstance()**

In this, the container wrapping is tested to be list using isinstance(). The
recursion strategy is used to check for repeated flattening of the list till
tuple.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiflatten Tuple List

# Using recursion + isinstance()

 

 

res = []

def remove_lists(test_list):

 for ele in test_list:

 

 # checking for wrapped list

 if isinstance(ele, list):

 remove_lists(ele)

 else:

 res.append(ele)

 return res

 

# initializing list

test_list = [[[(4, 6)]], [[[(7, 4)]]], [[[[(10,
3)]]]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling recursive function

res = remove_lists(test_list)

 

# printing result

print("The Flattened container : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[[(4, 6)]], [[[(7, 4)]]], [[[[(10, 3)]]]]]
>
> The Flattened container : [(4, 6), (7, 4), (10, 3)]

 **Method #2 : Using** **yield** **\+ recursion**

This method performs a similar task using recursion. The generator is used to
process intermediate results using yield keyword.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiflatten Tuple List

# Using yield + recursion

 

def remove_lists(test_list):

 if isinstance(test_list, list):

 

 # return intermediate to recursive function

 for ele in test_list:

 yield from remove_lists(ele)

 else:

 yield test_list

 

# initializing list

test_list = [[[(4, 6)]], [[[(7, 4)]]], [[[[(10,
3)]]]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling recursive function

res = list(remove_lists(test_list))

 

# printing result

print("The Flattened container : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[[(4, 6)]], [[[(7, 4)]]], [[[[(10, 3)]]]]]
>
> The Flattened container : [(4, 6), (7, 4), (10, 3)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

