Python Program for Bubble Sort



Bubble Sort is the simplest sorting algorithm that works by repeatedly
swapping the adjacent elements if they are in wrong order.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for implementation of Bubble Sort

 

def bubbleSort(arr):

 n = len(arr)

 

 # Traverse through all array elements

 for i in range(n-1):

 # range(n) also work but outer loop will repeat one time more than
needed.

 

 # Last i elements are already in place

 for j in range(0, n-i-1):

 

 # traverse the array from 0 to n-i-1

 # Swap if the element found is greater

 # than the next element

 if arr[j] > arr[j+1] :

 arr[j], arr[j+1] = arr[j+1], arr[j]

 

# Driver code to test above

arr = [64, 34, 25, 12, 22, 11, 90]

 

bubbleSort(arr)

 

print ("Sorted array is:")

for i in range(len(arr)):

 print ("%d" %arr[i]),   
  
---  
  
__

__

Please refer complete article onBubble Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

