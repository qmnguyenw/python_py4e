Python Program to check whether all elements in a string list are numeric



Given a list that contains only string elements the task here is to write a
Python program to check if all of them are numeric or not. If all are numeric
return True otherwise, return False.

>  **Input** : test_list = [“434”, “823”, “98”, “74”]
>
>  **Output :** True
>
>  **Explanation :** All Strings are digits.
>
>  **Input :** test_list = [“434”, “82e”, “98”, “74”]
>
>  
>
>
>  
>
>
>  **Output :** False
>
>  **Explanation :** e is not digit, hence verdict is False.

 **Method 1 :** _Using_ _all()_ _,_ _isdigit()_ _and_ _generator expression_

In this, we check for number from isdigit(). all() is used to check for all
strings to be number, iteration for each string is done using generator
expression.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["434", "823", "98", "74"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking all elements to be numeric using isdigit()

res = all(ele.isdigit() for ele in test_list)

 

# printing result

print("Are all strings digits ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘434’, ‘823’, ’98’, ’74’]
>
> Are all strings digits ? : True
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _all()_ _,_ _isdigit()_ _and_ _map()_

In this, we extend test logic to each string using map(), rather than
generator expression. Rest all the functionalities are performed similar to
above method.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["434", "823", "98", "74"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking all elements to be numeric using isdigit()

# map() to extend to each element

res = all(map(str.isdigit, test_list))

 

# printing result

print("Are all strings digits ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘434’, ‘823’, ’98’, ’74’]
>
> Are all strings digits ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

