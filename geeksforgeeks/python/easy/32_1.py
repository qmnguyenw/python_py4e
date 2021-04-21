Array in Python | Set 2 (Important Functions)



Array in Python | Set 1 (Introduction and Functions)

Below are some more functions.

 **1\. typecode** :- This function **returns the data type** by which array is
initialised.

 **2\. itemsize** :- This function returns **size** in bytes of a **single
array element.**

 **3\. buffer_info()** :- Returns a tuple representing the **address in which
array is stored and number of elements** in it.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# typecode, itemsize, buffer_info()

 

# importing "array" for array operations

import array

 

# initializing array with array values

# initializes array with signed integers

arr= array.array('i',[1, 2, 3, 1, 2, 5]) 

 

# using typecode to print datatype of array

print ("The datatype of array is : ")

print (arr.typecode)

 

# using itemsize to print itemsize of array

print ("The itemsize of array is : ")

print (arr.itemsize)

 

# using buffer_info() to print buffer info. of array

print ("The buffer info. of array is : ")

print (arr.buffer_info())  
  
---  
  
 __

 __

 **Output:**

    
    
    The datatype of array is : 
    i
    The itemsize of array is : 
    4
    The buffer info. of array is : 
    (29784224, 6)
    

Instead of import array, we can also use * to import array.

 __

 __  
 __

 __

 __  
 __  
 __

# importing "array" using * for array operations

from array import *

 

# initializing array with array values

# initializes array with signed integers

arr = array('i',[1, 2, 3, 1, 2, 5]) 

 

print(arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    array('i', [1, 2, 3, 1, 2, 5])
    

**4\. count()** :- This function **counts the number of occurrences** of
argument mentioned in array.

 **5\. extend(arr)** :- This function **appends a whole array** mentioned in
its arguments to the specified array.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# count() and extend()

 

# importing "array" for array operations

import array

 

# initializing array 1 with array values

# initializes array with signed integers

arr1 = array.array('i',[1, 2, 3, 1, 2, 5]) 

 

# initializing array 2 with array values

# initializes array with signed integers

arr2 = array.array('i',[1, 2, 3]) 

 

# using count() to count occurrences of 1 in array

print ("The occurrences of 1 in array is : ")

print (arr1.count(1))

 

# using extend() to add array 2 elements to array 1 

arr1.extend(arr2)

 

print ("The modified array is : ")

for i in range (0,9):

 print (arr1[i])  
  
---  
  
 __

 __

 **Output:**

    
    
    The occurrences of 1 in array is : 
    2
    The modified array is : 
    1
    2
    3
    1
    2
    5
    1
    2
    3
    

**6\. fromlist(list)** :- This function is used to **append a list** mentioned
in its argument **to end of array**.

 **7\. tolist()** :- This function is used to **transform an array into a
list**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# fromlist() and tolist()

 

# importing "array" for array operations

import array

 

# initializing array with array values

# initializes array with signed integers

arr = array.array('i',[1, 2, 3, 1, 2, 5]) 

 

# initializing list

li = [1, 2, 3]

 

# using fromlist() to append list at end of array

arr.fromlist(li)

 

# printing the modified array

print ("The modified array is : ",end="")

for i in range (0,9):

 print (arr[i],end=" ")

 

# using tolist() to convert array into list

li2 = arr.tolist()

 

print ("\r")

 

# printing the new list

print ("The new list created is : ",end="")

for i in range (0,len(li2)):

 print (li2[i],end=" ")  
  
---  
  
 __

 __

 **Output:**

    
    
    The modified array is : 1 2 3 1 2 5 1 2 3 
    The new list created is : 1 2 3 1 2 5 1 2 3
    

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

