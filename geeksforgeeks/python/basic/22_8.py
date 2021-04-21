sort() in Python



Like C++ sort(), Java sort() and other languages, python also provides built
in function to sort.

The sort function can be used to sort the list in both ascending and
descending order.

To sort the list in ascending order.

 **Syntax**

> # This will sort the given list in ascending order.  
> # It returns a sorted list according to the passed parameter.  
> List_name.sort()
>
>  
>
>
>  
>

This function can be used to sort list of integers, floating point number,
string and others.

 __

 __  
 __

 __

 __  
 __  
 __

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

Output:

    
    
    [1, 2, 3, 4]
    [1.68, 2.0, 2.01, 3.28, 3.67]
    ['For', 'Geeks', 'Geeks']
    
    

To sort the list in descending order.

 **Syntax**

    
    
    list_name.sort(reverse=True)
    This will sort the given list in descending order.
    

__

__  
__

__

__  
__  
__

# List of Integers

numbers = [1, 3, 4, 2]

 

# Sorting list of Integers

numbers.sort(reverse=True)

 

print(numbers)

 

# List of Floating point numbers

decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]

 

# Sorting list of Floating point numbers

decimalnumber.sort(reverse=True)

 

print(decimalnumber)

 

# List of strings

words = ["Geeks", "For", "Geeks"]

 

# Sorting list of strings

words.sort(reverse=True)

 

print(words)  
  
---  
  
 __

 __

Output:

    
    
    [4, 3, 2, 1]
    [3.67, 3.28, 2.01, 2.0, 1.68]
    ['Geeks', 'Geeks', 'For']

 **Syntax :**

> list_name.sort() – it sorts in ascending order  
> list_name.sort(reverse=True) – it sorts in descending order  
> list_name.sort(key=…, reverse=…) – it sorts according to user’s choice

 **Parameters:**  
By default, sort() doesn’t require any extra parameters. However, it has two
optional parameters:

>  **reverse** – If true, the list is sorted in descending order  
>  **key** – function that serves as a key for the sort comparison

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

list1 = [(1,2),(3,3),(1,1)]

 

# sorts the array in ascending according to 

# second element

list1.sort(key=sortSecond) 

print(list1)

 

# sorts the array in descending according to

# second element

list1.sort(key=sortSecond,reverse=True)

print(list1)  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 1), (1, 2), (3, 3)]
    [(3, 3), (1, 2), (1, 1)]
    

Please refer Python Sort articles for more Python Sorting articles.

Thanks to striver for inputs on this topic.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

