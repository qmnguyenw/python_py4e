Shared Reference in Python



Let, we assign a variable x to value 5, and another variable y to the variable
x.

 __

 __  
 __

 __

 __  
 __  
 __

x= 5

y = x  
  
---  
  
 __

 __

When Python looks at the first statement, what it does is that, first, it
creates an object to represent the value 5. Then, it creates the variable x if
it doesn’t exist and made it a reference to this new object 5. The second line
causes Python to create the variable y, and it is not assigned with x, rather
it is made to reference that object that x does. The net effect is that the
variables x and y wind up referencing the same object. This situation, with
multiple names referencing the same object, is called a **Shared Reference**
in Python.  
Now, if we write:

 __

 __  
 __

 __

 __  
 __  
 __

x= 'Geeks'  
  
---  
  
 __

 __

This statement makes a new object to represent ‘Geeks’ and makes x to
reference this new object. However, y still references the original object i.e
5. Again if we write one more statement as:

 __

 __  
 __

 __

 __  
 __  
 __

b= 10  
  
---  
  
 __

 __

This statement causes the creation of a new object and made y to reference
this new object. The space held by the prior object is reclaimed if it is no
longer referenced, that is, the object’s space is automatically thrown back
into the free space pool, to be reused for a future object.  
This automatic reclamation of object’s space is known as **Garbage
Collection**.

## Shared reference and In- place changes

There are objects and operations that perform in-place object changes. For
example, an assignment to an element in a list actually changes the list
object itself in-place, rather than creating a new list object. For objects
that support in-place changes, you need to be very careful of shared
reference, as a change in one can affect others.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

L1= [1, 2, 3, 4, 5]

 

L2 = L1  
  
---  
  
 __

 __

Just like x and y, L1 and L2, after statement 2, will refer to the same
object. If we change the 0th place value in L1, Now think what will happen,
whether it will change only L1 or both L1 and L2 ?

 __

 __  
 __

 __

 __  
 __  
 __

L1= [1, 2, 3, 4, 5]

L2 = L1

 

L1[0] = 0

 

print(L1)

print(L2)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 2, 3, 4, 5]
    [0, 2, 3, 4, 5]

Thus, the change in L1 reflects back to L2. Rather than creating a new object
for L1, it overwrites the part of the list object at that place. This is an
in-place change. If we still want to maintain a separate copy for L2 such that
any changes in L1 doesn’t reflect in L2, then we can request Python to create
a copy of the list L1 for L2.

 __

 __  
 __

 __

 __  
 __  
 __

L1= [1, 2, 3, 4, 5]

L2 = L1[:]

 

L1[0] = 0

 

print(L1)

print(L2)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]

 **Note:** This slicing technique doesn’t work for dictionaries and sets.

Because of Python’s reference model, there are two different ways to check for
equality in Python Program.

 __

 __  
 __

 __

 __  
 __  
 __

L1= [1, 2, 3, 4, 5]

L2 = L1

 

print(L1 == L2)

print(L1 is L2)  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    True

The first method, the == operator tests whether the referenced objects have
the same values, if they have the same values, it returns True, otherwise
False. The second method, the is operator, instead tests for object identity
– it returns True only if both names point to the exact same object, so
basically it is a much stronger form of equality testing. It serves as a way
to detect shared references in your code if required. It returns False if the
names point to an equivalent but different objects.

  

  

 **Now, here comes a tricky part:**  
Look at the following code,

 __

 __  
 __

 __

 __  
 __  
 __

L1= [1, 2, 3, 4, 5]

L2 = [1, 2, 3, 4, 5]

 

print(L1 == L2)

print(L1 is L2)  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    False

What will happen if we perform the same operation on small numbers:

 __

 __  
 __

 __

 __  
 __  
 __

a= 50

b = 50

 

print(a == b)

print(a is b)  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    True

Because small integers and strings are cached and reused, therefore they refer
to a same single object. And since, you cannot change integers or strings in-
place, so it doesn’t matter how many references there are to the same object.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

