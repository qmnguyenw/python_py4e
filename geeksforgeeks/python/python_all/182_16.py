Python Program for Linear Search



 **Problem:** Given an array arr[] of n elements, write a function to search a
given element x in arr[].  
 **Examples :**

    
    
    **Input :** arr[] = {10, 20, 80, 30, 60, 50, 
                         110, 100, 130, 170}
              x = 110;
    **Output :** 6
    Element x is present at index 6
    
    **Input :** arr[] = {10, 20, 80, 30, 60, 50, 
                         110, 100, 130, 170}
               x = 175;
    **Output :** -1
    Element x is not present in arr[].
    

A simple approach is to do **linear search** , i.e

  * Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
  * If x matches with an element, return the index.
  * If x doesn’t match with any of elements, return -1.

 **  
Example:** ![linear-search1](https://media.geeksforgeeks.org/wp-
content/uploads/Linear.png)

__

__  
__

__

__  
__  
__

# Searching an element in a list/array in python

# can be simply done using \'in\' operator

# Example:

# if x in arr:

# print arr.index(x)

 

# If you want to implement Linear Search in python

 

# Linearly search x in arr[]

# If x is present then return its location

# else return -1

 

def search(arr, x):

 

 for i in range(len(arr)):

 

 if arr[i] == x:

 return i

 

 return -1  
  
---  
  
 __

 __

The time complexity of above algorithm is O(n).

Please refer complete article on Linear Search for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

