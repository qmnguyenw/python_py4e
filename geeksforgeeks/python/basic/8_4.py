Python super()



One of the important OOP features is Inheritance in Python. When a class
inherits some or all of the behaviors from another class is known as
Inheritance. In such a case, the inherited class is the subclass and the
latter class is the parent class.  
In an inherited subclass, a parent class can be referred to with the use of
the super() function. The super function returns a temporary object of the
superclass that allows access to all of its methods to its child class.

 **Note:** For more information, refer to Inheritance in Python

Furthermore, The benefits of using a super function are:-

  * Need not remember or specify the parent class name to access its methods. This function can be used both in single and multiple inheritances.
  * This implements modularity (isolating changes) and code reusability as there is no need to rewrite the entire function.
  * Super function in Python is called dynamically because Python is a dynamic language unlike other languages.

There are 3 constraints to use the super function:-

  * The class and its methods which are referred by the super function
  * The arguments of the super function and the called function should match.
  * Every occurrence of the method must include super() after you use it.

 **Super function in single inheritance**

  

  

 **Example:** Let’s take an example of animals. Dogs, cats and cows are part
of animals. They also share common characteristics like –

  * They are mammals.
  * They have a tail and four legs.
  * They are domestic animals.

So, the classes dogs, cats and horses are subclass of animal class. This is an
example of single inheritance because many subclass are inherited from a
single parent class.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# super function

class Animals:

 

 # Initializing constructor

 def __init__(self):

 self.legs = 4

 self.domestic = True

 self.tail = True

 self.mammals = True

 

 def isMammal(self):

 if self.mammals:

 print("It is a mammal.")

 

 def isDomestic(self):

 if self.domestic:

 print("It is a domestic animal.")

 

class Dogs(Animals):

 def __init__(self):

 super().__init__()

 def isMammal(self):

 super().isMammal()

class Horses(Animals):

 def __init__(self):

 super().__init__()

 def hasTailandLegs(self):

 if self.tail and self.legs == 4:

 print("Has legs and tail")

# Driver code

Tom = Dogs()

Tom.isMammal()

Bruno = Horses()

Bruno.hasTailandLegs()  
  
---  
  
 __

 __

 **Output:**

    
    
    It is a mammal.
    Has legs and tail

 **Super function in multiple inheritance**

 **Example:** Let’s take another example. Suppose a class canfly and canswim
inherit from a mammal class and these classes are inherited by the animal
class. So the animal class inherits from the multiple base classes. Let’s see
the use of super in this case.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class Mammal():

 

 def __init__(self, name):

 print(name, "Is a mammal")

 

class canFly(Mammal):

 

 def __init__(self, canFly_name):

 print(canFly_name, "cannot fly")

 

 # Calling Parent class

 # Constructor

 super().__init__(canFly_name)

 

class canSwim(Mammal):

 

 def __init__(self, canSwim_name):

 

 print(canSwim_name, "cannot swim")

 

 super().__init__(canSwim_name)

 

class Animal(canFly, canSwim):

 

 def __init__(self, name):

 

 # Calling the contructor

 # of both thr parent

 # class in the order of

 # their inheritance

 super().__init__(name)

# Driver Code

Carol = Animal("Dog")  
  
---  
  
 __

 __

 **Output:**

    
    
    Dog cannot fly
    Dog cannot swim
    Dog Is a mammal

The class Animal inherits from two-parent classes – canFly and canSwim. So,
the subclass instance Carol can access both of the parent class constructors.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

