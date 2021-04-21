Python Program for Recursive Insertion Sort



Insertion sort is a simple sorting algorithm that works the way we sort
playing cards in our hands.  
Below is an iterative algorithm for insertion sort

 **Algorithm**

    
    
    // Sort an arr[] of size n
    insertionSort(arr, n) 
        Loop from i = 1 to n-1.
           a) Pick element arr[i] and insert
              it into sorted sequence arr[0..i-1] 

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Recursive Python program for insertion sort

# Recursive function to sort an array using insertion sort

 

def insertionSortRecursive(arr,n):

 # base case

 if n<=1:

 return

 

 # Sort first n-1 elements

 insertionSortRecursive(arr,n-1)

 \'\'\'Insert last element at its correct position

 in sorted array.\'\'\'

 last = arr[n-1]

 j = n-2

 

 # Move elements of arr[0..i-1], that are

 # greater than key, to one position ahead

 # of their current position 

 while (j>=0 and arr[j]>last):

 arr[j+1] = arr[j]

 j = j-1

 

 arr[j+1]=last

 

# A utility function to print an array of size n

def printArray(arr,n):

 for i in range(n):

 print arr[i],

 

# Driver program to test insertion sort 

arr = [12,11,13,5,6]

n = len(arr)

insertionSortRecursive(arr, n)

printArray(arr, n)

 

# Contributed by Harsh Valecha  
  
---  
  
 __

 __

Please refer complete article onRecursive Insertion Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

