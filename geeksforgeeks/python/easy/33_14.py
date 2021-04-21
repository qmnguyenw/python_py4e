Python | Set 4 (Dictionary, Keywords in Python)



In the previous two articles (Set 2 and Set 3), we discussed the basics of
python. In this article, we will learn more about python and feel the power of
python.  
  
**Dictionary in Python**  
In python, dictionary is similar to hash or maps in other languages. It
consists of key value pairs. The value can be accessed by unique key in the
dictionary.  

__

__  
__

__

__  
__  
__

# Create a new dictionary

d = dict() # or d = {}

 

# Add a key - value pairs to dictionary

d['xyz'] = 123

d['abc'] = 345

 

# print the whole dictionary

print d

 

# print only the keys

print d.keys()

 

# print only values

print d.values()

 

# iterate over dictionary 

for i in d :

 print "%s %d" %(i, d[i])

 

# another method of iteration

for index, key in enumerate(d):

 print index, key, d[key]

 

# check if key exist

print 'xyz' in d

 

# delete the key-value pair

del d['xyz']

 

# check again 

print "xyz" in d  
  
---  
  
 __

 __

  
Output:

    
    
    {'xyz': 123, 'abc': 345}
    ['xyz', 'abc']
    [123, 345]
    xyz 123
    abc 345
    0 xyz 123
    1 abc 345
    True
    False
    

  
**break, continue, pass in Python**  
  
break – takes you out of the current loop.  
  
continue – ends the current iteration in the loop and moves to the next
iteration.  
  
pass – The pass statement does nothing. It can be used when a statement is
required. syntactically but the program requires no action. It is commonly
used for creating minimal classes.  

__

__  
__

__

__  
__  
__

# Function to illustrate break in loop

def breakTest(arr):

 for i in arr:

 if i == 5:

 break

 print i,

 # For new line

 print

 

 

# Function to illustrate continue in loop

def continueTest(arr):

 for i in arr:

 if i == 5:

 continue

 print i,

 

 # For new line

 print

 

# Function to illustrate pass 

def passTest(arr):

 pass

 

 

# Driver program to test above functions

 

# Array to be used for above functions:

arr = [1, 3 , 4, 5, 6 , 7]

 

# Illustrate break

print "Break method output"

breakTest(arr)

 

# Illustrate continue 

print "Continue method output"

continueTest(arr)

 

# Illustrate pass- Does nothing

passTest(arr)

   
  
---  
  
__

__

  
Output:

    
    
    Break method output
    1 3 4
    Continue method output
    1 3 4 6 7
    

  
**map, filter, lambda**  
  
map – The map() function applies a function to every member of iterable and
returns the result. If there are multiple arguments, map() returns a list
consisting of tuples containing the corresponding items from all iterables.  
  
filter – It takes a function returning True or False and applies it to a
sequence, returning a list of only those members of the sequence for which the
function returned True.  
  
lambda- Python provides the ability to create a simple (no statements allowed
internally) anonymous inline function called lambda function. Using lambda and
map you can have two for loops in one line.  

  

  

__

__  
__

__

__  
__  
__

# Python program to test map, filter and lambda

 

# Function to test map 

def cube(x):

 return x**2

 

# Driver to test above function

 

# Program for working of map 

print "MAP EXAMPLES"

cubes = map(cube, range(10))

print cubes

 

print "LAMBDA EXAMPLES"

 

# first parentheses contains a lambda form, that is 

# a squaring function and second parentheses represents

# calling lambda

print (lambda x: x**2)(5)

 

# Make function of two arguments that return their product

print (lambda x, y: x*y)(3, 4)

 

 

print "FILTER EXAMPLE"

special_cubes = filter(lambda x: x > 9 and x < 60,
cubes)

print special_cubes  
  
---  
  
 __

 __

  
Output:

    
    
    MAP EXAMPLES
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    LAMBDA EXAMPLES
    25
    12
    FILTER EXAMPLE
    [16, 25, 36, 49]
    

  
For more clarity about map, filter and lambda, you can have a look at the
below example:

 __

 __  
 __

 __

 __  
 __  
 __

#code without using map, filter and lambda

 

# Find the number which are odd in the list

# and multiply them by 5 and create a new list

 

# Declare a new list

x = [2, 3, 4, 5, 6]

 

# Empty list for answer

y = []

 

# Perform the operations and print the answer

for v in x:

 if v % 2:

 y += [v*5]

print y  
  
---  
  
 __

 __

  
Output:

    
    
    [15, 25]
    

  
The same operation can be performed in two lines using map, filter and lambda
as :

 __

 __  
 __

 __

 __  
 __  
 __

#above code with map, filter and lambda

 

# Declare a list 

x = [2, 3, 4, 5, 6]

 

# Perform the same operation as in above post

y = map(lambda v : v * 5, filter(lambda u : u %
2, x))

print y  
  
---  
  
 __

 __

  
Output:

    
    
    [15, 25]
    

References :  
https://docs.python.org/2/tutorial/controlflow.html#break-and-continue-
statements-and-else-clauses-on-loops  
http://www.u.arizona.edu/~erdmann/mse350/topics/list_comprehensions.html  
  
This article is contributed by **Nikhil Kumar Singh**  
  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

