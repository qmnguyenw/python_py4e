Python Program for QuickSort



Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an
element as pivot and partitions the given array around the picked pivot. There
are many different versions of quickSort that pick pivot in different ways.

  1. Always pick first element as pivot.
  2. Always pick last element as pivot (implemented below)
  3. Pick a random element as pivot.
  4. Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an
array and an element x of array as pivot, put x at its correct position in
sorted array and put all smaller elements (smaller than x) before x, and put
all greater elements (greater than x) after x. All this should be done in
linear time.  
**Pseudo Code for recursive QuickSort function :**

    
    
    /* low  --> Starting index,  high  --> Ending index */
    quickSort(arr[], low, high)
    {
        if (low < high)
        {
            /* pi is partitioning index, arr[p] is now
               at right place */
            pi = partition(arr, low, high);
    
            quickSort(arr, low, pi - 1);  // Before pi
            quickSort(arr, pi + 1, high); // After pi
        }
    }
    
    

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for implementation of Quicksort Sort

 

# This function takes last element as pivot, places

# the pivot element at its correct position in sorted

# array, and places all smaller (smaller than pivot)

# to left of pivot and all greater elements to right

# of pivot

 

 

def partition(arr, low, high):

 i = (low-1) # index of smaller element

 pivot = arr[high] # pivot

 

 for j in range(low, high):

 

 # If current element is smaller than or

 # equal to pivot

 if arr[j] <= pivot:

 

 # increment index of smaller element

 i = i+1

 arr[i], arr[j] = arr[j], arr[i]

 

 arr[i+1], arr[high] = arr[high], arr[i+1]

 return (i+1)

 

# The main function that implements QuickSort

# arr[] --> Array to be sorted,

# low --> Starting index,

# high --> Ending index

 

# Function to do Quick sort

 

 

def quickSort(arr, low, high):

 if len(arr) == 1:

 return arr

 if low < high:

 

 # pi is partitioning index, arr[p] is now

 # at right place

 pi = partition(arr, low, high)

 

 # Separately sort elements before

 # partition and after partition

 quickSort(arr, low, pi-1)

 quickSort(arr, pi+1, high)

 

 

# Driver code to test above

arr = [10, 7, 8, 9, 1, 5]

n = len(arr)

quickSort(arr, 0, n-1)

print("Sorted array is:")

for i in range(n):

 print("%d" % arr[i]),

 

# This code is contributed by Mohit Kumra

#This code in improved by https://github.com/anushkrishnav  
  
---  
  
 __

 __

Please refer complete article onQuickSort for more details!  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

