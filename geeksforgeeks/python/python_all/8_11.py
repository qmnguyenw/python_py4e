Python program to get all pairwise combinations from a list



Given a list. The task is to write a Python program to get all pairwise
combinations from the list.

### Finding all Pairs (No uniqueness)

 **Example:**

>  **Input:** [1,”Mallika”,2,”Yash”]
>
>  **Output:** [(1, ‘Mallika’), (1, 2), (1, ‘Yash’), (‘Mallika’, 1),
> (‘Mallika’, 2), (‘Mallika’, ‘Yash’), (2, 1), (2, ‘Mallika’), (2, ‘Yash’),
> (‘Yash’, 1), (‘Yash’, ‘Mallika’), (‘Yash’, 2)]

 **Method 1:** Using simple loops

  

  

We can access all combinations of the list using two loops to iterate over
list indexes. If both the index counters are on the same index value, we skip
it, else we print the element at index i followed by the element at index j in
order.

The time complexity of this method is O(n2) since we require two loops to
iterate over lists.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring a list

lst = [1,"Mallika",2,"Yash"]

 

# output

output = []

 

# looping over list

for i in range(0,len(lst)):

 for j in range(0,len(lst)):

 

 # checking if i and j indexes are not on same element

 if (i!=j):

 

 # add to output

 output.append((lst[i],lst[j]))

 

# view output

print(output)  
  
---  
  
 __

 __

 **Output:**

> [(1, ‘Mallika’), (1, 2), (1, ‘Yash’), (‘Mallika’, 1), (‘Mallika’, 2),
> (‘Mallika’, ‘Yash’), (2, 1), (2, ‘Mallika’), (2, ‘Yash’), (‘Yash’, 1),
> (‘Yash’, ‘Mallika’), (‘Yash’, 2)]

 **Method 2:** Using itertools

Python provides support of **itertools** standard library which is used to
create iterators for efficient looping. The library provides support for
various kinds of iterations, in groups, sorted order, etc. The permutations()
functions of this library are used to get through all possible orderings of
the list of elements, without any repetitions. The permutations() functions
have the following syntax:

    
    
    itertools.permutations(lst,r)

Where r depicts the r-length tuples, that is, 2 depicts a pair,3 depicts a
triplet. The first argument is the specified list.

The function returns the list of groups of elements returned after forming the
permutations. The output contains n x (n-1) number of elements, where n is the
size of the list since each element is subsequently is multiplied with all
others. The time required to compute permutations is roughly exponential in
the order of the size of the list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required library

import itertools

 

# creating a list of elements belonging to integers and strings

lst = [1, "Mallika", 2, "Yash"]

 

# simulating permutations of the list in a group of 2

pair_order_list = itertools.permutations(lst, 2)

 

# printing the elements belonging to permutations

print(list(pair_order_list))  
  
---  
  
 __

 __

 **Output:**

> [(1, ‘Mallika’), (1, 2), (1, ‘Yash’), (‘Mallika’, 1), (‘Mallika’, 2),
> (‘Mallika’, ‘Yash’), (2, 1), (2, ‘Mallika’), (2, ‘Yash’), (‘Yash’, 1),
> (‘Yash’, ‘Mallika’), (‘Yash’, 2)]

 **Note:**

  * The pairs are printed in the order of the sequence of arrival of elements in the list. 
  * In the case of all same elements, the method still continues to form pairs and return them, even if they are duplicates. 

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required ibrary

import itertools

 

 

# declaring a list

lst = [2,2,2]

 

# creating a list of pairs of the list

ordered_list = itertools.permutations(lst,2)

 

# looping over the elements belonging to the

# pair of permutations

for i in ordered_list:

 

 # printing ith element

 print(i)  
  
---  
  
 __

 __

 **Output** :

    
    
    (2, 2)
    (2, 2)
    (2, 2)
    (2, 2)
    (2, 2)
    (2, 2)

### Finding all Unique Pairs (Uniqueness)

However, the permutations’ method doesn’t distinguish between (a, b) and (b,
a) pairs and returns them both. The itertools library also supports a
combinations() method that prints either of the (a, b) or (b, a) pairs and not
both. The output number of elements is equivalent to (n-1)! where n is the
length of the list. The time required to compute combinations is roughly
polynomial.

**Example:**

>  **Input:** [1,”Mallika”,2,”Yash”]
>
>  **Output:** [(1, ‘Mallika’), (1, 2), (1, ‘Yash’), (‘Mallika’, 2),
> (‘Mallika’, ‘Yash’), (2, ‘Yash’)]

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required library

import itertools

 

 

# creating a list of elements belonging 

 

3 to integers and strings

lst = [1,"Mallika",2,"Yash"]

 

# simulating permutations of the list in 

# a group of 2

pair_order_list = itertools.combinations(lst,2)

 

# printing the elements belonging to permutations

print (list(pair_order_list))  
  
---  
  
 __

 __

 **Output:**

> [(1, ‘Mallika’), (1, 2), (1, ‘Yash’), (‘Mallika’, 2), (‘Mallika’, ‘Yash’),
> (2, ‘Yash’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

