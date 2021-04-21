Python Program to extract dictionaries with maximum number of keys



Given a list of dictionaries, the task is to write a python program to extract
dictionary with maximum number of keys.

>  **Input** : test_list = [{‘Gfg’ : 1}, {‘Gfg’ : 1, ‘is’ : 5, ‘best’ : 4},
> {‘Gfg’ : 2, ‘best’ : 9}]
>
>  **Output** : {‘Gfg’ : 1, ‘is’ : 5, ‘best’ : 4}
>
>  **Explanation** : Dictionary with max. length 3 is output.
>
>  **Input :** test_list = [{‘Gfg’ : 1}, {‘Gfg’ : 2, ‘best’ : 9}]
>
>  
>
>
>  
>
>
>  **Output :** {‘Gfg’ : 2, ‘best’ : 9}
>
>  **Explanation :** Dictionary with max. length 2 is output.

 **Method 1 :** _Using_ _len()_ _and_ _loop_

In this, we iterate for all the dictionaries and keep track of its number of
keys, comparing and updating maximum at each step.

This method displays only the first dictionary found with maximum number of
elements i.e. if more than one dictionary have the same number of elements and
this number is maximum then only the first dictionary will be displayed.

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

test_list = [{'Gfg': 1}, {'Gfg': 1, 'is': 5,
'best': 4}, {'Gfg': 2, 'best': 9}]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

max_len = 0

for sub in test_list:

 

 # comparing and updating maximum dictionary acc. to length

 if len(sub) > max_len:

 res = sub

 max_len = len(sub)

 

# printing result

print("Dictionary with maximum keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 1}, {‘Gfg’: 1, ‘is’: 5, ‘best’: 4}, {‘Gfg’:
> 2, ‘best’: 9}]
>
>  
>
>
>  
>
>
> Dictionary with maximum keys : {‘Gfg’: 1, ‘is’: 5, ‘best’: 4}

 **Method 2 :** _Using_ _max()_ _and_ _list comprehension_

In this, we get the maximum length of number of keys present in dictionary
lists. Then dictionaries with maximum length computed are extracted. This
method allows multiple results for matching keys.

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

test_list = [{'Gfg': 1}, {'Gfg': 1, 'is': 5,
'best': 4},

 {'Gfg': 2, 'best': 9, "book": 1}]

 

# printing original list

print("The original list is : " + str(test_list))

 

max_len = max(len(sub) for sub in test_list)

res = [sub for sub in test_list if len(sub) ==
max_len]

 

# printing result

print("Dictionary with maximum keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 1}, {‘Gfg’: 1, ‘is’: 5, ‘best’: 4}, {‘Gfg’:
> 2, ‘best’: 9, ‘book’: 1}]
>
> Dictionary with maximum keys : [{‘Gfg’: 1, ‘is’: 5, ‘best’: 4}, {‘Gfg’: 2,
> ‘best’: 9, ‘book’: 1}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

