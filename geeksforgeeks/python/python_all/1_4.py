Python – Dictionary Values Mapped Summation



Given a dictionary with a values list, our task is to extract the sum of
values, found using mappings.

>  **Input :** test_dict = {4 : [‘a’, ‘v’, ‘b’, ‘e’],
>
> 1 : [‘g’, ‘f’, ‘g’],
>
> 3 : [‘e’, ‘v’]}, map_vals = {‘a’ : 3, ‘g’ : 8, ‘f’ : 10, ‘b’ : 4, ‘e’ : 7,
> ‘v’ : 2}
>
>  **Output :** {4: 16, 1: 26, 3: 9}
>
>  
>
>
>  
>
>
>  **Explanation :** “g” has 8, “f” has 10 as magnitude, hence 1 is mapped by
> 8 + 8 + 10 = 26. ( sum of list mapped ).
>
>  **Input :** test_dict = {4 : [‘a’, ‘v’, ‘b’, ‘e’],
>
> 1 : [‘g’, ‘f’, ‘g’]}, map_vals = {‘a’ : 3, ‘g’ : 8, ‘f’ : 10, ‘b’ : 4, ‘e’ :
> 7, ‘v’ : 2}
>
>  **Output :** {4: 16, 1: 26}
>
>  **Explanation :** “g” has 8, “f” has 10 as magnitude, hence 1 is mapped by
> 8 + 8 + 10 = 26. ( sum of list mapped ).

 **Method 1 : Using** **loop** **+** **items()**

In this, each key is iterated in the dictionary and each value of each dict.
is iterated and summed using mapped sum dictionary initialized.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Values Mapped Summation

# Using loop + items()

 

# initializing dictionary

test_dict = {4 : ['a', 'v', 'b', 'e'],

 1 : ['g', 'f', 'g'],

 3 : ['e', 'v']}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# values mapped 

map_vals = {'a' : 3, 'g' : 8, 'f' : 10,

 'b' : 4, 'e' : 7, 'v' : 2}

 

res = dict()

# items() getting keys and values

for key, vals in test_dict.items():

 sum = 0

 for val in vals:

 

 # summing with mappings

 sum += map_vals[val]

 res[key] = sum

 

# printing result

print("The extracted values sum : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original dictionary is : {4: [‘a’, ‘v’, ‘b’, ‘e’], 1: [‘g’, ‘f’, ‘g’],
> 3: [‘e’, ‘v’]}
>
> The extracted values sum : {4: 16, 1: 26, 3: 9}

 **Method #2 : Using** **dictionary comprehension** **+** **sum()**

In this, we perform the task of getting sum of each value using sum(). The
dictionary comprehension is used for getting keys and assigning to values sum
corresponding in shorthand.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Values Mapped Summation

# Using dictionary comprehension + sum()

 

# initializing dictionary

test_dict = {4 : ['a', 'v', 'b', 'e'],

 1 : ['g', 'f', 'g'],

 3 : ['e', 'v']}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# values mapped 

map_vals = {'a' : 3, 'g' : 8, 'f' : 10,

 'b' : 4, 'e' : 7, 'v' : 2}

 

# sum() gets sum of each mapped values 

res = {key : sum(map_vals[val] for val in vals) 

 for key, vals in test_dict.items()}

 

# printing result

print("The extracted values sum : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {4: [‘a’, ‘v’, ‘b’, ‘e’], 1: [‘g’, ‘f’, ‘g’],
> 3: [‘e’, ‘v’]}
>
> The extracted values sum : {4: 16, 1: 26, 3: 9}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

