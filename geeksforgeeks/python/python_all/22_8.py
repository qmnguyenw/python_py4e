Python – Extract Particular data type rows



Given A Matrix, extract all the rows which have all the elements with
particular data type.

>  **Input** : test_list = [[4, 5, “Hello”], [2, 6, 7], [“g”, “f”, “g”], [9,
> 10, 11]], data_type = int  
> **Output** : [[2, 6, 7], [9, 10, 11]]  
> **Explanation** : All lists with integer are extracted.
>
>  **Input** : test_list = [[4, 5, “Hello”], [2, 6, 7], [“g”, “f”, “g”], [9,
> 10, 11]], data_type = str  
> **Output** : [[“g”, “f”, “g”]]  
> **Explanation** : All lists with strings are extracted.

**Method #1 : Using isinstance() + all() + list comprehension**

In this, we check for data type using _isinstance(), all()_ checks for all the
elements being of particular data type.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Particular data type rows

# Using isinstance() + all() + list comprehension

 

# initializing list

test_list = [[4, 5, "Hello"], [2, 6, 7],
["g", "f", "g"], [9, 10, 11]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing data type

data_type = int

 

# checking data type using isinstance

res = [row for row in test_list if all(

 isinstance(ele, data_type) for ele in row)]

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, ‘Hello’], [2, 6, 7], [‘g’, ‘f’, ‘g’], [9, 10,
> 11]]  
> Filtered Rows : [[2, 6, 7], [9, 10, 11]]

 **Method #2 : Using filter() + lambda + isinstance()**

In this, we perform task of filtering using _filter()_ and _lambda,
isinstance()_ , is used to perform task of type check as in case of above
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Particular data type rows

# Using filter() + lambda + isinstance()

 

# initializing list

test_list = [[4, 5, "Hello"], [2, 6, 7],
["g", "f", "g"], [9, 10, 11]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing data type

data_type = int

 

# checking data type using isinstance

# filter() used to get filter

res = list(filter(lambda row: all(isinstance(ele,
data_type)

 for ele in row), test_list))

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, ‘Hello’], [2, 6, 7], [‘g’, ‘f’, ‘g’], [9, 10,
> 11]]  
> Filtered Rows : [[2, 6, 7], [9, 10, 11]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

