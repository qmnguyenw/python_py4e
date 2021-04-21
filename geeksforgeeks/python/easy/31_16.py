Iterator Functions in Python | Set 2 (islice(), starmap(), tee()..)



Iterator Functions in Python | Set 1

 **1\. islice(iterable, start, stop, step)** :- This iterator **selectively
prints the values mentioned in its iterable container** passed as argument.
This iterator takes **4 arguments, iterable container, starting pos., ending
position and step.**

 **2\. starmap(func., tuple list)** :- This iterator takes a **function and
tuple list** as argument and returns the **value according to the function**
from each tuple of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# islice() and starmap()

 

# importing "itertools" for iterator operations

import itertools

 

# initializing list 

li = [2, 4, 5, 7, 8, 10, 20]

 

# initializing tuple list

li1 = [ (1, 10, 5), (8, 4, 1), (5, 4,
9), (11, 10 , 1) ]

 

 

# using islice() to slice the list acc. to need

# starts printing from 2nd index till 6th skipping 2

print ("The sliced list values are : ",end="")

print (list(itertools.islice(li,1, 6, 2)))

 

# using starmap() for selection value acc. to function

# selects min of all tuple values

print ("The values acc. to function are : ",end="")

print (list(itertools.starmap(min,li1)))  
  
---  
  
 __

 __

Output:

    
    
    The sliced list values are : [4, 7, 10]
    The values acc. to function are : [1, 1, 4, 1]
    

**3\. takewhile(func, iterable)** :- This iterator is opposite of dropwhile(),
it prints the values **till the function returns false** for 1st time.

  

  

 **4\. tee(iterator, count)** :- This iterator **splits the container into a
number of iterators** mentioned in the argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# takewhile() and tee()

 

# importing "itertools" for iterator operations

import itertools

 

# initializing list 

li = [2, 4, 6, 7, 8, 10, 20]

 

# storing list in iterator

iti = iter(li)

 

# using takewhile() to print values till condition is false.

print ("The list values till 1st false value are : ",end="")

print (list(itertools.takewhile(lambda x : x%2==0,li
)))

 

# using tee() to make a list of iterators

# makes list of 3 iterators having same values.

it = itertools.tee(iti, 3)

 

# printing the values of iterators

print ("The iterators are : ")

for i in range (0,3):

 print (list(it[i]))  
  
---  
  
 __

 __

Output:

    
    
    The list values till 1st false value are : [2, 4, 6]
    The iterators are : 
    [2, 4, 6, 7, 8, 10, 20]
    [2, 4, 6, 7, 8, 10, 20]
    [2, 4, 6, 7, 8, 10, 20]
    

**5\. zip_longest( iterable1, iterable2, fillval.)** :- This iterator prints
the **values of iterables alternatively in sequence**. If one of the iterables
is printed fully, **remaining values are filled by the values assigned to
fillvalue**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# zip_longest()

 

# importing "itertools" for iterator operations

import itertools

 

# using zip_longest() to combine two iterables.

print ("The combined values of iterables is : ")

print
(*(itertools.zip_longest('GesoGes','ekfrek',fillvalue='_'
)))  
  
---  
  
 __

 __

Output:

    
    
    The combined values of iterables is  : 
    ('G', 'e') ('e', 'k') ('s', 'f') ('o', 'r') ('G', 'e') ('e', 'k') ('s', '_')
    

**Combinatoric Iterators**

 **1\. product(iter1, iter2)** :- This iterator prints the **cartesian
product** of the two iterable containers passed as arguments.

 **2\. permutations(iter, group_size)** :- This iterator prints all **possible
permutation** of all elements of iterable. The **size** of each permuted group
is **decided by group_size** argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# product() and permutations()

 

# importing "itertools" for iterator operations

import itertools

 

# using product() to print the cartesian product

print ("The cartesian product of the containers is : ")

print (list(itertools.product('AB','12')))

 

# using permutations to compute all possible permutations

print ("All the permutations of the given container is : ")

print (list(itertools.permutations('GfG',2)))  
  
---  
  
 __

 __

Output:

  

  

    
    
    The cartesian product of the containers is : 
    [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
    All the permutations of the given container is : 
    [('G', 'f'), ('G', 'G'), ('f', 'G'), ('f', 'G'), ('G', 'G'), ('G', 'f')]
    

**3\. combinations(iterable, group_size)** :- This iterator prints **all the
possible combinations(without replacement)** of the container passed in
arguments in the **specified group size** in **sorted order.**

 **4\. combinations_with_replacement(iterable, group_size)** :- This iterator
prints **all the possible combinations(with replacement)** of the container
passed in arguments in the **specified group size** in **sorted order.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# combination() and combination_with_replacement()

 

# importing "itertools" for iterator operations

import itertools

 

# using combinations() to print every combination

# (without replacement)

print ("All the combination of container in sorted order(without
replacement) is : ")

print (list(itertools.combinations('1234',2)))

 

# using combinations_with_replacement() to print every combination

# with replacement

print ("All the combination of container in sorted order(with
replacement) is : ")

print (list(itertools.combinations_with_replacement('GfG',2)))  
  
---  
  
 __

 __

Output:

    
    
    All the combination of container in sorted order(without replacement) is : 
    [('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]
    All the combination of container in sorted order(with replacement) is : 
    [('G', 'G'), ('G', 'f'), ('G', 'G'), ('f', 'f'), ('f', 'G'), ('G', 'G')]
    

**Infinite Iterators**

 **1\. count(start, step)** :- This iterator **starts printing from the
“start” number and prints infinitely**. If steps are mentioned, the numbers
are skipped else step is 1 by default.

Example :

    
    
    iterator.count(5,2) prints -- 5,7,9,11...infinitely
    

**2\. cycle(iterable)** :- This iterator prints all values in order from the
passed container. It restarts **printing from beginning again when all
elements are printed in a cyclic manner**.

Example :

    
    
    iterator.cycle([1,2,3,4]) prints -- 1,2,3,4,1,2,3,4,1...infinitely
    

**3\. repeat(val, num)** :- This iterator **repeatedly prints** the passed
value infinite number of times. If num. is mentioned, them till that number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# repeat()

 

# importing "itertools" for iterator operations

import itertools

 

# using repeat() to repeatedly print number

print ("Printing the numbers repeatedly : ")

print (list(itertools.repeat(25,4)))  
  
---  
  
 __

 __

Output:

    
    
    Printing the numbers repeatedly : 
    [25, 25, 25, 25]
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

