Iterators in Python



Iterator in python is an object that is used to iterate over iterable objects
like lists, tuples, dicts, and sets. The iterator object is initialized using
the **iter()** method. It uses the **next()** method for iteration.  

  1. **__iter(iterable)__** method that is called for the initialization of an iterator. This returns an iterator object
  2.  **next ( __next__ in Python 3)** The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object which further uses next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.

How an iterator really works in python  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Here is an example of a python inbuilt iterator

# value can be anything which can be iterate

iterable_value = 'Geeks'

iterable_obj = iter(iterable_value)

while True:

 try:

 # Iterate by calling next

 item = next(iterable_obj)

 print(item)

 except StopIteration:

 # exception will happen when iteration will over

 break  
  
---  
  
 __

 __

 **Output :**

    
    
    G                                                                                                                                                                            
    e                                                                                                                                                                            
    e                                                                                                                                                                            
    k                                                                                                                                                                            
    s
    
    
    

Below is a simple Python custom iterator that creates iterator type that
iterates from 10 to a given limit. For example, if the limit is 15, then it
prints 10 11 12 13 14 15. And if the limit is 5, then it prints nothing.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A simple Python program to demonstrate

# working of iterators using an example type

# that iterates from 10 to given value

# An iterable user defined type

class Test:

 # Constructor

 def __init__(self, limit):

 self.limit = limit

 # Creates iterator object

 # Called when iteration is initialized

 def __iter__(self):

 self.x = 10

 return self

 # To move to next element. In Python 3,

 # we should replace next with __next__

 def __next__(self):

 # Store current value ofx

 x = self.x

 # Stop iteration if limit is reached

 if x > self.limit:

 raise StopIteration

 # Else increment and return old value

 self.x = x + 1;

 return x

# Prints numbers from 10 to 15

for i in Test(15):

 print(i)

# Prints nothing

for i in Test(5):

 print(i)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    10
    11
    12
    13
    14
    15
    
    
    

In the following iterations, the for loop is internally(we can’t see it) using
iterator object to traverse over the iterables  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Sample built-in iterators

# Iterating over a list

print("List Iteration")

l = ["geeks", "for", "geeks"]

for i in l:

 print(i)

 

# Iterating over a tuple (immutable)

print("\nTuple Iteration")

t = ("geeks", "for", "geeks")

for i in t:

 print(i)

 

# Iterating over a String

print("\nString Iteration") 

s = "Geeks"

for i in s :

 print(i)

 

# Iterating over dictionary

print("\nDictionary Iteration") 

d = dict()

d['xyz'] = 123

d['abc'] = 345

for i in d :

 print("%s %d" %(i, d[i]))  
  
---  
  
 __

 __

 **Output :**

    
    
    List Iteration
    geeks
    for
    geeks
    
    Tuple Iteration
    geeks
    for
    geeks
    
    String Iteration
    G
    e
    e
    k
    s
    
    Dictionary Iteration
    xyz  123
    abc  345
    
    
    

**Generators in Python**  
This article is contributed by **Shwetanshu Rohatgi**. Please write comments
if you find anything incorrect, or you want to share more information about
the topic discussed above  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

