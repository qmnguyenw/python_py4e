Python – All occurrences of Substring from the list of strings



Given a list of strings and a list of substring. The task is to extract all
the occurrences of substring from the list of strings.

 **Examples:**

>  **Input** : test_list = [“gfg is best”, “gfg is good for CS”, “gfg is
> recommended for CS”]
>
> subs_list = [“gfg”, “CS”]
>
> **Output** : [‘gfg is good for CS’, ‘gfg is recommended for CS’]
>
>  
>
>
>  
>
>
> **Explanation** : Result strings have both “gfg” and “CS”.
>
>  **Input** : test_list = [“gfg is best”, “gfg is recommended for CS”]
>
> subs_list = [“gfg”]
>
> **Output** : [“gfg is best”, “gfg is recommended for CS”]
>
> **Explanation** : Result strings have “gfg”.

**Method #1 : Using loop + in operator**

The combination of the above functions can be used to solve this problem. In
this, we run a loop to extract all strings and also all substring in the list.
The in operator is used to check for substring existence.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strings with all Substring Matches

# Using loop + in operator

 

# initializing list

test_list = ["gfg is best", "gfg is good for CS",

 "gfg is recommended for CS"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Substring List 

subs_list = ["gfg", "CS"]

 

res = []

for sub in test_list:

 flag = 0

 for ele in subs_list:

 

 # checking for non existance of 

 # any string 

 if ele not in sub:

 flag = 1

 break

 if flag == 0:

 res.append(sub)

 

# printing result 

print("The extracted values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [‘gfg is best’, ‘gfg is good for CS’, ‘gfg is
> recommended for CS’]  
> The extracted values : [‘gfg is good for CS’, ‘gfg is recommended for CS’]

 **Method #2 : Using all() + list comprehension**

This is a one-liner approach with the help of which we can perform this task.
In this, we check for all values existence using all(), and list comprehension
is used to iteration of all the containers.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strings with all Substring Matches

# Using all() + list comprehension

 

# initializing list

test_list = ["gfg is best", "gfg is good for CS",

 "gfg is recommended for CS"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Substring List 

subs_list = ["gfg", "CS"]

 

# using all() to check for all values

res = [sub for sub in test_list 

 if all((ele in sub) for ele in subs_list)]

 

# printing result 

print("The extracted values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg is best’, ‘gfg is good for CS’, ‘gfg is
> recommended for CS’]  
> The extracted values : [‘gfg is good for CS’, ‘gfg is recommended for CS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

