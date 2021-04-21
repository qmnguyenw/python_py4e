Python list | index()



 _ **index()**_ is an inbuilt function in Python, which searches for a given
element from the start of the list and returns the lowest index where the
element appears.  
**Syntax :**  

    
    
    list_name.index(element, start, end)
    
    
    
    
    

**Parameters :**  

    
    
    **element** - The element whose lowest index will be returned.
    
    **start** _(Optional)_ - The position from where the search begins.
    **end** _(Optional)_ - The position from where the search ends.
    
    
    
    
    
    

**Returns :**  

    
    
    Returns lowest index where the element appears.
    
    
    
    
    

**Error :**  

    
    
    If any element which is not present is searched,
    it returns a ValueError
    
    
    
    
    

**Code #1 :**  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for demonstration

# of list index() method

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print the index of '4' in list1

print(list1.index(4))

list2 = ['cat', 'bat', 'mat', 'cat', 'pet']

# Will print the index of 'cat' in list2

print(list2.index('cat'))  
  
---  
  
 __

 __

Output :  

    
    
    3
    0
    
    
    
    
    
    

  
**Code #2 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for demonstration

# of index() method

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print index of '4' in sublist

# having index from 4 to 8.

print(list1.index(4, 4, 8))

# Will print index of '1' in sublist

# having index from 1 to 7.

print(list1.index(1, 1, 7))

list2 = ['cat', 'bat', 'mat', 'cat',

 'get', 'cat', 'sat', 'pet']

# Will print index of 'cat' in sublist

# having index from 2 to 6

print(list2.index('cat', 2, 6 ))  
  
---  
  
 __

 __

Output :  

    
    
    7
    4
    3
    
    
    
    
    

  
**Code #3 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for demonstration

# of list index() method

# Random list having sublist and tuple also

list1 = [1, 2, 3, [9, 8, 7], ('cat',
'bat')]

# Will print the index of sublist [9, 8, 7]

print(list1.index([9, 8, 7]))

# Will print the index of tuple

# ('cat', 'bat') inside list

print(list1.index(('cat', 'bat')))  
  
---  
  
 __

 __

 **Output :**  

    
    
    3
    4
    
    
    
    
    

  
**Code #4 :** ValueError  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for demonstration

# of index() method error

 

 

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Return ValueError

print(list1.index(10))  
  
---  
  
 __

 __

 **Output :**  

    
    
    Traceback (most recent call last):
      File "/home/b910d8dcbc0f4f4b61499668654450d2.py", line 8, in 
        print(list1.index(10))
    ValueError: 10 is not in list
    
    
    
    
    
    

**Code #5 :** When 2 arguments are passed

  

  

When two arguments are passed in the index function, the first argument is
treated as the element to be searched and the second argument is the index
from where the searching begins.

    
    
    list_name.index(element , start)
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for demonstration

# of index() method

list1 = [6 , 8 , 5 , 6 , 1 , 2]

# Will print index of '3' in sublist

# having index from 1 to end of the list.

print(list1.index(6 , 1 ))  
  
---  
  
 __

 __

 **Output :**

    
    
    3
    

**Code #6** : The end index passed as argument is not included

The third argument which is the end, itself is not included in the range from
start to end, i.e the searching takes place from start to end-1 index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for demonstration

# of index() method

list1 = [6 , 2 , 14 , 8 , 9 , 10]

# return error as index '4' is not included in the range

# having index from 1 to 4.

print(list1.index(9 , 1 , 4))  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "/home/3cbe5b7d0595ab3f8564f16af7a15172.py", line 9, in <module>
        print(list1.index(9 , 1 , 4))
    ValueError: 9 is not in list
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for demonstration

# of index() method

list1 = [6 , 2 , 14 , 8 , 9 , 10]

# Will print index of '4' in sublist as now index '4' is included

# having index from 1 to 5.

print(list1.index(9, 1, 5))  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

