Python – Convert Nested Tuple to Custom Key Dictionary



Sometimes, while working with Python records, we can have data that come
without proper column names/identifiers, which can just be identified by their
index, but we intend to assign them keys and render in form of dictionaries.
This kind of problem can have application in domains such as web development.
Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = ((1, ‘Gfg’, 2), (3, ‘best’, 4)), keys = [‘key’,
> ‘value’, ‘id’]  
>  **Output** : [{‘key’: 1, ‘value’: ‘Gfg’, ‘id’: 2}, {‘key’: 3, ‘value’:
> ‘best’, ‘id’: 4}]
>
>  **Input** : test_tuple = test_tuple = ((1, ‘Gfg’), (2, 3)), keys = [‘key’,
> ‘value’]  
>  **Output** : [{‘key’: 1, ‘value’: ‘Gfg’}, {‘key’: 2, ‘value’: 3}]

 **Method #1 : Using list comprehension + dictionary comprehension**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of assigning keys using dictionary comprehension and
iteration of all keys and constructing data using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Nested Tuple to Custom Key Dictionary

# Using list comprehension + dictionary comprehension

 

# initializing tuple

test_tuple = ((4, 'Gfg', 10), (3, 'is', 8),
(6, 'Best', 10))

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Convert Nested Tuple to Custom Key Dictionary

# Using list comprehension + dictionary comprehension

res = [{'key': sub[0], 'value': sub[1], 'id':
sub[2]} 

 for sub in test_tuple]

 

# printing result 

print("The converted dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

> The original tuple : ((4, ‘Gfg’, 10), (3, ‘is’, 8), (6, ‘Best’, 10))  
> The converted dictionary : [{‘key’: 4, ‘value’: ‘Gfg’, ‘id’: 10}, {‘key’: 3,
> ‘value’: ‘is’, ‘id’: 8}, {‘key’: 6, ‘value’: ‘Best’, ‘id’: 10}]

