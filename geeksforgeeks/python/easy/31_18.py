Iterator Functions in Python | Set 1



Perquisite: Iterators in Python

Python in its definition also allows some interesting and useful iterator
functions for efficient looping and making execution of the code faster. There
are many build-in iterators in the module “ **itertools** “.  
This module implements a number of iterator building blocks.  
 **Some useful Iterators :**

 **1\. accumulate(iter, func)** :- This iterator takes **two arguments,
iterable target and the function which would be followed at each iteration of
value in target**. If no function is passed, **addition** takes place by
default.If the input iterable is empty, the output iterable will also be
empty.

 **2\. chain(iter1, iter2..)** :- This function is used to print all the
**values in iterable targets** one after another mentioned in its arguments.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# accumulate() and chain()

 

# importing "itertools" for iterator operations

import itertools

 

# importing "operator" for operator operations

import operator

 

# initializing list 1

li1 = [1, 4, 5, 7]

 

# initializing list 2

li2 = [1, 6, 5, 9]

 

# initializing list 3

li3 = [8, 10, 5, 4]

 

# using accumulate()

# prints the successive summation of elements

print ("The sum after each iteration is : ",end="")

print (list(itertools.accumulate(li1)))

 

# using accumulate()

# prints the successive multiplication of elements

print ("The product after each iteration is : ",end="")

print (list(itertools.accumulate(li1,operator.mul)))

 

# using chain() to print all elements of lists

print ("All values in mentioned chain are : ",end="")

print (list(itertools.chain(li1,li2,li3)))  
  
---  
  
 __

 __

Output:

  

  

    
    
    The sum after each iteration is : [1, 5, 10, 17]
    The product after each iteration is : [1, 4, 20, 140]
    All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]
    

**3\. chain.from_iterable()** :- This function is implemented similarly as
chain() but the argument here is a **list of lists or any other iterable
container**.

 **4\. compress(iter, selector)** :- This iterator **selectively picks the
values to print** from the passed container **according to the boolean list**
value passed as other argument. The arguments **corresponding to boolean true
are printed** else all are skipped.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# chain.from_iterable() and compress()

 

# importing "itertools" for iterator operations

import itertools

 

# initializing list 1

li1 = [1, 4, 5, 7]

 

# initializing list 2

li2 = [1, 6, 5, 9]

 

# initializing list 3

li3 = [8, 10, 5, 4]

 

# intializing list of list

li4 = [li1, li2, li3]

 

# using chain.from_iterable() to print all elements of lists

print ("All values in mentioned chain are : ",end="")

print (list(itertools.chain.from_iterable(li4)))

 

# using compress() selectively print data values

print ("The compressed values in string are : ",end="")

print
(list(itertools.compress('GEEKSFORGEEKS',[1,0,0,0,0,1,0,0,1,0,0,0,0])))  
  
---  
  
 __

 __

Output:

    
    
    All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]
    The compressed values in string are : ['G', 'F', 'G']
    

**5\. dropwhile(func, seq)** :- This iterator starts printing the characters
only **after the func. in argument returns false** for the first time.

 **6\. filterfalse(func, seq)** :- As the name suggests, **this iterator
prints only values that return false** for the passed function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# dropwhile() and filterfalse()

 

# importing "itertools" for iterator operations

import itertools

 

# initializing list 

li = [2, 4, 5, 7, 8]

 

# using dropwhile() to start displaying after condition is false

print ("The values after condition returns false : ",end="")

print (list(itertools.dropwhile(lambda x :
x%2==0,li)))

 

# using filterfalse() to print false values

print ("The values that return false to function are : ",end="")

print (list(itertools.filterfalse(lambda x :
x%2==0,li)))  
  
---  
  
 __

 __

Output:

    
    
    The values after condition returns false : [5, 7, 8]
    The values that return false to function are : [5, 7]
    

**Reference** : https://docs.python.org/dev/library/itertools.html

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

