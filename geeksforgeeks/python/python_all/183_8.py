Python Program for Comb Sort



Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always
compares adjacent values. So all inversions are removed one by one. Comb Sort
improves on Bubble Sort by using gap of size more than 1. The gap starts with
a large value and shrinks by a factor of 1.3 in every iteration until it
reaches the value 1. Thus Comb Sort removes more than one inversion counts
with one swap and performs better than Bublle Sort.

The shrink factor has been empirically found to be 1.3 (by testing Combsort on
over 200,000 random lists) [Source: Wiki]

Although, it works better than Bubble Sort on average, worst case remains
O(n2).

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for implementation of CombSort

 

# To find next gap from current

def getNextGap(gap):

 

 # Shrink gap by Shrink factor

 gap = (gap * 10)/13

 if gap < 1:

 return 1

 return gap

 

# Function to sort arr[] using Comb Sort

def combSort(arr):

 n = len(arr)

 

 # Initialize gap

 gap = n

 

 # Initialize swapped as true to make sure that

 # loop runs

 swapped = True

 

 # Keep running while gap is more than 1 and last

 # iteration caused a swap

 while gap !=1 or swapped == 1:

 

 # Find next gap

 gap = getNextGap(gap)

 

 # Initialize swapped as false so that we can

 # check if swap happened or not

 swapped = False

 

 # Compare all elements with current gap

 for i in range(0, n-gap):

 if arr[i] > arr[i + gap]:

 arr[i], arr[i + gap]=arr[i + gap], arr[i]

 swapped = True

 

 

# Driver code to test above

arr = [ 8, 4, 1, 3, -44, 23, -6, 28,
0]

combSort(arr)

 

print ("Sorted array:")

for i in range(len(arr)):

 print (arr[i]),

 

 

# This code is contributed by Mohit Kumra  
  
---  
  
 __

 __

 **Output :**

    
    
    Sorted array: 
    -44 -6 0 1 3 4 8 23 28 56 
    

Please refer complete article on Comb Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

