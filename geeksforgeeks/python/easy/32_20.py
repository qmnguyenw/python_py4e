Object Oriented Programming in Python | Set 2 (Data Hiding and Object
Printing)



Prerequisite : Object Oriented Programming in Python | Set 1 (Class, Object
and Members)

**Data hiding**  
In Python, we use double underscore (Or __) before the attributes name and
those attributes will not be directly visible outside.

 __

 __  
 __

 __

 __  
 __  
 __

class MyClass:

 

 # Hidden member of MyClass

 __hiddenVariable = 0

 

 # A member method that changes 

 # __hiddenVariable 

 def add(self, increment):

 self.__hiddenVariable += increment

 print (self.__hiddenVariable)

 

# Driver code

myObject = MyClass() 

myObject.add(2)

myObject.add(5)

 

# This line causes error

print (myObject.__hiddenVariable)  
  
---  
  
 __

 __

Output :

    
    
    2
    7
    Traceback (most recent call last):
      File "filename.py", line 13, in 
        print (myObject.__hiddenVariable)
    AttributeError: MyClass instance has 
    no attribute '__hiddenVariable' 

In the above program, we tried to access hidden variable outside the class
using object and it threw an exception.

  

  

We can access the value of hidden attribute by a tricky syntax:

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate that hidden

# members can be accessed outside a class

class MyClass:

 

 # Hidden member of MyClass

 __hiddenVariable = 10

 

# Driver code

myObject = MyClass() 

print(myObject._MyClass__hiddenVariable)  
  
---  
  
 __

 __

Output :

    
    
    10

Private methods are accessible outside their class, just not easily
accessible. **Nothing in Python is truly private; internally** , the names of
private methods and attributes are mangled and unmangled on the fly to make
them seem inaccessible by their given names [See this for source ].

**Printing Objects**  
Printing objects gives us information about objects we are working with. In
C++, we can do this by adding a friend ostream& operator << (ostream&, const
Foobar&) method for the class. In Java, we use toString() method. In python
this can be achieved by using __repr__ or __str__ methods.

 __

 __  
 __

 __

 __  
 __  
 __

class Test:

 def __init__(self, a, b):

 self.a = a

 self.b = b

 

 def __repr__(self):

 return "Test a:%s b:%s" % (self.a, self.b)

 

 def __str__(self):

 return "From str method of Test: a is %s," \

 "b is %s" % (self.a, self.b)

 

# Driver Code 

t = Test(1234, 5678)

print(t) # This calls __str__()

print([t]) # This calls __repr__()  
  
---  
  
 __

 __

Output :

    
    
    From str method of Test: a is 1234,b is 5678
    [Test a:1234 b:5678]

 **Important Points about Printing:**

  * If no __str__ method is defined, print t (or print str(t)) uses __repr__.

 __

 __  
 __

 __

 __  
 __  
 __

class Test:

 def __init__(self, a, b):

 self.a = a

 self.b = b

 

 def __repr__(self):

 return "Test a:%s b:%s" % (self.a, self.b)

 

# Driver Code 

t = Test(1234, 5678)

print(t)   
  
---  
  
__

__

Output :

    
        Test a:1234 b:5678

  * If no __repr__ method is defined then the default is used.

