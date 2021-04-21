Mutable vs Immutable Objects in Python



Every variable in python holds an instance of an object. There are two types
of objects in python i.e. **Mutable** and **Immutable objects**. Whenever an
object is instantiated, it is assigned a unique object id. The type of the
object is defined at the runtime and it can’t be changed afterwards. However,
it’s state can be changed if it is a mutable object.

To summarise the difference, mutable objects can change their state or
contents and immutable objects can’t change their state or content.

  *  **Immutable Objects :** These are of in-built types like **int, float, bool, string, unicode, tuple**. In simple words, an immutable object can’t be changed after it is created.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to test that

# tuples are immutable 

 

tuple1 = (0, 1, 2, 3) 

tuple1[0] = 4

print(tuple1)  
  
---  
  
 __

 __

Error :

    
    
    Traceback (most recent call last):
      File "e0eaddff843a8695575daec34506f126.py", line 3, in 
        tuple1[0]=4
    TypeError: 'tuple' object does not support item assignment

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to test that

# strings are immutable 

 

message = "Welcome to GeeksforGeeks"

message[0] = 'p'

print(message)  
  
---  
  
 __

 __

 **Error :**

    
        Traceback (most recent call last):
      File "/home/ff856d3c5411909530c4d328eeca165b.py", line 3, in 
        message[0] = 'p'
    TypeError: 'str' object does not support item assignment

  *  **Mutable Objects :** These are of type **list, dict, set **. Custom classes are generally mutable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to test that

# lists are mutable 

color = ["red", "blue", "green"]

print(color)

 

color[0] = "pink"

color[-1] = "orange"

print(color)  
  
---  
  
 __

 __

Output:

  

  

    
        ['red', 'blue', 'green']
    ['pink', 'blue', 'orange']

 **Conclusion**

  1. Mutable and immutable objects are handled differently in python. Immutable objects are quicker to access and are expensive to **change** because it involves the creation of a copy.  
Whereas mutable objects are easy to change.

  2. Use of mutable objects is recommended when there is a need to change the size or content of the object.
  3.  **Exception :** However, there is an exception in immutability as well. We know that tuple in python is immutable. But the tuple consists of a sequence of names with unchangeable bindings to objects.  
Consider a tuple

    
         tup = ([3, 4, 5], 'myname') 

The tuple consists of a string and a list. Strings are immutable so we can’t
change its value. But the contents of the list can change. **The tuple itself
isn’t mutable but contain items that are mutable.**

As a rule of thumb, Generally Primitive-like types are probably immutable and
Customized Container-like types are mostly mutable.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

