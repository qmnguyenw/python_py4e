Python sorted containers | An Introduction



 **Sorted Containers** is an Apache2 licensed sorted collections library,
written in pure-Python, and fast as C-extensions. It was created by Grant
Jenks and is an open source library. It is a collection of containers that
allow us to insert and remove elements very efficiently while maintaining
sorted order.

 **Features:**

  * Pure-Python
  * Fully documented
  * Benchmark comparison (alternatives, runtimes, load-factors
  * Performance (often faster than C implementations)
  * Compatible API (nearly identical to popular blist and rbtree modules)
  * Feature-rich (e.g. get the five largest keys in a sorted dict: d.iloc[-5:])
  * Pragmatic design (e.g. SortedSet is a Python set with a SortedList index)

 **Containers:**

  * SortedList
  * SortedDict
  * SortedSet

 **Installation:**

 **Mac** and **Linux** users can install via pip command:

  

  

    
    
     sudo pip install sortedcontainers 

## SortedList –

Sorted list is a sorted mutable sequence in which the values are maintained in
sorted order.

 **Functions to add and remove elements:**

>  **add(value)** : A function that takes one element as parameter and inserts
> it into the list by maintaining sorted order. _Runtime Complexity:_
> O(log(n))
>
>  **update(iterable)** : A function that takes an iterable as input and
> updates the SortedList adding all the values from the iterable _Runtime
> complexity:_ O(k*log(n)).
>
>  **clear()** : Remove all values from sorted list. _Runtime complexity:_
> O(n).
>
>  **discard(value)** : Remove value from sorted list if it is a member. If
> value is not a member, do nothing. _Runtime complexity:_ O(log(n)).

Below is the implementation –

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from sortedcontainers import SortedList, SortedSet, SortedDict

 

# initializing a sorted list with parameters

# it takes an iterable as a parameter.

sorted_list = SortedList([1, 2, 3, 4])

 

# initializing a sorted list using default constructor

sorted_list = SortedList()

 

# inserting values one by one using add()

for i in range(5, 0, -1):

 sorted_list.add(i)

 

# prints the elements in sorted order

print('list after adding 5 elements: ', sorted_list)

 

print('list elements are: ', end = '')

 

# iterating through a sorted list

for i in sorted_list:

 print(i, end = ' ')

print()

 

# removing all elements using clear()

sorted_list.clear()

 

# adding elements using the update() function

elements = [10, 9, 8, 7, 6]

 

sorted_list.update(elements)

 

# prints the updated list in sorted order

print('list after updating: ', sorted_list)

 

# removing a particular element

sorted_list.discard(8)

 

print('list after removing one element: ', sorted_list)

 

# removing all elements

sorted_list.clear()

 

print('list after removing all elements using clear: ', sorted_list)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    list after adding 5 elements:  SortedList([1, 2, 3, 4, 5], load=1000)
    
    list elements are: 1 2 3 4 5 
    
    list after updating:  SortedList([6, 7, 8, 9, 10], load=1000)
    
    list after removing one element:  SortedList([6, 7, 9, 10], load=1000)
    
    list after removing all elements using clear:  SortedList([], load=1000)
    

## SortedSet –

Sorted set is a sorted mutable set in which values are unique and maintained
in sorted order. Sorted set uses a set for set-operations and maintains a
sorted list of values. Sorted set values must be hashable and comparable.

 **Functions to add and remove elements:**

>  **add(value) :** A function that takes one element as parameter and inserts
> it into the set by maintaining sorted order. _Runtime Complexity:_ O(log(n))
>
>  **clear()** : Remove all values from sorted set. _Runtime complexity:_ O(n)
>
>  **discard(value)** : Remove value from sorted set if it is a member. If
> value is not a member, do nothing. _Runtime complexity:_ O(log(n))

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from sortedcontainers import SortedList, SortedSet, SortedDict

 

# initializing a sorted set with parameters

# it takes an iterable as an argument

sorted_set = SortedSet([1, 1, 2, 3, 4])

 

# initializing a sorted set using default constructor

sorted_set = SortedSet()

 

# inserting values one by one

for i in range(5, 0, -1):

 sorted_set.add(i)

 

print('set after adding elements: ', sorted_set)

 

# inserting duplicate value

sorted_set.add(5)

 

print('set after inserting duplicate element: ', sorted_set)

 

# discarding an element

sorted_set.discard(4)

 

print('set after discarding: ', sorted_set)

 

# checking membership using 'in' operator

if(2 in sorted_set):

 print('2 is present')

else:

 print('2 is not present')

 

print('set elements are: ', end = '')

 

# iterating through a sorted set

for i in sorted_set:

 print(i, end = ' ')

print()  
  
---  
  
 __

 __

 **Output :**

    
    
    set after adding elements:  SortedSet([1, 2, 3, 4, 5], key=None, load=1000)
    
    set after inserting duplicate element:  SortedSet([1, 2, 3, 4, 5], key=None, load=1000)
    
    set after discarding:  SortedSet([1, 2, 3, 5], key=None, load=1000)
    
    2 is present
    
    set elements are: 1 2 3 5
    

### SortedDict –

Sorted dict is a sorted mutable mapping in which keys are maintained in sorted
order. Sorted dict inherits from dict to store items and maintains a sorted
list of keys. Sorted dict keys must be hashable and comparable.

 **Functions to add and remove elements:**

>  **setdefault(key, default = None)** : Return value for item identified by
> key in sorted dict. If key is in the sorted dict then return its value. If
> key is not in the sorted dict then insert key with value default and return
> default. _Runtime Complexity:_ O(log(n))
>
>  **clear()** : Remove all values from sorted dict. _Runtime complexity:_
> O(n)
>
>  **get(key, default)** : Return the value for key if key is in the
> dictionary, else default.

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from sortedcontainers import SortedList, SortedSet, SortedDict

 

# initializing a sorted dict with parameters

# it takes a dictionary object as a parameter

sorted_dict = SortedDict({'a': 1, 'b': 2, 'c':
3})

 

# initializing a sorted dict

sorted_dict = SortedDict({'a': 1, 'c': 2,
'b':3})

 

# print the dict

print('sorted dict is: ', sorted_dict)

 

# adding key => value pairs

sorted_dict['d'] = 3

 

print('sorted dict after adding an element: ', sorted_dict)

 

# adding element using setdefault()

sorted_dict.setdefault('e', 4)

 

print('sorted dict after setdefault(): ', sorted_dict)

 

# using the get function

print('using the get function to print the value of a: ',
sorted_dict.get('a', 0))

 

# checking membership using 'in' operator

if('a' in sorted_dict):

 print('a is present')

else:

 print('a is not present')

 

print('dict elements are: ', end = '')

 

# iterating over key => value pairs in a dictionary

for key in sorted_dict:

 print('{} -> {}'.format(key, sorted_dict[key]), end = '
')

print()

 

# removing all elements from the dict

sorted_dict.clear()

 

print('sorted dict after removing all elements: ', sorted_dict)  
  
---  
  
 __

 __

 **Output :**

    
    
    sorted dict is:  SortedDict(None, 1000, {'a': 1, 'b': 3, 'c': 2})
    
    sorted dict after adding an element:  SortedDict(None, 1000, {'a': 1, 'b': 3, 'c': 2, 'd': 3})
    
    sorted dict after setdefault():  SortedDict(None, 1000, {'a': 1, 'b': 3, 'c': 2, 'd': 3, 'e': 4})
    
    using the get function to print the value of a:  1
    
    a is present
    
    dict elements are: a -> 1 b -> 3 c -> 2 d -> 3 e -> 4 
    
    sorted dict after removing all elements:  SortedDict(None, 1000, {})
    

Reference: http://www.grantjenks.com/docs/sortedcontainers/index.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

