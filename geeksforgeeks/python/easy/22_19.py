Python Lists



 **Lists** are just like dynamic sized arrays, declared in other languages
(vector in C++ and ArrayList in Java). Lists need not be homogeneous always
which makes it a most powerful tool in Python. A single list may contain
DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and
hence, they can be altered even after their creation.

List in Python are ordered and have a definite count. The elements in a list
are indexed according to a definite sequence and the indexing of a list is
done with 0 being the first index. Each element in the list has its definite
place in the list, which allows duplicating of elements in the list, with each
element having its own distinct place and credibility.

 **Note-** Lists are a useful tool for preserving a sequence of data and
further iterating over it.

>  **Table of content:**
>
>   * Creating a List
>   * Knowing the size of List
>   * Adding Elements to a List:
>     * Using append() method
>     * Using insert() method
>     * Using extend() method
>   * Accessing elements from the List
>   * Removing Elements from the List:
>     * Using remove() method
>     * Using pop() method
>   * Slicing of a List
>   * List Comprehension
>   * Operations on List
>   * List Methods
>

# Creating a List

Lists in Python can be created by just placing the sequence inside the square
brackets[]. Unlike Sets, list doesn’t need a built-in function for creation of
list.

  

  

 **Note –** Unlike Sets, list may contain mutable elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Creation of List 

 

# Creating a List

List = []

print("Blank List: ")

print(List)

 

# Creating a List of numbers

List = [10, 20, 14]

print("\nList of numbers: ")

print(List)

 

# Creating a List of strings and accessing

# using index

List = ["Geeks", "For", "Geeks"]

print("\nList Items: ")

print(List[0]) 

print(List[2])

 

# Creating a Multi-Dimensional List

# (By Nesting a list inside a List)

List = [['Geeks', 'For'] , ['Geeks']]

print("\nMulti-Dimensional List: ")

print(List)  
  
---  
  
 __

 __

 **Output:**

    
    
    Blank List: 
    []
    
    List of numbers: 
    [10, 20, 14]
    
    List Items
    Geeks
    Geeks
    
    Multi-Dimensional List: 
    [['Geeks', 'For'], ['Geeks']]
    

### Creating a list with multiple distinct or duplicate elements

A list may contain duplicate values with their distinct positions and hence,
multiple distinct or duplicate values can be passed as a sequence at the time
of list creation.

 __

 __  
 __

 __

 __  
 __  
 __

# Creating a List with

# the use of Numbers

# (Having duplicate values)

List = [1, 2, 4, 4, 3, 3, 3, 6, 5]

print("\nList with the use of Numbers: ")

print(List)

 

# Creating a List with 

# mixed type of values

# (Having numbers and strings)

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

print("\nList with the use of Mixed Values: ")

print(List)  
  
---  
  
 __

 __

 **Output:**

    
    
    List with the use of Numbers: 
    [1, 2, 4, 4, 3, 3, 3, 6, 5]
    
    List with the use of Mixed Values: 
    [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
    

# Knowing the size of List

 __

 __  
 __

 __

 __  
 __  
 __

# Creating a List

List1 = []

print(len(List1))

 

# Creating a List of numbers

List2 = [10, 20, 14]

print(len(List2))  
  
---  
  
 __

 __

 **Output:**

    
    
    0
    3
    

# Adding Elements to a List

### Using append() method

Elements can be added to the List by using built-in **append()** function.
Only one element at a time can be added to the list by using append()
method, for addition of multiple elements with the append() method, loops
are used. Tuples can also be added to the List with the use of append method
because tuples are immutable. Unlike Sets, Lists can also be added to the
existing list with the use of append() method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Addition of elements in a List

 

# Creating a List

List = []

print("Initial blank List: ")

print(List)

 

# Addition of Elements 

# in the List

List.append(1)

List.append(2)

List.append(4)

print("\nList after Addition of Three elements: ")

print(List)

 

# Adding elements to the List

# using Iterator

for i in range(1, 4):

 List.append(i)

print("\nList after Addition of elements from 1-3: ")

print(List)

 

# Adding Tuples to the List

List.append((5, 6))

print("\nList after Addition of a Tuple: ")

print(List)

 

# Addition of List to a List

List2 = ['For', 'Geeks']

List.append(List2)

print("\nList after Addition of a List: ")

print(List)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial blank List: 
    []
    
    List after Addition of Three elements: 
    [1, 2, 4]
    
    List after Addition of elements from 1-3: 
    [1, 2, 4, 1, 2, 3]
    
    List after Addition of a Tuple: 
    [1, 2, 4, 1, 2, 3, (5, 6)]
    
    List after Addition of a List: 
    [1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]
    

### Using insert() method

append() method only works for addition of elements at the end of the List,
for addition of element at the desired position, insert() method is used.
Unlike append() which takes only one argument, insert() method requires
two arguments(position, value).

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Addition of elements in a List

 

# Creating a List

List = [1,2,3,4]

print("Initial List: ")

print(List)

 

# Addition of Element at 

# specific Position

# (using Insert Method)

List.insert(3, 12)

List.insert(0, 'Geeks')

print("\nList after performing Insert Operation: ")

print(List)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial List: 
    [1, 2, 3, 4]
    
    List after performing Insert Operation: 
    ['Geeks', 1, 2, 3, 12, 4]
    

### Using extend() method

Other than append() and insert() methods, there’s one more method for
Addition of elements, **extend()**, this method is used to add multiple
elements at the same time at the end of the list.

 **Note –**append() and extend() methods can only add elements at the end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Addition of elements in a List

 

# Creating a List

List = [1,2,3,4]

print("Initial List: ")

print(List)

 

# Addition of multiple elements

# to the List at the end

# (using Extend Method)

List.extend([8, 'Geeks', 'Always'])

print("\nList after performing Extend Operation: ")

print(List)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial List: 
    [1, 2, 3, 4]
    
    List after performing Extend Operation: 
    [1, 2, 3, 4, 8, 'Geeks', 'Always']
    

# Accessing elements from the List

In order to access the list items refer to the index number.Use the index
operator [ ] to access an item in a list.The index must be an integer.Nested
list are accessed using nested indexing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# accessing of element from list

 

# Creating a List with

# the use of multiple values

List = ["Geeks", "For", "Geeks"]

 

# accessing a element from the 

# list using index number

print("Accessing a element from the list")

print(List[0]) 

print(List[2])

 

# Creating a Multi-Dimensional List

# (By Nesting a list inside a List)

List = [['Geeks', 'For'] , ['Geeks']]

 

# accessing an element from the 

# Multi-Dimensional List using

# index number

print("Acessing a element from a Multi-Dimensional list")

print(List[0][1])

print(List[1][0])  
  
---  
  
 __

 __

 **Output:**

    
    
    Accessing a element from the list
    Geeks
    Geeks
    Acessing a element from a Multi-Dimensional list
    For
    Geeks
    

### Negative indexing

In Python, negative sequence indexes represent positions from the end of the
array. Instead of having to compute the offset as in List[len(List)-3], it
is enough to just write List[-3]. Negative indexing means beginning from the
end, -1 refers to the last item, -2 refers to the second-last item, etc.

 __

 __  
 __

 __

 __  
 __  
 __

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

 

# accessing a element using

# negative indexing

print("Accessing element using negative indexing")

 

# print the last element of list

print(List[-1])

 

# print the third last element of list 

print(List[-3])  
  
---  
  
 __

 __

 **Output:**

    
    
    Accessing element using negative indexing
    Geeks
    For
    

# Removing Elements from the List

### Using remove() method

Elements can be removed from the List by using built-in **remove()**

