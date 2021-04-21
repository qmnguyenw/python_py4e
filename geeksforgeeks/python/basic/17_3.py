Python | range() does not return an iterator



 **range() :** Python range function generates a list of numbers which are
generally used in many situation for iteration as in for loop or in many other
cases. In python range objects are not iterators. range is a class of a list
of immutable objects. The iteration behavior of range is similar to iteration
behavior of list in list and range we can not directly call next function. We
can call next if we get an iterator using iter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to understand range

# this creates a list of 0 to 5

# integers

 

demo = range(6)

 

# print the demo

print(demo)

 

# it will generate error

print(next(demo))  
  
---  
  
 __

 __

 **OUTPUT :**

    
    
     range(0, 6)
    

**Runtime Errors :**

    
    
     Traceback (most recent call last):
      File "/home/6881218331a293819d2a4c16029084f9.py", line 13, in 
        print(next(demo))
    TypeError: list object is not an iterator
    

**Note :** Above runtime error clearly indicates that python range is not a
iterator.

Because **range is iterable** so we can get a iterator with the help of them
but we can not directly call next in next. Below example explains it clearly

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to understand range

 

# creates an iterator

demo = iter(range(6))

 

# print iterator

print(demo)

 

# use next

print(next(demo))  
  
---  
  
 __

 __

 **OUTPUT :**

    
    
    <listiterator object at 0x7f3f32a46450 >
    0
    

range does not generates all numbers that it contains when we create it. It
gives only those numbers which we get them using loop. range has following
properties.

  * range objects are immutable means that they can not be changed again so they can be used as index in dictionaries.
  * They have start stop and step arguments .
  * same range can be visit again and again

 **Example**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to understand range

 

# creates a demo range

demo = range(1, 31, 2)

 

# print the range

print(demo)

 

# print the start of range

print(demo.start)

 

# print step of range

print(demo.step)

 

# print the index of element 23

print(demo.index(23))

 

# since 30 is not present it will give error

print(demo.index(30))  
  
---  
  
 __

 __

 **OUTPUT :**

    
    
    range(1, 31, 2)
    1
    2
    11
    

**Runtime Error :** Since element 30 is not present it will rise an error

    
    
     Traceback (most recent call last):
      File "/home/cddaae6552d1d9288d7c5ab503c54642.py", line 19, in 
        print(demo.index(30))
    ValueError: 30 is not in range
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

