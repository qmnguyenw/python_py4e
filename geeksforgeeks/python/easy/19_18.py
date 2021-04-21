Python | set() method



 **Set** , a term in mathematics for a sequence consisting of distinct
language is also extended in its language by Python and can easily be made
using set().

 **set()** method is used to convert any of the iterable to sequence of
iterable elements with distinct elements, commonly called Set.

> **Syntax :** set(iterable)  
>  **Parameters :** Any iterable sequence like list, tuple or dictionary.  
>  **Returns :** An empty set if no element is passed. Non-repeating element
> iterable modified as passed as argument.  
>

**Don’t worry if you get an unordered list from the set. Sets are unordered.
Use sorted(set(sampleList)) to get it sorted**

 **Code #1 :** Demonstrating set() with list and tuple

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate the

# working of set() on list and tuple

# initializing list

lis1 = [ 3, 4, 1, 4, 5 ]

# initializing tuple

tup1 = (3, 4, 1, 4, 5)

# Printing iterables before conversion

print("The list before conversion is : " + str(lis1))

print("The tuple before conversion is : " + str(tup1))

# Iterables after conversion are

# notice distinct and elements

print("The list after conversion is : " + str(set(lis1)))

print("The tuple after conversion is : " + str(set(tup1)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The list before conversion is : [3, 4, 1, 4, 5]
    The tuple before conversion is : (3, 4, 1, 4, 5)
    The list after conversion is : {1, 3, 4, 5}
    The tuple after conversion is : {1, 3, 4, 5}

 **Properties of set()**

  * No parameters are passed to create the empty set
  * Dictionary can also be created using set, but only keys remain after conversion, values are lost.

 **Code #2:** Demonstration of working of set on dictionary

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate the

# working of set() on dictionary

# initializing list

dic1 = { 4 : 'geeks', 1 : 'for', 3 : 'geeks' }

# Printing dictionary before conversion

# internaly sorted

print("Dictionary before conversion is : " + str(dic1))

# Dictionary after conversion are

# notice lost keys

print("Dictionary afer conversion is : " + str(set(dic1)))  
  
---  
  
 __

 __

 **Output:**

    
    
    Dictionary before conversion is : {1: 'for', 3: 'geeks', 4: 'geeks'}
    Dictionary afer conversion is : {1, 3, 4}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

