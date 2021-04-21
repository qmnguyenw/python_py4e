Python | Create list of numbers with given range



Given two numbers _r1_ and _r2_ (which defines the range), write a Python
program to create a list with the given range (inclusive).

 **Examples:**

    
    
    **Input :** r1 = -1, r2 = 1
    **Output :** [-1, 0, 1]
    
    **Input :** r1 = 5, r2 = 9
    **Output :** [5, 6, 7, 8, 9]
    

Let’s discuss a few approaches to do this task.

 **Approach #1 :** Naive Approach

A naive method to create list within a given range is to first create an empty
list and append successor of each integer in every iteration of for loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to Create list

# with integers within given range 

 

def createList(r1, r2):

 

 # Testing if range r1 and r2 

 # are equal

 if (r1 == r2):

 return r1

 

 else:

 

 # Create empty list

 res = []

 

 # loop to append successors to 

 # list until r2 is reached.

 while(r1 < r2+1 ):

 

 res.append(r1)

 r1 += 1

 return res

 

# Driver Code

r1, r2 = -1, 1

print(createList(r1, r2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1, 0, 1]
    

  
**Approach #2 :** List comprehension

We can also use list comprehension for the purpose. Just iterate ‘item’ in a
for loop from _r1_ to _r2_ and return all ‘item’ as list. This will be a
simple one liner code.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to Create list

# with integers within given range 

 

def createList(r1, r2):

 return [item for item in range(r1, r2+1)]

 

# Driver Code

r1, r2 = -1, 1

print(createList(r1, r2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1, 0, 1]
    

  
**Approach #3 :** using Python range()

Python comes with a direct function range() which creates a sequence of
numbers from start to stop values and print each item in the sequence. We use
range() with _r1_ and _r2_ and then convert the sequence into list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to Create list

# with integers within given range 

 

def createList(r1, r2):

 return list(range(r1, r2+1))

 

# Driver Code

r1, r2 = -1, 1

print(createList(r1, r2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [-1, 0, 1]
    

  
**Approach #4 :** Using numpy.arange()

Python numpy.arange()

