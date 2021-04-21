Python Program for ShellSort



In shellSort, we make the array h-sorted for a large value of h. We keep
reducing the value of h until it becomes 1. An array is said to be h-sorted if
all sublists of every h\’th element is sorted.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for implementation of Shell Sort

 

def shellSort(arr):

 

 # Start with a big gap, then reduce the gap

 n = len(arr)

 gap = n/2

 

 # Do a gapped insertion sort for this gap size.

 # The first gap elements a[0..gap-1] are already in gapped 

 # order keep adding one more element until the entire array

 # is gap sorted

 while gap > 0:

 

 for i in range(gap,n):

 

 # add a[i] to the elements that have been gap sorted

 # save a[i] in temp and make a hole at position i

 temp = arr[i]

 

 # shift earlier gap-sorted elements up until the correct

 # location for a[i] is found

 j = i

 while j >= gap and arr[j-gap] >temp:

 arr[j] = arr[j-gap]

 j -= gap

 

 # put temp (the original a[i]) in its correct location

 arr[j] = temp

 gap /= 2

 

 

# Driver code to test above

arr = [ 12, 34, 54, 2, 3]

 

n = len(arr)

print ("Array before sorting:")

for i in range(n):

 print(arr[i]),

 

shellSort(arr)

 

print ("\nArray after sorting:")

for i in range(n):

 print(arr[i]),

 

# This code is contributed by Mohit Kumra  
  
---  
  
 __

 __

 **Output:**

    
    
    Array before sorting:
    12 34 54 2 3 
    Array after sorting:
    2 3 12 34 54
    

Please refer complete article on ShellSort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

