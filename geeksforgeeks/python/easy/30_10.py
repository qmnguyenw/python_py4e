reduce() in Python



The **reduce(fun,seq)** function is used to **apply a particular function
passed in its argument to all of the list elements** mentioned in the sequence
passed along.This function is defined in “ **functools** ” module.

 **Working :**

  * At first step, first two elements of sequence are picked and the result is obtained.
  * Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
  * This process continues till no more elements are left in the container.
  * The final returned result is returned and printed on console.

 __

 __  
 __

 __

 __  
 __  
 __

# python code to demonstrate working of reduce()

 

# importing functools for reduce()

import functools

 

# initializing list

lis = [ 1 , 3, 5, 6, 2, ]

 

# using reduce to compute sum of list

print ("The sum of the list elements is : ",end="")

print (functools.reduce(lambda a,b : a+b,lis))

 

# using reduce to compute maximum element from list

print ("The maximum element of the list is : ",end="")

print (functools.reduce(lambda a,b : a if a > b else
b,lis))  
  
---  
  
 __

 __

Output:

    
    
    The sum of the list elements is : 17
    The maximum element of the list is : 6
    

**Using Operator Functions**

reduce() can also be combined with operator functions to achieve the similar
functionality as with lambda functions and makes the code more readable.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# python code to demonstrate working of reduce()

# using operator functions

 

# importing functools for reduce()

import functools

 

# importing operator for operator functions

import operator

 

# initializing list

lis = [ 1 , 3, 5, 6, 2, ]

 

# using reduce to compute sum of list

# using operator functions

print ("The sum of the list elements is : ",end="")

print (functools.reduce(operator.add,lis))

 

# using reduce to compute product

# using operator functions

print ("The product of list elements is : ",end="")

print (functools.reduce(operator.mul,lis))

 

# using reduce to concatenate string

print ("The concatenated product is : ",end="")

print
(functools.reduce(operator.add,["geeks","for","geeks"]))  
  
---  
  
 __

 __

Output

    
    
    The sum of the list elements is : 17
    The product of list elements is : 180
    The concatenated product is : geeksforgeeks
    

**reduce() vs accumulate()**

Both reduce() and accumulate() can be used to calculate the summation of a
sequence elements. But there are differences in the implementation aspects in
both of these.

  * reduce() is defined in “functools” module, accumulate() in “itertools” module.
  * reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a iterator containing the intermediate results. The last number of the iterator returned is summation value of the list.
  * reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.

 __

 __  
 __

 __

 __  
 __  
 __

# python code to demonstrate summation

# using reduce() and accumulate()

 

# importing itertools for accumulate()

import itertools

 

# importing functools for reduce()

import functools

 

# initializing list 

lis = [ 1, 3, 4, 10, 4 ]

 

# priting summation using accumulate()

print ("The summation of list using accumulate is :",end="")

print (list(itertools.accumulate(lis,lambda x,y : x+y)))

 

# priting summation using reduce()

print ("The summation of list using reduce is :",end="")

print (functools.reduce(lambda x,y:x+y,lis))  
  
---  
  
 __

 __

Output:

    
    
    The summation of list using accumulate is :[1, 4, 8, 18, 22]
    The summation of list using reduce is :22
    

This article is contributed by **Manjeet Singh(S.Nandini)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

