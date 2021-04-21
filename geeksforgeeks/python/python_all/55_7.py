Python program to find the Strongest Neighbour



Given an array arr[] of N positive integers. The task is to find the maximum
for every adjacent pair in the array.

 **Examples:**

    
    
     **Input:** 1 2 2 3 4 5
    **Output:** 2 2 3 4 5
    
    **Input:** 5 5
    **Output:** 5
    

**Approach:**

  1. Read the input array i.e,arr1.
  2. for i=1 to sizeofarray-1
    * find the max value between arr1[i] and arr1[i-1].
    * store the above value in another array i.e, arr2.
  3. print the values of arr2.

Below is the implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# define a function for finding

# the maximum for adjacent

# pairs in the array

def maximumAdjacent(arr1, n):

 

 # array to store the max 

 # value between adjacent pairs

 arr2 = [] 

 

 # iterate from 1 to n - 1

 for i in range(1, n):

 

 # find max value between 

 # adjacent pairs gets 

 # stored in r

 r = max(arr1[i], arr1[i-1])

 

 # add element 

 arr2.append(r)

 

 # printing the elements

 for ele in arr2 :

 print(ele,end=" ")

 

if __name__ == "__main__" :

 

 # size of the input array

 n = 6

 

 # input array

 arr1 = [1,2,2,3,4,5]

 

 # function calling

 maximumAdjacent(arr1, n)  
  
---  
  
 __

 __

 **Output:**

    
    
    2 2 3 4 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

