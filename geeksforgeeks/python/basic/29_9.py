Python | Set 3 (Strings, Lists, Tuples, Iterations)



In the previous article, we read about the basics of Python. Now, we continue
with some more python concepts.

 **Strings in Python**  
A string is a sequence of characters. It can be declared in python by using
double-quotes. Strings are immutable, i.e., they cannot be changed.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Assigning string to a variable

a = "This is a string"

print (a)  
  
---  
  
 __

 __

 **Lists in Python**  
Lists are one of the most powerful tools in python. They are just like the
arrays declared in other languages. But the most powerful thing is that list
need not be always homogeneous. A single list can contain strings, integers,
as well as objects. Lists can also be used for implementing stacks and queues.
Lists are mutable, i.e., they can be altered once declared.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Declaring a list

L = [1, "a" , "string" , 1+2]

print L

L.append(6)

print L

L.pop()

print L

print L[1]  
  
---  
  
 __

 __

The output is :

    
    
    [1, 'a', 'string', 3]
    [1, 'a', 'string', 3, 6]
    [1, 'a', 'string', 3]
    a
    
    
    

**Tuples in Python**  
A tuple is a sequence of immutable Python objects. Tuples are just like lists
with the exception that tuples cannot be changed once declared. Tuples are
usually faster than lists.

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

tup= (1, "a", "string", 1+2)

print(tup)

print(tup[1])  
  
---  
  
 __

 __

The output is :

    
    
    (1, 'a', 'string', 3)
    a
    
    
    

**Iterations in Python**  
Iterations or looping can be performed in python by ‘for’ and ‘while’ loops.
Apart from iterating upon a particular condition, we can also iterate on
strings, lists, and tuples.  
Example 1: Iteration by while loop for a condition

## Python

 __

 __  
 __

 __

 __  
 __  
 __

i= 1

while (i < 10):

 print(i)

 i += 1  
  
---  
  
 __

 __

The output is :

    
    
    1 2 3 4 5 6 7 8 9 
    
    
    

Example 2: Iteration by for loop on string

## Python

 __

 __  
 __

 __

 __  
 __  
 __

s= "Hello World"

for i in s :

 print (i)  
  
---  
  
 __

 __

The output is :

    
    
    H
    e
    l
    l
    o
     
    W
    o
    r
    l
    d
    
    
    

Example 3: Iteration by for loop on list

## Python

 __

 __  
 __

 __

 __  
 __  
 __

L= [1, 4, 5, 7, 8, 9]

for i in L:

 print (i)  
  
---  
  
 __

 __

The output is :

    
    
    1 4 5 7 8 9
    
    
    

Example 4 : Iteration by for loop for range

## Python

 __

 __  
 __

 __

 __  
 __  
 __

for i in range(0, 10):

 print (i)  
  
---  
  
 __

 __

The output is :

    
    
    0 1 2 3 4 5 6 7 8 9 
    
    

  * Next Article – Python: Dictionary and Keywords
  * Quiz on Data Types in Python

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

