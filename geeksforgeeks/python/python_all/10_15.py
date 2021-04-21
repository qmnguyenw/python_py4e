Python program to remove row with custom list element



Given a matrix, the task here is to write a Python program to remove rows that
have any element from the custom list and then display the result.

 **Examples:**

>  **Input** : test_list = [[5, 3, 1], [7, 8, 9], [1, 10, 22], [12, 18, 21]],
> check_list = [3, 10, 19, 29, 20, 15]  
> **Output** : [[7, 8, 9], [12, 18, 21]]  
> **Explanation** : [5, 3, 1] row has 3 in it in custom list, hence omitted.
>
>  **Input** : test_list = [[5, 3, 1], [7, 8, 19], [1, 10, 22], [12, 18, 20]],
> check_list = [3, 10, 19, 29, 20, 15]  
> **Output** : []  
> **Explanation** : All rows have some element from custom list, hence
> omitted.  
>

**Method 1:** Using any() and list comprehension

  

  

In this, we perform the task of checking for any elements from custom list to
check for rows using any() and list comprehension is used to omit row if any
element from custom list is found in row.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = [[5, 3, 1], [7, 8, 9], [1,
10, 22], [12, 18, 21]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing custom list

check_list = [3, 10, 19, 29, 20, 15]

 

# list comprehension used to omit rows from matrix

# any() checks for any element found from check list

res = [row for row in test_list if not any(el in row
for el in check_list)]

 

# printing result

print("The omitted rows matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[5, 3, 1], [7, 8, 9], [1, 10, 22], [12, 18, 21]]
>
> The omitted rows matrix : [[7, 8, 9], [12, 18, 21]]

 **Method 2 :** Using filter(), lambda and any()

Similar to above method, only difference being filter() and lambda function is
used to perform task of filtering out or omit rows from matrix from result.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = [[5, 3, 1], [7, 8, 9], [1,
10, 22], [12, 18, 21]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing custom list

check_list = [3, 10, 19, 29, 20, 15]

 

# filter() used to perform filtering

# any() checks for any element found from check list

res = list(filter(lambda row: not any(

 el in row for el in check_list), test_list))

 

# printing result

print("The omitted rows matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[5, 3, 1], [7, 8, 9], [1, 10, 22], [12, 18, 21]]
>
> The omitted rows matrix : [[7, 8, 9], [12, 18, 21]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

