Comparison between Lists and Array in Python



Python programming language has four collection data types namely **List,
Tuple, Set, and Dictionary**. A list is a mutable and ordered collection i.e.,
elements of the list can be changed and it maintains the order of insertion of
its items. Because of the property of order maintaining, each element of the
list has a fixed index and it permits the list to have duplicate elements. In
Python, list is very useful as it has the ability to contain non-homogeneous
elements.

Following are some operations which can be performed on the list:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# some operations on list

 

# Declaring a List of integers 

IntList = [10, 20, 30] 

print("List of numbers: ")

 

# Printing the list 

print(IntList) 

 

# Declaring a List of strings

StrList = ["Geeks", "For", "Geeks"] 

print("List of Strings: ")

 

# Printing the list 

print(StrList) 

 

# Declaring a list of non-homogeneous elements

Non_homogeneous_list = [10, "Geeks", 20.890,\

 "for", 30, "geeks"]

print("List of non-homogeneous elements: ")

 

# Printing the list

print(Non_homogeneous_list)

 

# Printing size of a list

print("Size of the Non-homogeneous list: ",\

 len(Non_homogeneous_list))

 

# Declaring a list

NewList = ["Geeks", "for", "Geeks"]

print("Original List: ", NewList)

 

# Adding an item to the list

 

# Adding an item in the list 

# using the append method

NewList.append("the")

 

# Printing the modified list

print("After adding an element the"\

 "list becomes: ")

print(NewList)

 

# Adding an item in the list using the insert 

# method to add an element at a specific position

NewList.insert(3, "is")

 

# Printing the modified list

print("After adding an element at"\

 "index 3 the list becomes: ")

print(NewList) 

 

# Adding multiple items to the list at the

# end using extend method

NewList.extend(["best", "CS", "website"]) 

 

# Printing the modified list

print("After adding 3 elements at the"\

 "end, the list becomes: ")

print(NewList)

 

# Removing an item from the list

 

# Removing an element by 

# writing the element itself

NewList.remove("the")

 

# Printing the modified list

print("After removing an element"\

 "the list becomes: ")

print(NewList)

 

# Removing an element by 

# specifying its position

NewList.pop(3)

 

# Printing the modified list

print("After removing an element "\

 "from index 3 the list becomes: ")

print(NewList)  
  
---  
  
 __

 __

 **Output:**

    
    
    List of numbers: 
    [10, 20, 30]
    List of Strings: 
    ['Geeks', 'For', 'Geeks']
    List of non-homogeneous elements: 
    [10, 'Geeks', 20.89, 'for', 30, 'geeks']
    Size of the Non-homogeneous list:  6
    Original List:  ['Geeks', 'for', 'Geeks']
    After adding an element thelist becomes: 
    ['Geeks', 'for', 'Geeks', 'the']
    After adding an element atindex 3 the list becomes: 
    ['Geeks', 'for', 'Geeks', 'is', 'the']
    After adding 3 elements at theend, the list becomes: 
    ['Geeks', 'for', 'Geeks', 'is', 'the', 'best', 'CS', 'website']
    After removing an elementthe list becomes: 
    ['Geeks', 'for', 'Geeks', 'is', 'best', 'CS', 'website']
    After removing an element from index 3 the list becomes: 
    ['Geeks', 'for', 'Geeks', 'best', 'CS', 'website']
    

To get more in-depth knowledge about python list click here.

### Python Array

Python arrays are also a collection but its items are stored at contiguous
memory locations. It can store only homogeneous elements(elements of the same
data type). Arrays are very beneficial in performing mathematical operations
on the elements. Unlike lists, arrays can not be declared directly. To create
an array the array module must be imported and the syntax of the declaration
is different from that of the list.

  

  

Following are some operations which can be performed on the array:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# some operations on arrays

 

# importing array module 

import array as arr

 

# declaring an array of integer type

# 'i' signifies integer type and

# elements inside [] are the array elements 

a1 = arr.array('i', [10, 20, 30])

 

# printing array with 

# data type and elements

print("Array a1: ", a1)

 

# printing elements of array

print ("Elements of the array"\

 "a1 is : ", end = " ") 

for i in range (len(a1)): 

 print (a1[i], end =", ")

print()

 

# Declaring an array of float type

# 'd' signifies integer type and

# elements inside [] are the array elements 

a2 = arr.array('d', [1.5, 2.4, 3.9])

 

# printing elements of array

print ("Elements of the array"\

 "a2 is : ", end = " ") 

for i in range (len(a2)): 

 print (a2[i], end =", ")

print()

 

# Adding an item to the array

 

# Printing the elements of array a1

print ("Original elements of the"\

 "array a1 is : ", end = " ") 

print(*a1)

 

# Adding an element at the end of

# array by using the append method

a1.append(40)

 

# printing the modified array

print ("Elements of the array a1"\

 "after adding an element"\

 "at last: ", end = " ")

print(*a1)

 

# Adding an element to the array at a 

# specific index using the insert method

