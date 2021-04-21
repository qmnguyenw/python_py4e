Tuples in Python



A Tuple is a collection of Python objects separated by commas. In someways a
tuple is similar to a list in terms of indexing, nested objects and repetition
but a tuple is immutable unlike lists which are mutable.

 **Creating Tuples**

 __

 __  
 __

 __

 __  
 __  
 __

# An empty tuple

empty_tuple = ()

print (empty_tuple)  
  
---  
  
 __

 __

Output:

    
    
     ()

 __

 __  
 __

 __

 __  
 __  
 __

# Creating non-empty tuples

 

# One way of creation

tup = 'python', 'geeks'

print(tup)

 

# Another for doing the same

tup = ('python', 'geeks')

print(tup)  
  
---  
  
 __

 __

Output

    
    
    ('python', 'geeks')
    ('python', 'geeks')

 _Note: In case your generating a tuple with a single element, make sure to
add a comma after the element._

  

  

**Concatenation of Tuples**

 __

 __  
 __

 __

 __  
 __  
 __

# Code for concatenating 2 tuples

 

tuple1 = (0, 1, 2, 3)

tuple2 = ('python', 'geek')

 

# Concatenating above two

print(tuple1 + tuple2)  
  
---  
  
 __

 __

Output:

    
    
    (0, 1, 2, 3, 'python', 'geek')

**Nesting of Tuples**

 __

 __  
 __

 __

 __  
 __  
 __

# Code for creating nested tuples

 

tuple1 = (0, 1, 2, 3)

tuple2 = ('python', 'geek')

tuple3 = (tuple1, tuple2)

print(tuple3)  
  
---  
  
 __

 __

Output :

    
    
    ((0, 1, 2, 3), ('python', 'geek'))

**Repetition in Tuples**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Code to create a tuple with repetition

 

tuple3 = ('python',)*3

print(tuple3)  
  
---  
  
 __

 __

Output

    
    
     ('python', 'python', 'python')

Try the above without a comma and check. You will get tuple3 as a string
‘pythonpythonpython’.

**Immutable Tuples**

 __

 __  
 __

 __

 __  
 __  
 __

#code to test that tuples are immutable

 

tuple1 = (0, 1, 2, 3)

tuple1[0] = 4

print(tuple1)  
  
---  
  
 __

 __

Output

    
    
    Traceback (most recent call last):
      File "e0eaddff843a8695575daec34506f126.py", line 3, in
        tuple1[0]=4
    TypeError: 'tuple' object does not support item assignment

**Slicing in Tuples**

 __

 __  
 __

 __

 __  
 __  
 __

# code to test slicing

 

tuple1 = (0 ,1, 2, 3)

print(tuple1[1:])

print(tuple1[::-1])

print(tuple1[2:4])  
  
---  
  
 __

 __

Output

    
    
    (1, 2, 3)
    (3, 2, 1, 0)
    (2, 3)

**Deleting a Tuple**

 __

 __  
 __

 __

 __  
 __  
 __

# Code for deleting a tuple

 

tuple3 = ( 0, 1)

del tuple3

print(tuple3)  
  
---  
  
 __

 __

Error:

    
    
    Traceback (most recent call last):
      File "d92694727db1dc9118a5250bf04dafbd.py", line 6, in <module>
        print(tuple3)
    NameError: name 'tuple3' is not defined

Output:

    
    
    (0, 1)

**Finding Length of a Tuple**

 __

 __  
 __

 __

 __  
 __  
 __

# Code for printing the length of a tuple

 

tuple2 = ('python', 'geek')

print(len(tuple2))  
  
---  
  
 __

 __

Output

    
    
     2

**Converting list to a Tuple**

 __

 __  
 __

 __

 __  
 __  
 __

# Code for converting a list and a string into a tuple

 

list1 = [0, 1, 2]

print(tuple(list1))

print(tuple('python')) # string 'python'  
  
---  
  
 __

 __

Output

    
    
    (0, 1, 2)
    ('p', 'y', 't', 'h', 'o', 'n')

Takes a single parameter which may be a list,string,set or even a dictionary(
only keys are taken as elements) and converts them to a tuple.

**Tuples in a loop**

 __

 __  
 __

 __

 __  
 __  
 __

#python code for creating tuples in a loop

 

tup = ('geek',)

n = 5 #Number of time loop runs

for i in range(int(n)):

 tup = (tup,)

 print(tup)  
  
---  
  
 __

 __

Output :

    
    
    (('geek',),)
    ((('geek',),),)
    (((('geek',),),),)
    ((((('geek',),),),),)
    (((((('geek',),),),),),)
    

**Using cmp(), max() , min()**

 __

 __  
 __

 __

 __  
 __  
 __

# A python program to demonstrate the use of

# cmp(), max(), min()

 

tuple1 = ('python', 'geek')

tuple2 = ('coder', 1)

 

if (cmp(tuple1, tuple2) != 0):

 

 # cmp() returns 0 if matched, 1 when not tuple1 

 # is longer and -1 when tuple1 is shoter

 print('Not the same')

else:

 print('Same')

print ('Maximum element in tuples 1,2: ' +

 str(max(tuple1)) + ',' +

 str(max(tuple2)))

print ('Minimum element in tuples 1,2: ' +

 str(min(tuple1)) + ',' + str(min(tuple2)))  
  
---  
  
 __

 __

Output

    
    
    Not the same
    Maximum element in tuples 1,2: python,coder
    Minimum element in tuples 1,2: geek,1
    

_Note: max() and min() checks the based on ASCII values. If there are two
strings in a tuple, then the first different character in the strings are
checked._

This article is contributed by **Sri Sanketh Uppalapati.** Please write
comments if you find anything incorrect, or you want to share more information
about the topic discussed above.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

