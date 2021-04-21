Python Program for Binary Insertion Sort



We can use binary search to reduce the number of comparisons in normal
insertion sort. Binary Insertion Sort find use binary search to find the
proper location to insert the selected item at each iteration.  
In normal insertion, sort it takes O(i) (at ith iteration) in worst case. we
can reduce it to O(logi) by using binary search.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program implementation

# of binary insertion sort

 

def binary_search(arr, val, start, end):

 # we need to distinugish whether we should insert

 # before or after the left boundary.

 # imagine [0] is the last step of the binary search

 # and we need to decide where to insert -1

 if start == end:

 if arr[start] > val:

 return start

 else:

 return start+1

 

 # this occurs if we are moving beyond left\'s boundary

 # meaning the left boundary is the least position to

 # find a number greater than val

 if start > end:

 return start

 

 mid = (start+end)/2

 if arr[mid] < val:

 return binary_search(arr, val, mid+1, end)

 elif arr[mid] > val:

 return binary_search(arr, val, start, mid-1)

 else:

 return mid

 

def insertion_sort(arr):

 for i in xrange(1, len(arr)):

 val = arr[i]

 j = binary_search(arr, val, 0, i-1)

 arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]

 return arr

 

print("Sorted array:")

print insertion_sort([37, 23, 0, 17, 12, 72,
31,

 46, 100, 88, 54])

 

# Code contributed by Mohit Gupta_OMG   
  
---  
  
__

__

Please refer complete article onBinary Insertion Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

