Python – Filter dictionaries by values in Kth Key in list



Given a list of dictionaries, the task is to write a Python program to filter
dictionaries on basis of elements of Kth key in the list.

 **Examples:**

>  **Input :** test_list = [{“Gfg” : 3, “is” : 5, “best” : 10},
>
> {“Gfg” : 5, “is” : 1, “best” : 1},
>
> {“Gfg” : 8, “is” : 3, “best” : 9},
>
>  
>
>
>  
>
>
> {“Gfg” : 9, “is” : 9, “best” : 8},
>
> {“Gfg” : 4, “is” : 10, “best” : 7}], K = “best”, search_list = [1, 9, 8, 4,
> 5]
>
>  **Output :** [{‘Gfg’: 5, ‘is’: 1, ‘best’: 1}, {‘Gfg’: 8, ‘is’: 3, ‘best’:
> 9}, {‘Gfg’: 9, ‘is’: 9, ‘best’: 8}]
>
>  **Explanation :** Dictionaries with “best” as key and values other than 1,
> 9, 8, 4, 5 are omitted.
>
>  **Input :** test_list = [{“Gfg” : 3, “is” : 5, “best” : 10},
>
> {“Gfg” : 5, “is” : 1, “best” : 1},
>
> {“Gfg” : 8, “is” : 3, “best” : 9}], K = “best”, search_list = [1, 9, 4, 5]
>
>  **Output :** [{‘Gfg’: 5, ‘is’: 1, ‘best’: 1}, {‘Gfg’: 8, ‘is’: 3, ‘best’:
> 9}]
>
>  
>
>
>  
>
>
>  **Explanation :** Dictionaries with “best” as key and values other than 1,
> 9, 4, 5 are omitted.

 **Method #1 : Using** **loop** **+** **conditional statements** ****

In this, key-value pairs are added to the resultant dictionary after checking
for Kth keys values in the list using conditionals, iterated using a loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter dictionaries by values in Kth Key in list

# Using loop + conditional statements

 

# initializing list

test_list = [{"Gfg": 3, "is": 5, "best": 10},

 {"Gfg": 5, "is": 1, "best": 1},

 {"Gfg": 8, "is": 3, "best": 9},

 {"Gfg": 9, "is": 9, "best": 8},

 {"Gfg": 4, "is": 10, "best": 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search_list

search_list = [1, 9, 8, 4, 5]

 

# initializing K

K = "best"

 

res = []

for sub in test_list:

 

 # checking if Kth key's value present in search_list

 if sub[K] in search_list:

 res.append(sub)

 

# printing result

print("Filtered dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 3, ‘is’: 5, ‘best’: 10}, {‘Gfg’: 5, ‘is’: 1,
> ‘best’: 1}, {‘Gfg’: 8, ‘is’: 3, ‘best’: 9}, {‘Gfg’: 9, ‘is’: 9, ‘best’: 8},
> {‘Gfg’: 4, ‘is’: 10, ‘best’: 7}]
>
> Filtered dictionaries : [{‘Gfg’: 5, ‘is’: 1, ‘best’: 1}, {‘Gfg’: 8, ‘is’: 3,
> ‘best’: 9}, {‘Gfg’: 9, ‘is’: 9, ‘best’: 8}]

 **Method #2 : Using** **list comprehension**

Similar to the above method, list comprehension is used to provide shorthand
to the method used above.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter dictionaries by values in Kth Key in list

# Using list comprehension

 

# initializing list

test_list = [{"Gfg": 3, "is": 5, "best": 10},

 {"Gfg": 5, "is": 1, "best": 1},

 {"Gfg": 8, "is": 3, "best": 9},

 {"Gfg": 9, "is": 9, "best": 8},

 {"Gfg": 4, "is": 10, "best": 7}, ]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search_list

search_list = [1, 9, 8, 4, 5]

 

# initializing K

K = "best"

 

# list comprehension as shorthand for solving problem

res = [sub for sub in test_list if sub[K] in
search_list]

 

# printing result

print("Filtered dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 3, ‘is’: 5, ‘best’: 10}, {‘Gfg’: 5, ‘is’: 1,
> ‘best’: 1}, {‘Gfg’: 8, ‘is’: 3, ‘best’: 9}, {‘Gfg’: 9, ‘is’: 9, ‘best’: 8},
> {‘Gfg’: 4, ‘is’: 10, ‘best’: 7}]
>
> Filtered dictionaries : [{‘Gfg’: 5, ‘is’: 1, ‘best’: 1}, {‘Gfg’: 8, ‘is’: 3,
> ‘best’: 9}, {‘Gfg’: 9, ‘is’: 9, ‘best’: 8}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