a1.insert(3, 35)

 

# printing the modified array

print ("Elements of the array a1"\

 "after adding an element"\

 "at index 3: ", end = " ")

print(*a1)

 

# Removing an element from the array

 

# Removing an element by writing the elements itself

a1.remove(20)

 

# Printing the modified array

print("Array a1 after removing"\

 "element 20: ", end = " ")

print(*a1)

 

# Removing an element of a specific index

# Removing the element of array a1 present at index 2

a1.pop(2)

 

# Printing the modified array

print("Array a1 after removing"\

"element of index 2: ", end = " ")

print(*a1)  
  
---  
  
 __

 __

 **Output:**

    
    
    Array a1:  array('i', [10, 20, 30])
    Elements of the arraya1 is :  10, 20, 30, 
    Elements of the arraya2 is :  1.5, 2.4, 3.9, 
    Original elements of thearray a1 is :  10 20 30
    Elements of the array a1after adding an elementat last:  10 20 30 40
    Elements of the array a1after adding an elementat index 3:  10 20 30 35 40
    Array a1 after removingelement 20:  10 30 35 40
    Array a1 after removingelement of index 2:  10 30 40
    

To get more in-depth knowledge about python array click here.

### Similarities in Python list and array

 **Both array and lists are used for storing the data:** The purpose of both
the collection is to store the data. While the list is used to store
homogeneous as well as non-homogeneous data, an array can store only
homogeneous data.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate data

# storing similarities in array and list

 

# importing array module 

import array as arr

 

# Declaring a Homogeneous List of strings

Homogeneous_List = ["Geeks", "For", "Geeks"] 

print("List of Strings: ")

 

# Printing the list 

print(Homogeneous_List) 

 

# Declaring a list of 

# non-homogeneous elements

Non_homogeneous_list = [10, "Geeks",\

 20.890, "for", 30, "geeks"]

print("List of non-homogeneous elements: ")

 

# Printing the list

print(Non_homogeneous_list)

 

# declaring an array of float type

# 'd' signifies integer type and

# elements inside [] are the array elements 

Homogeneous_array = arr.array('d',\

 [1.5, 2.4, 3.9])

 

# printing elements of array

print ("Elements of the array is"\

 " : ", end = " ") 

for i in range (len(Homogeneous_array)): 

 print (Homogeneous_array[i], end =", ")  
  
---  
  
 __

 __

 **Output:**

    
    
    List of Strings: 
    ['Geeks', 'For', 'Geeks']
    List of non-homogeneous elements: 
    [10, 'Geeks', 20.89, 'for', 30, 'geeks']
    Elements of the array is :  1.5, 2.4, 3.9,
    

**List and Array both are mutable:** List, as well as the array, have the
ability to modify their elements i.e., they are mutable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# both the list and array is mutable

 

# importing array module 

import array as arr

 

# Declaring a list

List1 = ["Geeks", 1, "Geeks"]

 

# Printing original list

print("Original list: ", List1)

 

# Changing the value of the 

# element at a specific index

List1[1] = "for"

 

# Printing modified list

print("\nModified list: ", List1)

 

# Declaring an array with integers values

Array1 = arr.array('i', \

 [10, 20, 30, 37, 50, ]) 

 

# Printing original array 

print ("\nOriginal array: ", end =" ") 

for i in range (len(Array1)): 

 print (Array1[i], end =" ") 

 

 

# Updating an element in the array 

Array1[3] = 40

 

# Printing modified Array:

print("\nModified array: ", end ="") 

for i in range (len(Array1)): 

 print (Array1[i], end =" ")   
  
---  
  
__

__

**Output:**

    
    
    Original list:  ['Geeks', 1, 'Geeks']
    
    Modified list:  ['Geeks', 'for', 'Geeks']
    
    Original array:  10 20 30 37 50 
    Modified array: 10 20 30 40 50
    

**Elements of both list and array can be accessed by index and iteration:** In
order to access the elements of list and array, we have the option of using
index number or we can traverse them by iteration.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# that elements of list and array can

# be accessed through index and iteration

 

# importing array module 

import array as arr

 

# Declaring a list 

List1 = [10, 20, 30, 20, 10, 40]

 

# Printing the list

print("List1 elements: ", List1, "\n")

 

# Accessing elements of list by index number

print("Element at index 0: ", List1[0])

print("Element at index 1: ", List1[1])

print("Element at index 3: ", List1[3])

print("Element at index 4: ", List1[4])

 

# Accessing elements of the list

# using negative indexing

 

# Printing last element of the list

print("Element at last index: ", List1[-1])

 

# Printing 3rd last 

# the element of the list

print("Element at "\

 "3rd last index: ", List1[-3])

 

# Accessing elements of list through iteration

print("Accessing through iteration: ", end = " ")

for item in range(len(List1)):

 print(List1[item], end =" ")

 

 

# Declaring an array

Array1 = arr.array('i',\

[10, 20, 30, 40, 50, 60])

print("\nArray1: ", Array1)

 

