Array in Python | Set 1 (Introduction and Functions)



Other than some generic containers like list, Python in its definition can
also handle containers with specified data types. The array can be handled in
python by a module named “ **array** “. They can be useful when we have to
manipulate only a specific data type values.  
 **Operations on Array :**  
 **1\. array(data type, value list)** :- This function is used to **create**
an array with data type and value list specified in its arguments. Some data
types are mentioned in the table below.  
Type Code| C Type| Python Type| Minimum size in Bytes| ‘b’| signed char| int|
1| ‘B’| unsigned char| int| 1| ‘u’| Py_UNICODE| unicode character| 2| ‘h’|
signed short| int| 2| ‘H’| unsigned short| int| 2| ‘i’| signed int| int| 2|
‘I’| unsigned int| int| 2| ‘l’| signed long| int| 4| ‘L’| unsigned long| int|
4| ‘q’| signed long long| int| 8| ‘Q’| unsigned long long| int| 8| ‘f’| float|
float| 4| ‘d’| double| float| 8  
---|---|---|---  
  
 **2\. append()** :- This function is used to **add the value** mentioned in
its arguments at the **end** of the array.  
 **3\. insert(i,x)** :- This function is used to **add the value(x) at the ith
position** specified in its argument.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# array(), append(), insert()

 

# importing "array" for array operations

import array

 

# initializing array with array values

# initializes array with signed integers

arr = array.array('i', [1, 2, 3])

# printing original array

print ("The new created array is : ",end=" ")

for i in range (0, 3):

 print (arr[i], end=" ")

print("\r")

# using append() to insert new value at end

arr.append(4);

# printing appended array

print("The appended array is : ", end="")

for i in range (0, 4):

 print (arr[i], end=" ")

 

# using insert() to insert value at specific position

# inserts 5 at 2nd position

arr.insert(2, 5)

print("\r")

# printing array after insertion

print ("The array after insertion is : ", end="")

for i in range (0, 5):

 print (arr[i], end=" ")  
  
---  
  
 __

 __

 **Output:**

    
    
    The new created array is : 1 2 3 
    The appended array is : 1 2 3 4 
    The array after insertion is : 1 2 5 3 4 
    

  
**4\. pop()** :- This function **removes the element at the position**
mentioned in its argument and returns it.  
 **5\. remove()** :- This function is used to **remove the first occurrence**
of the value mentioned in its arguments.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# pop() and remove()

# importing "array" for array operations

import array

# initializing array with array values

# initializes array with signed integers

arr= array.array('i',[1, 2, 3, 1, 5])

# printing original array

print ("The new created array is : ",end="")

for i in range (0,5):

 print (arr[i],end=" ")

print ("\r")

# using pop() to remove element at 2nd position

print ("The popped element is : ",end="")

print (arr.pop(2));

# printing array after popping

print ("The array after popping is : ",end="")

for i in range (0,4):

 print (arr[i],end=" ")

print("\r")

# using remove() to remove 1st occurrence of 1

arr.remove(1)

# printing array after removing

print ("The array after removing is : ",end="")

for i in range (0,3):

 print (arr[i],end=" ")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The new created array is : 1 2 3 1 5 
    The popped element is : 3
    The array after popping is : 1 2 1 5 
    The array after removing is : 2 1 5 
    
    
    

  
**6\. index()** :- This function returns the **index of the first occurrence**
of value mentioned in arguments.  
 **7\. reverse()** :- This function **reverses** the array.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# index() and reverse()

 

# importing "array" for array operations

import array

 

# initializing array with array values

# initializes array with signed integers

arr= array.array('i',[1, 2, 3, 1, 2, 5])

# printing original array

print ("The new created array is : ",end="")

for i in range (0,6):

 print (arr[i],end=" ")

print ("\r")

# using index() to print index of 1st occurrenece of 2

print ("The index of 1st occurrence of 2 is : ",end="")

print (arr.index(2))

#using reverse() to reverse the array

arr.reverse()

# printing array after reversing

print ("The array after reversing is : ",end="")

for i in range (0,6):

 print (arr[i],end=" ")  
  
---  
  
 __

 __

 **Output:**

    
    
    The new created array is : 1 2 3 1 2 5 
    The index of 1st occurrence of 2 is : 1
    The array after reversing is : 5 2 1 3 2 1
    
    
    

**Reference :**  
https://docs.python.org/3/library/array.html#module-array  
This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

