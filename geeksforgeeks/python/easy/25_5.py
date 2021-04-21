Program to print all distinct elements of a given integer array in Python |
Ordered Dictionary



  
Given an integer array, print all distinct elements in array. The given array
may contain duplicates and the output should print every element only once.
The given array is not sorted.

Examples:

    
    
    Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
    Output: 12, 10, 9, 45, 2
    
    Input: arr[] = {1, 2, 3, 4, 5}
    Output: 1, 2, 3, 4, 5
    
    Input: arr[] = {1, 1, 1, 1, 1}
    Output: 1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Print All Distinct Elements of
a given integer array link. We will solve this problem in python quickly using
Ordered Dictionary. Approach is simple,

  1. Convert array into dictionary data structure using **OrderedDict.fromkeys(iterable)** function, it converts any iterable into dictionary having elements as Key in the same order they appeared in array.
  2. Now iterate through complete dictionary and print keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print All Distinct

# Elements of a given integer array

 

from collections import OrderedDict

 

def printDistinct(input):

 # convert list into ordered dictionary

 ordDict = OrderedDict.fromkeys(input)

 

 # iterate through dictionary and get list of keys

 # list of keys will be resultant distinct elements 

 # in array

 result = [ key for (key, value) in ordDict.items() ]

 

 # concatenate list of elements with ', ' and print

 print (', '.join(map(str, result))) 

 

# Driver program

if __name__ == "__main__":

 input = [12, 10, 9, 45, 2, 10, 10,
45]

 printDistinct(input)  
  
---  
  
 __

 __

Output:

    
    
    12, 10, 9, 45, 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