# Accessing the elements of an array

 

# Access element of 

# array by index number

print("Element of Array1"\

 " at index 3: ", Array1[3])

 

# Accessing elements of 

# array through iteration

print("Accessing through iteration:"\

 " ", end = " ")

for i in range (len(Array1)): 

 print (Array1[i], end =" ")  
  
---  
  
 __

 __

 **Output:**

    
    
    List1 elements:  [10, 20, 30, 20, 10, 40] 
    
    Element at index 0:  10
    Element at index 1:  20
    Element at index 3:  20
    Element at index 4:  10
    Element at last index:  40
    Element at 3rd last index:  20
    Accessing through iteration:  10 20 30 20 10 40 
    Array1:  array('i', [10, 20, 30, 40, 50, 60])
    Element of Array1 at index 3:  40
    Accessing through iteration:  10 20 30 40 50 60
    

**List and array both can be sliced:** Slicing operation is valid for both the
list and array to get a range of elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# that both list and array can

# be accessed sliced

 

# importing array module 

import array as arr

 

# Declaring a list 

List1 = [10, 20, 30, 20, 10, 40]

 

# Accessing a range of elements in the 

# list using slicing operation

 

# Printing items of the list

# from index 1 to 3 

print("List elements from "\

 "index 1 to 4: ", List1[1:4])

 

# Printing items of the 

# list from index 2 to end

print("List elements from "\

"index 2 to last: ", List1[2:])

 

# Declaring an array

Array1 = arr.array('i', 

 [10, 20, 30, 40, 50, 60])

 

# Accessing a range of elements in the 

# array using slicing operation

Sliced_array1 = Array1[1:4] 

print("\nSlicing elements of the "\

"array in a\nrange from index 1 to 4: ") 

print(Sliced_array1) 

 

# Print elements of the array 

# from a defined point to end 

Sliced_array2 = Array1[2:] 

print("\nSlicing elements of the "\

"array from\n2nd index till the end: ") 

print(Sliced_array2)   
  
---  
  
__

__

**Output:**

    
    
    List elements from index 1 to 4:  [20, 30, 20]
    List elements from index 2 to last:  [30, 20, 10, 40]
    
    Slicing elements of the array in a
    range from index 1 to 4: 
    array('i', [20, 30, 40])
    
    Slicing elements of the array from
    2nd index till the end: 
    array('i', [30, 40, 50, 60])
    

### Differences between the Python list and array:

 **Difference in creation:** Unlike list which is a part of Python syntax, an
array can only be created by importing the array module. A list can be created
by simply putting a sequence of elements around a square bracket. All the
above codes are the proofs of this difference.

 **Memory consumption between array and lists:** List and array take a
different amount of memory even if they store the same amount of elements.
Arrays are found to be more efficient in this case as they store data in a
very compact manner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# difference in memory consumption 

# of list and array

 

# importing array module 

import array as arr

 

# importing system module 

import sys 

 

# declaring a list of 1000 elements 

List = range(1000) 

 

# printing size of each element of the list 

print("Size of each element of"\

" list in bytes: ", sys.getsizeof(List)) 

 

# printing size of the whole list 

print("Size of the whole list in"\

" bytes: ", sys.getsizeof(List)*len(List)) 

 

# declaring an array of 1000 elements 

Array = arr.array('i', [1]*1000) 

 

# printing size of each 

# element of the Numpy array 

print("Size of each element of "\

"the array in bytes: ", Array.itemsize) 

 

# printing size of the whole Numpy array 

print("Size of the whole array"\

" in bytes: ", len(Array)*Array.itemsize)   
  
---  
  
__

__

**Output:**

    
    
    Size of each element of list in bytes:  48
    Size of the whole list in bytes:  48000
    Size of each element of the array in bytes:  4
    Size of the whole array in bytes:  4000
    

**Performing mathematical operations:** Mathematical operations like dividing
or adding each element of the collection with a certain number can be carried
out in arrays but lists do not support these kinds of arithmetic operations.
Arrays are optimized for this purpose while to carry out these operations in
the list, operations have to be applied to every element separately.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# difference between list and array in 

# carrying out mathematical operations

 

# importing array module 

from numpy import array

 

# declaring a list 

List =[1, 2, 3] 

 

# declaring an array 

Array = array([1, 2, 3])

 

try: 

 # adding 5 to each element of list 

 List = List + 5

 

except(TypeError): 

 print("Lists don't support list + int") 

 

# for array

try: 

 

 Array = Array + 5

 

 # printing the array 

 print("Modified array: ", Array) 

 

except(TypeError): 

 print("Arrays don't support list + int")   
  
---  
  
__

__

**Output:**

    
    
    Lists don't support list + int
    Modified array:  [6 7 8]
    

**Resizing:** Arrays once declared can not be resized. The only way is to copy
the elements of the older array into a larger sized array. While the list can
be re-sized very efficiently.

 **Data that can be stored:** List can store both homogeneous as well as non-
homogeneous data while arrays support the storage of only homogeneous data.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

