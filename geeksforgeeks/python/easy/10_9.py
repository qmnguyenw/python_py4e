Bound, unbound, and static methods in Python



Methods in Python are like functions except that it is attached to an
object.The methods are called on objects and it possibly make changes to that
object. These methods can be Bound, Unbound or Static method. The static
methods are one of the types of Unbound method. These types are explained in
detail below.

## Bound methods

If a function is an attribute of class and it is accessed via the instances,
they are called bound methods. A bound method is one that has ‘self‘ as its
first argument. Since these are dependent on the instance of classes, these
are also known as instance methods.

#### Need for these bound methods

The methods inside the classes would take at least one argument. To make them
zero-argument methods, ‘decorators‘ has to be used. Different instances of a
class have different values associated with them.

For example, if there is a class “Fruits”, and instances like apple, orange,
mango are possible. Each instance may have different size, color, taste, and
nutrients in it. Thus to alter any value for a specific instance, the method
must have ‘self’ as an argument that allows it to alter only its property.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

class sample(object):

 

 # Static variable for object number

 objectNo = 0

 

 def __init__(self, name1):

 

 # variable to hold name

 self.name = name1

 

 # Increment static variable for each object

 sample.objectNo = sample.objectNo + 1

 

 # each object's unique number that can be

 # considered as ID

 self.objNumber = sample.objectNo

 

 def myFunc(self):

 print("My name is ", self.name, 

 "from object ", self.objNumber)

 

 def alterIt(self, newName):

 self.name = newName

 

 def myFunc2():

 print("I am not a bound method !!!")

 

 

# creating first instance of class sample 

samp1 = sample("A")

samp1.myFunc()

 

# unhide the line below to see the error

# samp1.myFunc2() #----------> error line

 

 

# creating second instance of class sample 

samp2 = sample("B")

samp2.myFunc()

samp2.alterIt("C")

samp2.myFunc()

samp1.myFunc()  
  
---  
  
 __

 __

 **Output:**

    
    
    My name is  A from object  1
    My name is  B from object  2
    My name is  C from object  2
    My name is  A from object  1
    

In the above example two instances namely samp1 and samp2 are created. Note
that when the function alterIt() is applied to the second instance, only
that particular instance’s value is changed. The line **samp1.myFunc()** will
be expanded as **sample.myFunc(samp1)**. For this method no explicit argument
is required to be passed. The instance samp1 will be passed as argument to the
myFunc(). The line **samp1.myFunc2()** will generate the error :

    
    
    Traceback (most recent call last):
      File "/home/4f130d34a1a72402e0d26bab554c2cf6.py", line 26, in 
        samp1.myFunc2() #----------> error line
    TypeError: myFunc2() takes 0 positional arguments but 1 was given
    

It means that this method is **unbound**. It does not accept any instance as
an argument. These functions are unbound functions.

## Unbound methods and Static methods

Methods that do not have an instance of the class as the first argument are
known as unbound methods. As of Python 3.0, the unbound methods have been
removed from the language. They are not bounded with any specific object of
the class. To make the method **myFunc2()** work in the above class it should
be made into a **static method**

Static methods are similar to class methods but are bound completely to class
instead of particular objects. They are accessed using class names.

#### Need for making a method static

Not all the methods need to alter the instances of a class. They might serve
any common purpose. A method may be a utility function also.

For example, When we need to use certain mathematical functions, we use the
built in class Math. The methods in this class are made static because they
have nothing to do with specific objects. They do common actions. Thus each
time it is not an optimized way to write as:

    
    
    math=Math()
    math.ceil(5.23)

So they can be simply accessed using their class name as
**Math.ceil(5.23)**.

  

  

A method can be made static in two ways:

  1. Using staticmethod()
  2. Using decorator

 **Using staticmethod():** The staticmethod() function takes the function to
be converted as its argument and returns the static version of that function.
A static function knows nothing about the class, it just works with the
parameters passed to it.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

class sample():

 

 def myFunc2(x):

 

 print("I am", x, "from the static method")

 

sample.myFunc2 = staticmethod(sample.myFunc2)

sample.myFunc2("A")  
  
---  
  
 __

 __

 **Output:**

    
    
    I am A from the static method
    

**Using decorators:** These are features of Python used for modifying one part
of the program using another part of the program at the time of compilation.
The decorator that can be used to make a method static is

    
    
    @staticmethod

This informs the built-in default metaclass not to create any bound methods
for this method. Once this line is added before a function, the function can
be called using the class name. Consider the example taken for the Bound
method where we encountered an error. To overcome that, it can be written as:

 __

 __  
 __

 __

 __  
 __  
 __

class sample(object):

 

 # Static variable for object number

 objectNo = 0

 

 def __init__(self, name1):

 # variable to hold name

 self.name = name1

 

 # Increment static variable for each object

 sample.objectNo = sample.objectNo + 1

 

 # each object's unique number that can be

 # considered as ID

 self.objNumber = sample.objectNo

 

 def myFunc(self):

 print("My name is ", self.name, 

 "from object ", self.objNumber)

 

 def alterIt(self, newName):

 self.name = newName

 

 # using decorator to make the method static

 @staticmethod

 def myFunc2():

 print("I am not a bound method !!!")

 

 

# creating first instance of class sample 

samp1 = sample("A")

samp1.myFunc()

 

 

sample.myFunc2() #----------> error line

 

 

# creating second instance of class sample 

samp2 = sample("B")

samp2.myFunc()

samp2.alterIt("C")

samp2.myFunc()

samp1.myFunc()  
  
---  
  
 __

 __

 **Output:**

    
    
    My name is  A from object  1
    I am not a bound method !!!
    My name is  B from object  2
    My name is  C from object  2
    My name is  A from object  1
    

Here, the line **sample.myFunc2()** runs without any error and the print()
within it works perfectly and gives the output **I am not a bound method!!!**

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

