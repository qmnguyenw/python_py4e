Python – Convert Matrix to Coordinate Dictionary



Sometimes, while working with Python dictionaries, we can have problem in
which we need to perform the conversion of matrix elements to their coordinate
list. This kind of problem can come in many domains including day-day
programming and competitive programming. Lets discuss certain ways in which
this task can be performed.

>  **Input** : test_list = [[‘g’, ‘g’, ‘g’], [‘g’, ‘g’, ‘g’]]  
>  **Output** : {‘g’: {(0, 1), (1, 2), (0, 0), (1, 1), (1, 0), (0, 2)}}
>
>  **Input** : test_list = [[‘a’, ‘b’, ‘c’]]  
>  **Output** : {‘a’: {(0, 0)}, ‘b’: {(0, 1)}, ‘c’: {(0, 2)}}

 **Method #1 : Using loop +enumerate()**  
The combination of above functionalities can be used to perform this task. In
this, we use brute force to extract elements and assign indices to them with
the help of enumerate().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to Coordinate Dictionary

# Using loop + enumerate()

 

# initializing list

test_list = [['g', 'f', 'g'], ['i', 's', 'g'],
['b', 'e', 's', 't']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Matrix to Coordinate Dictionary

# Using loop + enumerate()

res = dict()

for idx, sub in enumerate(test_list):

 for j, ele in enumerate(sub):

 if ele in res:

 res[ele].add((idx, j))

 else:

 res[ele] = {(idx, j)}

 

# printing result 

print("The Coordinate Dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [[‘g’, ‘f’, ‘g’], [‘i’, ‘s’, ‘g’], [‘b’, ‘e’, ‘s’,
> ‘t’]]  
> The Coordinate Dictionary : {‘g’: {(1, 2), (0, 0), (0, 2)}, ‘f’: {(0, 1)},
> ‘t’: {(2, 3)}, ‘i’: {(1, 0)}, ‘b’: {(2, 0)}, ‘e’: {(2, 1)}, ‘s’: {(1, 1),
> (2, 2)}}

