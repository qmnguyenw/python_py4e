type and isinstance in Python



 **type in Python**

Python have a built-in method called as type which generally come in handy
while figuring out the type of variable used in the program in the runtime.

If a single argument (object) is passed to type() built-in, it returns type of
the given object. If three arguments (name, bases and dict) are passed, it
returns a new type object.  
 **Syntax:**

    
         **type(object)
    type(name, bases, dict)**

    1.  **type() With a Single Object Parameter**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code type() with a single object parameter

x = 5

s = "geeksforgeeks"

y = [1,2,3]

print(type(x))

print(type(s))

print(type(y))  
  
---  
  
 __

 __

 **Output:**

        
        
        class 'int'
        class 'str'
        class 'list'
        

    2. **type() With a name, bases and dict Parameter**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for type() with a name,

# bases and dict parameter

 

o1 = type('X', (object,), dict(a='Foo', b=12))

 

print(type(o1))

print(vars(o1))

 

class test:

 a = 'Foo'

 b = 12

 

o2 = type('Y', (test,), dict(a='Foo', b=12))

print(type(o2))

print(vars(o2))  
  
---  
  
 __

 __

 **Output:**

  

  

        
        
        {'b': 12, 'a': 'Foo', '__dict__': , '__doc__': None, '__weakref__': }
        {'b': 12, 'a': 'Foo', '__doc__': None}
        

If you need to check type of an object, it is recommended to use Python
isinstance() function instead. It’s because isinstance() function also checks
if the given object is an instance of the subclass.

 **isinstance()**

The isinstance() function checks if the object (first argument) is an instance
or subclass of classinfo class (second argument).

 **Syntax:**

    
         **isinstance(object, classinfo)**
    
    
    The isinstance() takes two parameters:
    **object :** object to be checked
    **classinfo** : class, type, or tuple of classes and types

 **Return Value :**  
 **true** if the object is an instance or subclass of a class, or any element
of the tuple **false** otherwise. If class info is not a type or tuple of
types, a TypeError exception is raised.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for isinstance()

class Test:

 a = 5

 

TestInstance = Test()

 

print(isinstance(TestInstance, Test))

print(isinstance(TestInstance, (list, tuple)))

print(isinstance(TestInstance, (list, tuple, Test)))  
  
---  
  
 __

 __

Output:

    
        True
    False
    True

 **type() vs. isinstance()**

One elementary error people make is using the type() function where
isinstance() would be more appropriate.

    * If you’re checking to see if an object has a certain type, you want isinstance() as it checks to see if the object passed in the first argument is of the type of any of the type objects passed in the second argument. Thus, it works as expected with subclassing and old-style classes, all of which have the legacy type object instance.
    * type(), on the other hand, simply returns the type object of an object and comparing what it returns to another type object will only yield True when you use the exact same type object on both sides.  
In Python, it’s preferable to use Duck Typing( type checking be deferred to
run-time, and is implemented by means of dynamic typing or reflection) rather
than inspecting the type of an object.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

#Python code to illustrate duck typing

 

class User(object):

 def __init__(self, firstname):

 self.firstname = firstname

 

 @property

 def name(self):

 return self.firstname

 

class Animal(object):

 pass

 

class Fox(Animal):

 name = "Fox"

 

class Bear(Animal):

 name = "Bear"

 

# Use the .name attribute (or property) regardless of the type

for a in [User("Geeksforgeeks"), Fox(), Bear()]:

 print(a.name)  
  
---  
  
 __

 __

Output:

    
        Geeksforgeeks
    Fox
    Bear

  * The next reason not to use type() is the lack of support for inheritance.

 __

 __  
 __

 __

 __  
 __  
 __

#python code to illustrate the lack of

#support for inheritance in type()

 

class MyDict(dict):

 """A normal dict, that is always created with an "initial" key"""

 def __init__(self):

 self["initial"] = "some data"

 

d = MyDict()

print(type(d) == dict)

print(type(d) == MyDict)

 

d = dict()

print(type(d) == dict)

print(type(d) == MyDict)  
  
---  
  
 __

 __

 **Output:**

    
    
    False
    True
    True
    False
    

The MyDict class has all the properties of a dict, without any new methods. It
will behave exactly like a dictionary. But type() will not return the expected
result.  
Using isinstance() is preferable in this case because it will give the
expected result:

 __

 __  
 __

 __

 __  
 __  
 __

#python code to show isintance() support

#inheritance

class MyDict(dict):

 """A normal dict, that is always created with an "initial" key"""

 def __init__(self):

 self["initial"] = "some data"

 

d = MyDict()

print(isinstance(d, MyDict))

print(isinstance(d, dict))

 

d = dict()

print(isinstance(d, MyDict))

print(isinstance(d, dict))  
  
---  
  
 __

 __

Output:

    
        True
    True
    False
    True

Reference Links:

 **1.** Stack Overflow – Differences between isinstance() and type() in python  
 **2.** Programiz isintance()  
 **3.** Programiz type  
This article is contributed by **Subhajit Saha**. If you like GeeksforGeeks
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

