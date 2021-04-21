Python – Difference between sorted() and sort()



Sorting means rearranging a given sequence of elements according to a
comparison operator on the elements. The comparison operator is used to decide
the new order of the element in the respective data structure.

 **For example:** The below list of characters is sorted in increasing order
of their ASCII values. That is, the character with lesser ASCII value will be
placed first than the character with higher ASCII value.

![python-sorting](https://media.geeksforgeeks.org/wp-
content/uploads/20191218193125/python-sorting.jpg)

In Python, sorting any sequence is very easy as it provides in-built methods
for sorting. Two such methods are sorted() and sort(). These two methods
are used for sorting but are quite different in their own way. Let’s have a
look at them one by one.

## sorted()

sorted() method sorts the given sequence either in ascending order or in
descending order and always return the a sorted list. This method doesnot
effect the original sequence.

  

  

>  **Syntax:** sorted(iterable, key, reverse=False)
>
>  **Parameters:**  
>  **Iterable:** sequence (list, tuple, string) or collection (dictionary,
> set, frozenset) or any other iterator that needs to be sorted.  
>  **Key(optional):** A function that would serve as a key or a basis of sort
> comparison.  
>  **Reverse(optional):** If set True, then the iterable would be sorted in
> reverse (descending) order, by default it is set as False.
>
>  **Return Type:** Returns a sorted list.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# sorted()

 

 

L = [1, 2, 3, 4, 5]

 

print("Sorted list:")

print(sorted(L))

 

print("\nReverse sorted list:")

print(sorted(L, reverse = True))

 

print("\nOriginal list after sorting:")

print(L)  
  
---  
  
 __

 __

 **Output:**

    
    
    Sorted list:
    [1, 2, 3, 4, 5]
    
    Reverse sorted list:
    [5, 4, 3, 2, 1]
    
    Original list after sorting:
    [1, 2, 3, 4, 5]
    

**Example 2:** Sorting different data types

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# sorted()

 

 

# List 

x = ['q', 'w', 'r', 'e', 't', 'y'] 

print(sorted(x)) 

 

# Tuple 

x = ('q', 'w', 'e', 'r', 't', 'y') 

print(sorted(x))

 

# String-sorted based on ASCII translations 

x = "python"

print(sorted(x)) 

 

# Dictionary 

x = {'q':1, 'w':2, 'e':3, 'r':4,
't':5, 'y':6} 

print(sorted(x)) 

 

# Set 

x = {'q', 'w', 'e', 'r', 't', 'y'} 

print(sorted(x))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['e', 'q', 'r', 't', 'w', 'y']
    ['e', 'q', 'r', 't', 'w', 'y']
    ['h', 'n', 'o', 'p', 't', 'y']
    ['e', 'q', 'r', 't', 'w', 'y']
    ['e', 'q', 'r', 't', 'w', 'y']
    

#### Using key parameter

This optional parameter key takes a function as it’s value. This key function
transforms each element before sorting, it takes the value and returns 1 value
which is then used within sort instead of the original value.

  

  

 **Example:** Let’s suppose we want to sort a List of string according to its
length. This can be done by passing the len() function as the value to the
key parameter. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# sorted()

 

 

L = ['aaaa', 'bbb', 'cc', 'd']

 

# sorted without key parameter

print(sorted(L))

print()

 

# sorted with key parameter

print(sorted(L, key = len))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['aaaa', 'bbb', 'cc', 'd']
    
    ['d', 'cc', 'bbb', 'aaaa']
    

## sort()

sort() function is very similar to sorted() but unlike sorted it returns
nothing and makes changes to the original sequence. Moreover, sort() is a
method of list class and can only be used with lists.

>  **Syntax:** List_name.sort(key, reverse=False)
>
>  **Parameters:**  
>  **key:** A function that serves as a key for the sort comparison.  
>  **reverse:** If true, the list is sorted in descending order.
>
>  **Return type:** None

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# sort()

 

 

# List of Integers 

numbers = [1, 3, 4, 2] 

 

# Sorting list of Integers 

numbers.sort() 

 

print(numbers) 

 

# List of Floating point numbers 

decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68] 

 

# Sorting list of Floating point numbers 

decimalnumber.sort() 

 

print(decimalnumber) 

 

# List of strings 

words = ["Geeks", "For", "Geeks"] 

 

# Sorting list of strings 

words.sort() 

 

print(words)   
  
---  
  
__

__

**Output:**

    
    
    [1, 2, 3, 4]
    [1.68, 2.0, 2.01, 3.28, 3.67]
    ['For', 'Geeks', 'Geeks']
    

**Example 2:** Sorting in reverse order.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# sort()

 

 

# List of Integers 

numbers = [1, 3, 4, 2] 

 

# Sorting list of Integers 

numbers.sort(reverse = True) 

 

print(numbers) 

 

# List of Floating point numbers 

decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68] 

 

# Sorting list of Floating point numbers 

decimalnumber.sort(reverse = True) 

 

print(decimalnumber) 

 

# List of strings 

words = ["Geeks", "For", "Geeks"] 

 

# Sorting list of strings 

words.sort(reverse = True) 

 

print(words)   
  
---  
  
__

__

**Output:**

    
    
    [4, 3, 2, 1]
    [3.67, 3.28, 2.01, 2.0, 1.68]
    ['Geeks', 'Geeks', 'For']
    

**Example 3:** Using key parameter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate sorting by user's

# choice 

 

# function to return the second element of the 

# two elements passed as the parameter 

def sortSecond(val): 

 return val[1] 

 

# list1 to demonstrate the use of sorting 

# using using second key 

list1 = [(1, 2), (3, 3), (1, 1)] 

 

# sorts the array in ascending according to 

# second element 

list1.sort(key = sortSecond) 

print(list1) 

 

# sorts the array in descending according to 

# second element 

list1.sort(key = sortSecond, reverse = True) 

print(list1)   
  
---  
  
__

__

**Output:**

    
    
    [(1, 1), (1, 2), (3, 3)]
    [(3, 3), (1, 2), (1, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

