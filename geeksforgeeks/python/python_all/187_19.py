Python Program to Find the Number Occurring Odd Number of Times



Given an array of positive integers. All numbers occur even number of times
except one number which occurs odd number of times. Find the number in O(n)
time & constant space.

 **Examples :**

    
    
    Input : arr = {1, 2, 3, 2, 3, 1, 3}
    Output : 3
    
    Input : arr = {5, 7, 2, 7, 5, 2, 5}
    Output : 5
    

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the element occurring

# odd number of times

 

# function to find the element occurring odd

# number of times

def getOddOccurrence(arr, arr_size):

 

 for i in range(0, arr_size):

 count = 0

 for j in range(0, arr_size):

 if arr[i] == arr[j]:

 count+= 1

 

 if (count % 2 != 0):

 return arr[i]

 

 return -1

 

 

# driver code 

arr = [2, 3, 5, 4, 5, 2, 4, 3, 5,
2, 4, 4, 2 ]

n = len(arr)

print(getOddOccurrence(arr, n))

 

# This code has been contributed by 

# Smitha Dinesh Semwal  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

A **Better Solution** is to use Hashing. Use array elements as key and their
counts as value. Create an empty hash table. One by one traverse the given
array elements and store counts. Time complexity of this solution is O(n). But
it requires extra space for hashing.

 **Program :**  

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __



# Python program to find the element occurring odd number of times

 

def getOddOccurrence(arr):

 

 # Initialize result

 res = 0

 

 # Traverse the array

 for element in arr:

 # XOR with the result

 res = res ^ element

 

 return res

 

# Test array

arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5,
2, 4, 4, 2]

 

print "% d" % getOddOccurrence(arr)  
  
---  
  
 __

 __

