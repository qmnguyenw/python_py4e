Different ways of sorting Dictionary by Values and Reverse sorting by values



 **Prerequisite:** Dictionaries in Python

A dictionary is a collection which is unordered, changeable, and indexed. In
Python, dictionaries are written with curly brackets, and they have keys and
values. We can access the values of the dictionary using keys. In this
article, 10 different ways of sorting the Python dictionary by values and also
reverse sorting by values are discussed.

 ** _Using lambda function along with items() and sorted()_ :** The **lambda
function** returns the key(0th element) for a specific item tuple, When these
are passed to the sorted() method, it returns a sorted sequence which is then
type-casted into a dictionary. **keys()** method returns a view object that
displays a list of all the keys in the dictionary. **sorted()** is used to
sort the keys of the dictionary.

 **Examples:**

>  **Input:** my_dict = {2: ‘three’, 1: ‘two’}  
> **Output:** [(2, ‘three’), (1, ‘two’)]
>
>  
>
>
>  
>

Below is the implementation using lambda function:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort dictionary

# by value using lambda function

# Initialize a dictionary

my_dict = {2: 'three',

 1: 'two'}

# Sort the dictionary

sorted_dict = sorted(

 my_dict.items(),

 key = lambda kv: kv[1])

# Print sorted dictionary

print("Sorted dictionary is :",

 sorted_dict)  
  
---  
  
 __

 __

 **Output**

    
    
    Sorted dictionary is : [(2, 'three'), (1, 'two')]
    

**_Using items() alone_ :** The method items() is used alone with two
variables i.e., key and value to sort the dictionary by value.

 **Examples:**

>  **Input:** my_dict = {‘c’: 3, ‘a’: 1, ‘d’: 4, ‘b’: 2}  
>  **Output:** [(1, ‘a’), (2, ‘b’), (3, ‘c’), (4, ‘d’)]  
>

Below is the implementation using method items():

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort dictionary

# by value using item function

# Initialize a dictionary

my_dict = {'c': 3,

 'a': 1,

 'd': 4,

 'b': 2}

# Sorting dictionary

sorted_dict = sorted([(value, key)

 for (key, value) in my_dict.items()])

# Print sorted dictionary

print("Sorted dictionary is :")

print(sorted_dict)  
  
---  
  
 __

 __

 **Output**

    
    
    Sorted dictionary is :
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    

**_Using sorted() and get()_ :** The method get() returns the value for the
given key, if present in the dictionary. If not, then it will return **None**.

  

  

 **Examples:**

>  **Input:** my_dict = {‘red’:’#FF0000′, ‘green’:’#008000′,
> ‘black’:’#000000′, ‘white’:’#FFFFFF’}  
> **Output:**  
> black #000000  
> green #008000  
> red #FF0000  
> white #FFFFFF

Below is the implementation using sorted() and get() method:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort dictionary

# by value using sorted() and get()

# Initialize a dictionary

my_dict = {'red': '# FF0000', 'green': '# 008000',

 'black': '# 000000', 'white': '# FFFFFF'}

# Sort and print dictionary

print("Sorted dictionary is :")

for w in sorted(my_dict, key = my_dict.get):

 print(w, my_dict[w])  
  
---  
  
 __

 __

 **Output**

    
    
    Sorted dictionary is :
    black # 000000
    green # 008000
    red # FF0000
    white # FFFFFF
    

**_Using itemgetter from operator_ :**

The method itemgetter(n) constructs a callable that assumes an iterable object
as input, and fetches the n-th element out of it.

 **Examples**

>  **Input:**  
> my_dict = {‘a’: 23, ‘g’: 67, ‘e’: 12, 45: 90}  
> **Output:**  
> [(‘e’, 12), (‘a’, 23), (‘g’, 67), (45, 90)]  
>

Below is the python program to sort the dictionary using itemgetter():

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort dictionary

# by value using itemgetter() function

# Importing OrderedDict

import operator

# Initialize a dictionary

my_dict = {'a': 23,

 'g': 67,

 'e': 12,

 45: 90}

# Sorting dictionary

sorted_dict = sorted(my_dict.items(), \

 key = operator.itemgetter(1))

# Printing sorted dictionary

print("Sorted dictionary is :")

print(sorted_dict)  
  
---  
  
 __

 __

 **Output**

    
    
    Sorted dictionary is :
    [('e', 12), ('a', 23), ('g', 67), (45, 90)]
    

**_Using OrderedDict from collections_ :** The OrderedDict is a standard
library class, which is located in the collections module. OrderedDict
maintains the orders of keys as inserted.

 **Examples:**

>  **Input:** my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}  
> **Output:** [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]  
>

Below is the implementation using Ordered Dict:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort dictionary

# by value using OrderedDict

# Import OrderedDict

from collections import OrderedDict

# Initialize a dictionary

my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0:
0}

# Sort dictionary

sorted_dict = OrderedDict(sorted(\

 my_dict.items(), key = lambda x: x[1]))

# Print the sorted dictionary

print("Sorted dcitonary is :")

print(sorted_dict)  
  
---  
  
 __

 __

 **Output**

    
    
    Sorted dcitonary is :
    OrderedDict([(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)])
    

**_Using_** ** _Counter from collections_** **:** The counter is an unordered
collection where elements are stored as Dict keys and their count as dict
value. Counter elements count can be positive, zero or negative integers.

 **Examples:**

> **Input:** my_dict = {‘hello’: 1, ‘python’: 5, ‘world’: 3}  
>  **Output:** [(‘hello’, 1), (‘world’, 3), (‘python’, 5)]  
>

Below is the implementation using Counter from collections:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort dictionary

# by value using OrderedDict

# Import Counter

from collections import Counter

# Initialize a dictionary

my_dict = {'hello': 1, 'python': 5, 'world': 3}

# Sort and print the dictionary

sorted_dict = Counter(my_dict)

print("Sorted dictionary is :")

print(sorted_dict.most_common()[::-1])  
  
---  
  
 __

 __

 **Output**

    
    
    Sorted dictionary is :
    [('hello', 1), ('world', 3), ('python', 5)]
    

**_Reverse Sorting Dictionary by values_ :** The same syntax for both
ascending and descending ordered sorting. For reverse sorting, the idea is to
use **reverse = true.** with the function **sorted()**.

 **Examples:**

>  **Input:**  
> my_dict = {‘red’:’#FF0000′,  
> ‘green’:’#008000′,  
> ‘black’:’#000000′,  
> ‘white’:’#FFFFFF’}  
> **Output:**  
> black #000000  
> green #008000  
> red #FF0000  
> white #FFFFFF  
>

Below is the implementation using Reverse Sorting Dictionary by values:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort dictionary

# by value using sorted setting

# reverse parameter to true

# Initialize a dictionary

my_dict = {'red': '# FF0000', 'green': '# 008000',

 'black': '# 000000', 'white': '# FFFFFF'}

# Sort and print the dictionary

print("Sorted dictionary is :")

for w in sorted(my_dict, key = my_dict.get, \

 reverse = True):

 print(w, my_dict[w])  
  
---  
  
 __

 __

 **Output**

    
    
    Sorted dictionary is :
    white # FFFFFF
    red # FF0000
    green # 008000
    black # 000000
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

