How to check if an object is iterable in Python?



In simple words, any object that could be looped over is iterable. For
instance, a list object is iterable and so is an str object. The list numbers
and string names are iterables because we are able to loop over them (using a
for-loop in this case). In this article, we are going to see how to check if
an object is iterable in Python.

 **Examples:**

>  **Input:** “Hello”
>
>  **Output:** object is not iterable
>
>  **Explanation:** Object could be like( h, e, l, l, o)
>
>  
>
>
>  
>
>
>  **Input:** 5
>
>  **Output:** **‘** int’ object is not iterable

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

name = "Hello"

 

for letter in name:

 print(letter, end = " ")  
  
---  
  
 __

 __

 **Output:**

    
    
    H e l l o

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

number = 5

for i in number:

 print(i)  
  
---  
  
 __

 __

 **Output**

    
    
     **TypeError:** **'int'** object is not **iterable**

However, an **int** object is not **iterable** and so is a float object. The
integer object number is not **iterable** , as we are not able to loop over
it.

#### Checking an object’s iterability

We are going to explore the different ways of checking whether an object is
**iterable** or not. We use the **hasattr()** function to test whether the
string object name has **__iter__** attribute for checking iterability.
However, this check is not comprehensive.

  

  

 **Method 1: Using __iter__ method check.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

name = 'Roster'

 

if hasattr(name, '__iter__'):

 print(f'{name} is iterable')

 

else:

 print(f'{name} is not iterable')  
  
---  
  
 __

 __

 **Output:**

    
    
    Roster is iterable

 **Method 2: Using the Iterable class of collections.abc module.**

We could verify that an object is iterable by checking whether it is an
instance of the Iterable class. The instance check reports the string object
as iterable correctly using the Iterable class. This works for Python 3 as
well. For Python 3.3 and above, you will have to import the Iterable class
from **collections.abc** and not from collections like so:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

from collections.abc import Iterable

 

 

name = 'Roster'

 

if isinstance(name, Iterable):

 print(f"{name} is iterable")

 

else:

 print(f"{name} is not iterable")  
  
---  
  
 __

 __

 **Output:**

    
    
    Roster is iterable

 **Method 3: Using the iter() builtin function.**

The **iter** built-in function works in the following way:

  * Checks whether the object implements **__iter__,** and calls that to obtain an iterator.
  * If that fails, Python raises **TypeError** , usually saying “C object is not **iterable,** ” where C is the class of the target object.

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

name = "Roster"

 

try:

 iter(name)

 print("{} is iterable".format(name)) 

 

except TypeError:

 print("{} is not iterable".format(name))  
  
---  
  
 __

 __

 **Output:**

    
    
    Roster is iterable

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

