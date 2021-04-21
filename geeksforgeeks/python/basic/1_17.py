How to iterate over OrderedDict in Python?



An OrderedDict is a subclass that preserves the order in which the keys are
inserted. The difference between _OrderedDict_ and _Dict_ is that the normal
_Dict_ does not keep a track of the way the elements are inserted whereas the
_OrderedDict_ remembers the order in which the elements are inserted.

**Explanation:**

>  **Input :** original_dict = { ‘a’:1, ‘b’:2, ‘c’:3, ‘d’:4 }
>
>  **Output:** a 1 b 2 c 3 d 4
>
>  **Input:** original_dict = {‘sayantan’:9, ‘sanjoy’:7, ‘suresh’:5, ‘rony’:2}
>
>  
>
>
>  
>
>
>  **Output:** sayantan 9 sanjoy 7 suresh 5 rony 2

 **Steps to perform iteration through Ordereddict in python :**

  * Import the _ordereddict_ from _collection_ in python.
  * Take the input of the _ordereddict._
  * Iterate through the _ordereddict_ in either of the two approaches given below:

 **Approach #1**

Iterating through the _ordereddict_ and printing the value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to implement iteration

# over the ordereddict

 

# import required modules

from collections import OrderedDict

 

# create dictionary

od = OrderedDict({'a': 1, 'b': 2, 'c': 3,
'd': 4})

 

# iterating over the ordereddict

for key, value in od.items():

 print(key, value)  
  
---  
  
 __

 __

 **Output :**

    
    
    a 1
    b 2
    c 3
    d 4

The above code can also be written as –

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to implement iteration

# over the ordereddict

 

# import required modules

from collections import OrderedDict

 

# create dictionary

od = OrderedDict({'a': 1, 'b': 2, 'c': 3,
'd': 4})

 

# iterating over the ordereddict

for item in od.items():

 print(*item)  
  
---  
  
 __

 __

 **Output :**

    
    
    a 1
    b 2
    c 3
    d 4

 **Approach #2**

Iterating through the enumerate objects and printing the value. The
enumerate() method is a method in which it adds a counter to the iterable
object and returns the value in the form of an enumerate object.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to implement iteration

# over the ordereddict

 

# import required modules

from collections import OrderedDict

 

# create dictionary

od = OrderedDict({'a': 1, 'b': 2, 'c': 3,
'd': 4})

 

# iterating through the enumerate objects

for i, (key, value) in enumerate(od.items()):

 print(key, value)  
  
---  
  
 __

 __

 **Output:**

    
    
    a 1
    b 2
    c 3
    d 4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

