Python – Join strings by multiple delimiters



Given two strings, the task is to write a python program to join them by every
delimiter from delimiter list.

>  **Input :** test_str1 = ‘Geeksforgeeks’, test_str2 = “Best”, join_list =
> [“+”, “*”, “-“, “$”, “,”, “@”]
>
>  **Output :** [‘Geeksforgeeks+Best’, ‘Geeksforgeeks*Best’, ‘Geeksforgeeks-
> Best’, ‘Geeksforgeeks$Best’, ‘Geeksforgeeks,Best’, ‘Geeksforgeeks@Best’]
>
>  **Explanation :** Elements are concatenated with all desired delimiters.
>
>  **Input :** test_str1 = ‘Geeksforgeeks’, test_str2 = “Best”, join_list =
> [“+”, “*”, “-“, “$”]
>
>  
>
>
>  
>
>
>  **Output :** [‘Geeksforgeeks+Best’, ‘Geeksforgeeks*Best’, ‘Geeksforgeeks-
> Best’, ‘Geeksforgeeks$Best’]
>
>  **Explanation :** Elements are concatenated with all desired delimiters.

 **Method 1 :** _Using_ _list comprehension_

In this, we iterate through all the delimiters from list using loop inside
list comprehension and + operator performs task of concatenation.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing strings

test_str1 = 'Geeksforgeeks'

test_str2 = "Best"

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing join list

join_list = ["+", "*", "-", "$", ",", "@"]

 

# + operator used for concatenations

res = [test_str1 + delim + test_str2 for delim in
join_list]

 

# printing result

print("All delimiters concatenations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string 1 is : Geeksforgeeks
>
> The original string 2 is : Best
>
>  
>
>
>  
>
>
> All delimiters concatenations : [‘Geeksforgeeks+Best’, ‘Geeksforgeeks*Best’,
> ‘Geeksforgeeks-Best’, ‘Geeksforgeeks$Best’, ‘Geeksforgeeks,Best’,
> ‘Geeksforgeeks@Best’]

 **Method 2 :** _Using_ _join()_ _and_ _list comprehension_

Similar to above method, difference being task of joining is performed using
join(), rather than + operator.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing strings

test_str1 = 'Geeksforgeeks'

test_str2 = "Best"

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing join list

join_list = ["+", "*", "-", "$", ",", "@"]

 

# join() operator used for concatenations

res = [delim.join([test_str1, test_str2]) for delim in
join_list]

 

# printing result

print("All delimiters concatenations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string 1 is : Geeksforgeeks
>
> The original string 2 is : Best
>
> All delimiters concatenations : [‘Geeksforgeeks+Best’, ‘Geeksforgeeks*Best’,
> ‘Geeksforgeeks-Best’, ‘Geeksforgeeks$Best’, ‘Geeksforgeeks,Best’,
> ‘Geeksforgeeks@Best’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

