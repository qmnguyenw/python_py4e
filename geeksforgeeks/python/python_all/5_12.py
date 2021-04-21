Python Program to create a List using custom key-value pair of a dictionary



Given a dictionary list, the task here is to write a python program that can
convert it to a dictionary with items from values of custom keys.

>  **Input :** test_list = [{‘gfg’ : 1, ‘is’ : 4, ‘best’ : 6},
>
> {‘gfg’ : 10, ‘is’ : 3, ‘best’ : 7},
>
> {‘gfg’ : 9, ‘is’ : 4, ‘best’ : 2},
>
> {‘gfg’ : 4, ‘is’ : 1, ‘best’ : 0},
>
>  
>
>
>  
>
>
> {‘gfg’ : 6, ‘is’ : 3, ‘best’ : 8}], key, value = ‘gfg’, ‘best’
>
>  **Output :** {1: 6, 10: 7, 9: 2, 4: 0, 6: 8}
>
>  **Explanation :** Dictionary with ‘gfg”s keys and ‘best”s values is
> constructed.
>
>  **Input :** test_list = [{‘gfg’ : 1, ‘is’ : 4, ‘best’ : 6},
>
> {‘gfg’ : 10, ‘is’ : 3, ‘best’ : 7},
>
> {‘gfg’ : 9, ‘is’ : 4, ‘best’ : 2}], key, value = ‘gfg’, ‘best’
>
>  **Output :** {1: 6, 10: 7, 9: 2}
>
>  **Explanation :** Dictionary with ‘gfg”s keys and ‘best”s values is
> constructed.
>
>  
>
>
>  
>

 **Method 1 :** _Using_ _loop_

In this, dictionary list is iterated and values of required custom keys are
extracted to declare key value pairs of result dictionary.

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

test_list = [{'gfg': 1, 'is': 4, 'best': 6},

 {'gfg': 10, 'is': 3, 'best': 7},

 {'gfg': 9, 'is': 4, 'best': 2},

 {'gfg': 4, 'is': 1, 'best': 0},

 {'gfg': 6, 'is': 3, 'best': 8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key-values

key, value = 'gfg', 'best'

 

res = dict()

for sub in test_list:

 

 # constructed values

 res[sub[key]] = sub[value]

 

# printing result

print("Dictionary values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

>  _The original list is : [{‘gfg’: 1, ‘is’: 4, ‘best’: 6}, {‘gfg’: 10, ‘is’:
> 3, ‘best’: 7}, {‘gfg’: 9, ‘is’: 4, ‘best’: 2}, {‘gfg’: 4, ‘is’: 1, ‘best’:
> 0}, {‘gfg’: 6, ‘is’: 3, ‘best’: 8}]_
>
>  _Dictionary values : {1: 6, 10: 7, 9: 2, 4: 0, 6: 8}_

 **Method 2 :** Using dictionary comprehension

In this, we perform similar task as above method, difference being dictionary
comprehension is used to offer one liner alternative to solution.

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

test_list = [{'gfg': 1, 'is': 4, 'best': 6},

 {'gfg': 10, 'is': 3, 'best': 7},

 {'gfg': 9, 'is': 4, 'best': 2},

 {'gfg': 4, 'is': 1, 'best': 0},

 {'gfg': 6, 'is': 3, 'best': 8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key-values

key, value = 'gfg', 'best'

 

# dictionary comprehension for one liner

res = {sub[key]: sub[value] for sub in test_list}

 

# printing result

print("Dictionary values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

>  _The original list is : [{‘gfg’: 1, ‘is’: 4, ‘best’: 6}, {‘gfg’: 10, ‘is’:
> 3, ‘best’: 7}, {‘gfg’: 9, ‘is’: 4, ‘best’: 2}, {‘gfg’: 4, ‘is’: 1, ‘best’:
> 0}, {‘gfg’: 6, ‘is’: 3, ‘best’: 8}]_
>
>  _Dictionary values : {1: 6, 10: 7, 9: 2, 4: 0, 6: 8}_

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

