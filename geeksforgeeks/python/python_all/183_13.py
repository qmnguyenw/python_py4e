Python Program for Iterative Merge Sort



Following is a typical recursive implementation of Merge Sort that uses last
element as pivot.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Recursive Python Program for merge sort

 

def merge(left, right):

 if not len(left) or not len(right):

 return left or right

 

 result = []

 i, j = 0, 0

 while (len(result) < len(left) + len(right)):

 if left[i] < right[j]:

 result.append(left[i])

 i+= 1

 else:

 result.append(right[j])

 j+= 1

 if i == len(left) or j == len(right):

 result.extend(left[i:] or right[j:])

 break

 

 return result

 

def mergesort(list):

 if len(list) < 2:

 return list

 

 middle = len(list)/2

 left = mergesort(list[:middle])

 right = mergesort(list[middle:])

 

 return merge(left, right)

 

seq = [12, 11, 13, 5, 6, 7]

print("Given array is")

print(seq); 

print("\n")

print("Sorted array is")

print(mergesort(seq))

 

# Code Contributed by Mohit Gupta_OMG   
  
---  
  
__

__

Please refer complete article onIterative Merge Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

