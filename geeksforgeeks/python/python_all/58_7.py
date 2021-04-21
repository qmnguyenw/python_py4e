Python program to get all unique combinations of two Lists



The combination is a mathematical technique which calculates the number of
possible arrangements in a collection of items or list. In combination order
of selection doesn’t matter. The unique combination of two lists in Python can
be formed by pairing each element of the first list with the elements of the
second list.

**Example:**

    
    
    List_1 = ["a","b"]
    List_2 = [1,2]
    Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] 
    

**Method 1 :** Using **permutation()** of itertools package and **zip()**
function.

 **Approach :**

  * Import itertools package and initialize list_1 and list_2.
  * Create an empty list of ‘unique_combinations’ to store the resulting combinations so obtained.
  * Call itertools.permutations( ) which will return permutations of list_1 with length of list_2. Generally, the length of the shorter list is taken and if both lists are equal, use either.
  * For loop is used and zip() function is called to pair each permutation and shorter list element into the combination.
  * Then each combination is converted into a list and append to the combination list.

Below is the implementation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# python program to demonstrate

# unique combination of two lists

# using zip() and permutation of itertools

 

# import itertools package

import itertools

from itertools import permutations 

 

# initialize lists

list_1 = ["a", "b", "c","d"]

list_2 = [1,4,9]

 

# create empty list to store the

# combinations

unique_combinations = []

 

# Getting all permutations of list_1 

# with length of list_2

permut = itertools.permutations(list_1, len(list_2))

 

# zip() is called to pair each permutation

# and shorter list element into combination

for comb in permut:

 zipped = zip(comb, list_2)

 unique_combinations.append(list(zipped))

 

# printing unique_combination list 

print(unique_combinations)  
  
---  
  
 __

 __

 **Output :**

> [[(‘a’, 1), (‘b’, 4), (‘c’, 9)], [(‘a’, 1), (‘b’, 4), (‘d’, 9)], [(‘a’, 1),
> (‘c’, 4), (‘b’, 9)], [(‘a’, 1), (‘c’, 4), (‘d’, 9)], [(‘a’, 1), (‘d’, 4),
> (‘b’, 9)], [(‘a’, 1), (‘d’, 4), (‘c’, 9)], [(‘b’, 1), (‘a’, 4), (‘c’, 9)],
> [(‘b’, 1), (‘a’, 4), (‘d’, 9)], [(‘b’, 1), (‘c’, 4), (‘a’, 9)], [(‘b’, 1),
> (‘c’, 4), (‘d’, 9)], [(‘b’, 1), (‘d’, 4), (‘a’, 9)], [(‘b’, 1), (‘d’, 4),
> (‘c’, 9)], [(‘c’, 1), (‘a’, 4), (‘b’, 9)], [(‘c’, 1), (‘a’, 4), (‘d’, 9)],
> [(‘c’, 1), (‘b’, 4), (‘a’, 9)], [(‘c’, 1), (‘b’, 4), (‘d’, 9)], [(‘c’, 1),
> (‘d’, 4), (‘a’, 9)], [(‘c’, 1), (‘d’, 4), (‘b’, 9)], [(‘d’, 1), (‘a’, 4),
> (‘b’, 9)], [(‘d’, 1), (‘a’, 4), (‘c’, 9)], [(‘d’, 1), (‘b’, 4), (‘a’, 9)],
> [(‘d’, 1), (‘b’, 4), (‘c’, 9)], [(‘d’, 1), (‘c’, 4), (‘a’, 9)], [(‘d’, 1),
> (‘c’, 4), (‘b’, 9)]]

 **Method 2 :** Using **product()** of itertools package and **zip()**
function.

 **Approach :**

  * Import itertools package and initialize list_1 and list_2.
  * Create an empty list of ‘unique_combinations’ to store the resulting combinations so obtained.
  * product() is called to find all possible combinations of elements.
  * And zip() is used to pair up all these combinations, converting each element into a list and append them to the desired combination list.

Below is the implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# python program to demonstrate

# unique combination of two lists

# using zip() and product() of itertools

 

# import itertools package

import itertools

from itertools import product 

 

# initilize lists

list_1 = ["b","c","d"]

list_2 = [1,4,9]

 

# create empty list to store the combinations

unique_combinations = []

 

# Extract Combination Mapping in two lists 

# using zip() + product() 

unique_combinations = list(list(zip(list_1, element))

 for element in product(list_2, repeat = len(list_1)))

 

# printing unique_combination list 

print(unique_combinations)  
  
---  
  
 __

 __

 **Output :**

> [[(‘b’, 1), (‘c’, 1), (‘d’, 1)], [(‘b’, 1), (‘c’, 1), (‘d’, 4)], [(‘b’, 1),
> (‘c’, 1), (‘d’, 9)], [(‘b’, 1), (‘c’, 4), (‘d’, 1)], [(‘b’, 1), (‘c’, 4),
> (‘d’, 4)], [(‘b’, 1), (‘c’, 4), (‘d’, 9)], [(‘b’, 1), (‘c’, 9), (‘d’, 1)],
> [(‘b’, 1), (‘c’, 9), (‘d’, 4)], [(‘b’, 1), (‘c’, 9), (‘d’, 9)], [(‘b’, 4),
> (‘c’, 1), (‘d’, 1)], [(‘b’, 4), (‘c’, 1), (‘d’, 4)], [(‘b’, 4), (‘c’, 1),
> (‘d’, 9)], [(‘b’, 4), (‘c’, 4), (‘d’, 1)], [(‘b’, 4), (‘c’, 4), (‘d’, 4)],
> [(‘b’, 4), (‘c’, 4), (‘d’, 9)], [(‘b’, 4), (‘c’, 9), (‘d’, 1)], [(‘b’, 4),
> (‘c’, 9), (‘d’, 4)], [(‘b’, 4), (‘c’, 9), (‘d’, 9)], [(‘b’, 9), (‘c’, 1),
> (‘d’, 1)], [(‘b’, 9), (‘c’, 1), (‘d’, 4)], [(‘b’, 9), (‘c’, 1), (‘d’, 9)],
> [(‘b’, 9), (‘c’, 4), (‘d’, 1)], [(‘b’, 9), (‘c’, 4), (‘d’, 4)], [(‘b’, 9),
> (‘c’, 4), (‘d’, 9)], [(‘b’, 9), (‘c’, 9), (‘d’, 1)], [(‘b’, 9), (‘c’, 9),
> (‘d’, 4)], [(‘b’, 9), (‘c’, 9), (‘d’, 9)]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

