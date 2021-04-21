Advanced Python List Methods and Techniques



Lists are just like dynamically sized arrays, declared in other languages
(vector in C++ and ArrayList in Java). Lists need not be homogeneous always
which makes it a most powerful tool in Python. A single list may contain
DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and
hence, they can be altered even after their creation.

Lists are one of the most powerful tools in python. They have a lot of hidden
tricks which makes them extremely versatile. Let’s explore some of these
useful techniques which make our lives much easier !!!

###  **Sorting a list**

To sort a list in ascending or descending order, we use the _sort()_ function
with the following syntax:

    
    
     **For ascending order:** 
    list.sort()
    **For descending order:** 
    list.sort(reverse=True)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# sorting a list using sort() function

 

my_list = [5, 2, 90, 24, 10]

 

 

# sorting in ascending order it permanently 

# changes the order of the list

my_list.sort()

print(my_list)

 

# sorting in descending order it permanently 

# changes the order of the list

my_list.sort(reverse=True)

print(my_list)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [2, 5, 10, 24, 90]
    [90, 24, 10, 5, 2]

To temporarily change the order of the list use the _sorted()_ function with
the syntax:

    
    
    list.sorted()

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# temporary sorting using sorted() method

 

my_list = [5, 2, 90, 24, 10]

 

# ascending order

print(sorted(my_list))

 

# descending order

my_list_2 = sorted(my_list)

print(my_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 5, 10, 24, 90]
    [5, 2, 90, 24, 10]

###  **Reversing a list**

To reverse the order of a list we use the _reverse()_ function. Its syntax is:

    
    
    list.reverse()

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# reverse a list using reverse()

 

my_list = [5, 2, 90, 24, 10]

 

# reverse

my_list.reverse()

print(my_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 24, 90, 2, 5]

Or we could apply list comprehension to reverse a list:

    
    
     list = list[::-1]

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# reverse using list comprehension

my_list = [5, 2, 90, 24, 10]

 

# reverse

print(my_list[::-1])  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [10, 24, 90, 2, 5]

###  **Removing duplicates**

As dictionaries in python do not contain duplicate keys. We use the
_dict.fromkeys()_ function to convert our list into a dictionary with list
elements as keys. And then we convert the dictionary back to list.

This is a powerful trick to automatically remove all the duplicates. Its
syntax is:

    
    
    My_list =[‘a’, ’b’, ’c’, ’b’, ’a’]
    Mylist = list(dict.fromkeys(My_List))

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# removig duplicates from a list using dictionaries

 

my_list_1 = [5, 2, 90, 24, 10, 2, 90,
34]

my_list_2 = ['a', 'a', 'a', 'b', 'c', 'd',
'd', 'e']

 

# removing duplicates from list 1

my_list_1 = list(dict.fromkeys(my_list_1))

print(my_list_1)

 

# removing duplicates from list 2

my_list_2 = list(dict.fromkeys(my_list_2))

print(my_list_2)  
  
---  
  
 __

 __

 **Output:**

    
    
    [5, 2, 90, 24, 10, 34]
    ['a', 'b', 'c', 'd', 'e']

### Filtering a list

Python lists can be filtered with the help of _filter()_ function or with the
help of list comprehension. Below is the syntax:

    
    
    My_list = list(filter(filter_function , iterable_item))

The Filter function returns an iterator object which we must convert back into
the list.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# filtering with the help of filer() function

# creating a filter function filter all the values less than 20

 

# filter function

def my_filter(n):

 if n > 20:

 return n

 

 

# driver code

if __name__ == "__main__":

 my_list = [5, 2, 90, 24, 10, 2, 95,
36]

 my_filtered_list = list(filter(my_filter, my_list))

 print(my_filtered_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [90, 24, 95, 36]

We can also filter using list comprehension. It is a much easier and elegant
way to filter lists, below is the syntax:

    
    
    My_list = [item for item in my_list if (condition)]

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# filtering with the help of list comprehension

my_list = [5, 2, 90, 24, 10, 2, 95, 36]

 

# an elegant way to sort the list

my_list = [item for item in my_list if item > 20]

print(my_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [90, 24, 95, 36]

### Modifying list

To modify the values in the list with the help of an external function, we
make use of the map() function. Map() function returns a map object (iterator)
of the results after applying the given function to each element of a given
iterable(list, tuple etc.). Below is the syntax:

    
    
    My_list = list(map(function,iterable))

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# using map() function to modify the text

def squaring(n):

 return n**2

 

# driver code

if __name__ == "__main__":

 my_list = [5, 2, 90, 24, 10, 2, 95,
36]

 

 my_squared_list = list(map(squaring, my_list))

 print(my_squared_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [25, 4, 8100, 576, 100, 4, 9025, 1296]

A much cleaner approach is using list comprehension.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# the same result can be obtained by a much pythonic approach

# i.e., by using list comprehension

my_list = [5, 2, 90, 24, 10, 2, 95, 36]

 

print([i**2 for i in my_list])  
  
---  
  
 __

 __

 **Output:**

    
    
    [25, 4, 8100, 576, 100, 4, 9025, 1296]

### Combining lists

We can even combine lists with the help of the _zip()_ function which results
in a list of tuples. Here each item from list A is combined with corresponding
elements from list B in the form of a tuple. Below is the syntax:

    
    
    My_list = zip(list_1, list_2)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# combing lists with the help of zip() function

my_list_1 = [5, 2, 90, 24, 10]

my_list_2 = [6, 3, 91, 25, 12]

 

# combined

my_combined_list = list(zip(my_list_1, my_list_2))

print(my_combined_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [(5, 6), (2, 3), (90, 91), (24, 25), (10, 12)]

### Finding the most common item

To find the most frequent element we make use of the _set()_ function. The
_set()_ function removes all the duplicates from the list, and the _max()_
function returns the most frequent element (which is found with the help of
‘key’). The key is an optional single argument function. Below is the syntax:

    
    
    Most_frequent_value =max(set(my_list),key=mylist.count)

 **Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# to find the most frequent element from the list

my_list = ['a', 'a', 'a', 'b', 'c', 'd', 'd',
'e']

 

most_frequent_value = max(set(my_list), key=my_list.count)

 

print("The most common element is:", most_frequent_value)  
  
---  
  
 __

 __

 **Output:**

    
    
    The most common element is: a

### Checking for membership in a list

To check whether an item exists in a list, we use the _in_ statement.

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

my_list= ['a', 'a', 'a', 'b', 'c', 'd', 'd',
'e']

 

# to check whether 'c' is a member of my_list

# returns true if present

print('c' in my_list) 

 

# to check whether 'f' is a member of my_list

# returns false if not present

print('f' in my_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    False

### Flatten a list of lists

Sometimes we encounter a list where each element in itself is a list. To
convert a list of lists into a single list, we use list comprehension.

    
    
    my_list = [item  for List in list_of_lists for item in List ]

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# to flatten a list_of_lists by using list comprehension

list_of_lists = [[1, 2],

 [3, 4],

 [5, 6],

 [7, 8]]

 

# using list comprehension

my_list = [item for List in list_of_lists for item in
List]

print(my_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 3, 4, 5, 6, 7, 8]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

