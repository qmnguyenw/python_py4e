Sets in Python



A Set is an unordered collection data type that is iterable, mutable and has
no duplicate elements. Python’s set class represents the mathematical notion
of a set. The major advantage of using a set, as opposed to a list, is that it
has a highly optimized method for checking whether a specific element is
contained in the set. This is based on a data structure known as a hash table.
Since sets are unordered, we cannot access items using indexes like we do in
lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate sets

 

# Same as {"a", "b", "c"}

myset = set(["a", "b", "c"])

print(myset)

 

# Adding element to the set

myset.add("d")

print(myset)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'c', 'b', 'a'}
    {'d', 'c', 'b', 'a'}
    

## Frozen Sets

 **Frozen sets** in Python are immutable objects that only support methods and
operators that produce a result without affecting the frozen set or sets to
which they are applied. While elements of a set can be modified at any time,
elements of the frozen set remain the same after creation.  
If no parameters are passed, it returns an empty frozenset.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate differences

# between normal and frozen set

 

# Same as {"a", "b","c"}

normal_set = set(["a", "b","c"])

 

print("Normal Set")

print(normal_set)

 

# A frozen set

frozen_set = frozenset(["e", "f", "g"])

 

print("\nFrozen Set")

print(frozen_set)

 

# Uncommenting below line would cause error as

# we are trying to add element to a frozen set

# frozen_set.add("h")  
  
---  
  
 __

 __

 **Output:**

    
    
    Normal Set
    set(['a', 'c', 'b'])
    
    Frozen Set
    frozenset(['e', 'g', 'f'])
    

## Internal working of Set

This is based on a data structure known as a hash table.  
If Multiple values are present at the same index position, then the value is
appended to that index position, to form a Linked List. In, Python Sets are
implemented using dictionary with dummy variables, where key beings the
members set with greater optimizations to the time complexity.

  

  

 **Set Implementation:-**

![](https://media.geeksforgeeks.org/wp-content/uploads/HashTable-300x278.png)

Sets with Numerous operations on a single HashTable:-

![](https://media.geeksforgeeks.org/wp-content/uploads/Hasing-Python.png)  

## Methods for Sets

#### Adding elements

Insertion in set is done through set.add() function, where an appropriate
record value is created to store in the hash table. Same as checking for an
item, i.e., O(1) on average. However, in worst case it can become O(n).

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to

# demonstrate adding elements

# in a set

 

# Creating a Set

people = {"Jay", "Idrish", "Archi"}

 

print("People:", end = " ")

print(people)

 

# This will add Daxit

# in the set

people.add("Daxit")

 

# Adding elements to the

# set using iterator

for i in range(1, 6): 

 people.add(i) 

 

print("\nSet after adding element:", end = " ")

print(people)  
  
---  
  
 __

 __

 **Output:**

    
    
    People: {'Idrish', 'Archi', 'Jay'}
    
    Set after adding element: {1, 2, 3, 4, 5, 'Idrish', 'Archi', 'Jay', 'Daxit'}
    

#### Union

Two sets can be merged using union() function or | operator. Both Hash Table
values are accessed and traversed with merge operation perform on them to
combine the elements, at the same time duplicates are removed. Time Complexity
of this is O(len(s1) + len(s2)) where s1 and s2 are two sets whose union needs
to be done.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to

# demonstrate union of

# two sets

 

people = {"Jay", "Idrish", "Archil"}

vampires = {"Karan", "Arjun"}

dracula = {"Deepanshu", "Raju"}

 

# Union using union()

# function

population = people.union(vampires)

 

print("Union using union() function")

print(population)

 

# Union using "|"

# operator

population = people|dracula

 

print("\nUnion using '|' operator")

print(population)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Union using union() function
    {'Karan', 'Idrish', 'Jay', 'Arjun', 'Archil'}
    
    Union using '|' operator
    {'Deepanshu', 'Idrish', 'Jay', 'Raju', 'Archil'}
    

