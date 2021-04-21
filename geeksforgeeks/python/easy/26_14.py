Merge two sorted arrays in Python using heapq



Given two sorted arrays, the task is to merge them in a sorted manner.

Examples:

    
    
    Input :  arr1 = [1, 3, 4, 5]  
             arr2 = [2, 4, 6, 8]
    Output : arr3 = [1, 2, 3, 4, 4, 5, 6, 8]
    
    Input  : arr1 = [5, 8, 9]  
             arr2 = [4, 7, 8]
    Output : arr3 = [4, 5, 7, 8, 8, 9]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Merge two sorted arrays link.
We will solve this problem in python using **heapq.merge()** in a single line
of code.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to merge two sorted arrays

from heapq import merge

 

def mergeArray(arr1,arr2):

 return list(merge(arr1, arr2))

 

# Driver function

if __name__ == "__main__":

 arr1 = [1,3,4,5] 

 arr2 = [2,4,6,8]

 print (mergeArray(arr1, arr2))  
  
---  
  
 __

 __

Output:

  

  

    
    
    [1, 2, 3, 4, 4, 5, 6, 8]
    

### Properties of heapq module ?

This module provides an implementation of the heap queue algorithm, also known
as the priority queue algorithm.  
To create a heap, use a list initialized to [], or you can transform a
populated list into a heap via function heapify().The following functions are
provided:

  *  ** _heapq.heappush(heap,item) :_** Push the value item onto the heap, maintaining the heap invariant.
  *  ** _heapq.heappop(heap) :_** Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, **IndexError** is raised. To access the smallest item without popping it, use heap[0].
  *  ** _heapq.heappushpop(heap, item) :_** Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
  *  ** _heapq.heapify(x) :_** Transform list x into a heap, in-place, in linear time.
  *  ** _heapq.merge(*iterables) :_** Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

