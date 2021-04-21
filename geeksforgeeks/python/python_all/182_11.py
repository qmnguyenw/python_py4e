Python Program for Cycle Sort



Cycle sort is an in-place sorting Algorithm, unstable sorting algorithm, a
comparison sort that is theoretically optimal in terms of the total number of
writes to the original array.

  * It is optimal in terms of number of memory writes. It minimizes the number of memory writes to sort (Each value is either written zero times, if it’s already in its correct position, or written one time to its correct position.)
  * It is based on the idea that array to be sorted can be divided into cycles. Cycles can be visualized as a graph. We have n nodes and an edge directed from node i to node j if the element at i-th index must be present at j-th index in the sorted array.  
Cycle in arr[] = {4, 5, 2, 1, 5}  
![cycle-sort](https://media.geeksforgeeks.org/wp-content/cdn-uploads/cycle-
sort.png)

Cycle in arr[] = {4, 3, 2, 1}  
![cyclc-sort2](https://media.geeksforgeeks.org/wp-content/cdn-uploads/cyclc-
sort2.png)

We one by one consider all cycles. We first consider the cycle that includes
first element. We find correct position of first element, place it at its
correct position, say j. We consider old value of arr[j] and find its correct
position, we keep doing this till all elements of current cycle are placed at
correct position, i.e., we don\’t come back to cycle starting point.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to impleament cycle sort

 

def cycleSort(array):

 writes = 0

 

 # Loop through the array to find cycles to rotate.

 for cycleStart in range(0, len(array) - 1):

 item = array[cycleStart]

 

 # Find where to put the item.

 pos = cycleStart

 for i in range(cycleStart + 1, len(array)):

 if array[i] < item:

 pos += 1

 

 # If the item is already there, this is not a cycle.

 if pos == cycleStart:

 continue

 

 # Otherwise, put the item there or right after any duplicates.

 while item == array[pos]:

 pos += 1

 array[pos], item = item, array[pos]

 writes += 1

 

 # Rotate the rest of the cycle.

 while pos != cycleStart:

 

 # Find where to put the item.

 pos = cycleStart

 for i in range(cycleStart + 1, len(array)):

 if array[i] < item:

 pos += 1

 

 # Put the item there or right after any duplicates.

 while item == array[pos]:

 pos += 1

 array[pos], item = item, array[pos]

 writes += 1

 

 return writes

 

# driver code 

arr = [1, 8, 3, 9, 10, 10, 2, 4 ]

n = len(arr) 

cycleSort(arr)

 

print("After sort : ")

for i in range(0, n) : 

 print(arr[i], end = \' \')

 

# Code Contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output:**

    
    
    After sort : 
    1 2 3 4 8 9 10 10 
    

Please refer complete article on Cycle Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

