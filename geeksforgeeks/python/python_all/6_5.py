Python – Convert Matrix to Sets of Set



In this article, the task is to write Python program to Convert Matrix to sets
of set.

 **Examples:**

>  **Input :** test_list = [[5, 6, 3], [1, 7, 9], [8, 2, 0]]
>
>  **Output :** {frozenset({8, 0, 2}), frozenset({1, 9, 7}), frozenset({3, 5,
> 6})}
>
>  **Explanation** **:** Converted to sets of frozensets to remain immuatable
> and hashable.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [[5, 6, 3], [1, 7, 9]]
>
>  **Output :** {frozenset({1, 9, 7}), frozenset({3, 5, 6})}
>
>  **Explanation :** Converted to sets of frozensets to remain immuatable and
> hashable.

 **Method #1 : Using** **set()** **+** **frozenset()** **\+ generator
expression**

In this, we perform iteration till Matrix in generator expression to get inner
sets, and outer container is converted to set using set(). Inner container
needs to be hashable, hence has to be frozenset() for creation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to Sets of Set

# Using set() + frozenset() + generator expression

 

# initializing list

test_list = [[5, 6, 3], [1, 7, 9], [8, 2,
0]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# frozenset() to get inner elements hashable required for set()

res = set(frozenset(sub) for sub in test_list)

 

# printing result

print("Converted set Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[5, 6, 3], [1, 7, 9], [8, 2, 0]]
>
> Converted set Matrix : {frozenset({8, 0, 2}), frozenset({1, 9, 7}),
> frozenset({3, 5, 6})}
>
>  
>
>
>  
>

 **Method #2 : Using** **map()** **\+ frozenset() + set()**

In this, map() is used to extend logic of converting inner containers to
frozenset().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to Sets of Set

# Using map() + frozenset() + set()

 

# initializing list

test_list = [[5, 6, 3], [1, 7, 9], [8, 2,
0]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# map() to extend logic to inner elements

res = set(map(frozenset, test_list))

 

# printing result

print("Converted set Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[5, 6, 3], [1, 7, 9], [8, 2, 0]]
>
> Converted set Matrix : {frozenset({8, 0, 2}), frozenset({1, 9, 7}),
> frozenset({3, 5, 6})}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

