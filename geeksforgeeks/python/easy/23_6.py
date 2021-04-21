Python __iter__() and __next__() | Converting an object into an iterator



At many instances, we get a need to access an object like an iterator. One way
is to form a generator loop but that extends the task and time taken by the
programmer. Python eases this task by providing a built-in method __iter__()
for this task.

The __iter__() function returns an iterator for the given object (array, set,
tuple etc. or custom objects). It creates an object that can be accessed one
element at a time using **__next__()** function, which generally comes in
handy when dealing with loops.

 **Syntax :**

    
    
    iter(object)
    iter(callable, sentinel)

  *  _ **Object :**_ The object whose iterator has to be created. It can be a collection object like list or tuple or a user-defined object (using OOPS).
  *  _ **Callable,Sentinel :**_ Callable represents a callable object and sentinel is the value at which the iteration is needed to be terminated, sentinel value represents the end of sequence being iterated.

 **Exception :**

    
    
    If we call the iterator after all the elements have 
    been iterated, then **StopIterationError** is raised.

The __iter__() function returns an iterator object that goes through the each
element of the given object. The next element can be accessed through
__next__() function. In the case of callable object and sentinel value, the
iteration is done until the value is found or the end of elements reached. In
any case, the original object is not modified.

  

  

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code demonstrating

# basic use of iter()

listA = ['a','e','i','o','u']

 

iter_listA = iter(listA)

 

try:

 print( next(iter_listA)) 

 print( next(iter_listA)) 

 print( next(iter_listA)) 

 print( next(iter_listA)) 

 print( next(iter_listA))

 print( next(iter_listA)) #StopIteration error

except:

 pass  
  
---  
  
 __

 __

 **Output :**

    
    
    a
    e
    i
    o
    u
    

**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code demonstrating

# basic use of iter()

lst = [11, 22, 33, 44, 55]

 

iter_lst = iter(lst)

while True:

 try:

 print(iter_lst.__next__()) 

 except:

 break  
  
---  
  
 __

 __

Output :

    
    
    11
    22
    33
    44
    55

  
**Code #3 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code demonstrating

# basic use of iter()

 

listB = ['Cat', 'Bat', 'Sat', 'Mat']

 

 

iter_listB = listB.__iter__()

 

try:

 print(iter_listB.__next__())

 print(iter_listB.__next__())

 print(iter_listB.__next__())

 print(iter_listB.__next__())

 print(iter_listB.__next__()) #StopIteration error

except:

 print(" \nThrowing 'StopIterationError'",

 "I cannot count more.")  
  
---  
  
 __

 __

Output :

    
    
    Cat
    Bat
    Sat
    Mat
     
    Throwing 'StopIterationError' I cannot count more.

  
**Code #4 : User-defined objects (using OOPS)**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code showing use of iter() using OOPs

 

class Counter:

 def __init__(self, start, end):

 self.num = start

 self.end = end

 

 def __iter__(self):

 return self

 

 def __next__(self): 

 if self.num > self.end:

 raise StopIteration

 else:

 self.num += 1

 return self.num - 1

 

 

# Driver code

if __name__ == '__main__' :

 

 a, b = 2, 5

 

 c1 = Counter(a, b)

 c2 = Counter(a, b)

 

 # Way 1-to print the range without iter()

 print ("Print the range without iter()")

 

 for i in c1:

 print ("Eating more Pizzas, couting ", i, end ="\n")

 

 print ("\nPrint the range using iter()\n")

 

 # Way 2- using iter()

 obj = iter(c2)

 try:

 while True: # Print till error raised

 print ("Eating more Pizzas, couting ", next(obj))

 except: 

 # when StopIteration raised, Print custom message

 print ("\nDead on overfood, GAME OVER")   
  
---  
  
__

__

**Output :**

    
    
    Print the range without iter()
    Eating more Pizzas, couting  2
    Eating more Pizzas, couting  3
    Eating more Pizzas, couting  4
    Eating more Pizzas, couting  5
    
    Print the range using iter()
    
    Eating more Pizzas, couting  2
    Eating more Pizzas, couting  3
    Eating more Pizzas, couting  4
    Eating more Pizzas, couting  5
    
    Dead on overfood, GAME OVER

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

