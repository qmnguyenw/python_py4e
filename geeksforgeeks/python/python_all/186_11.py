Python Program for Minimum number of jumps to reach end



Given an array of integers where each element represents the max number of
steps that can be made forward from that element. Write a function to return
the minimum number of jumps to reach the end of the array (starting from the
first element). If an element is 0, then cannot move through that element.

 **Example:**

    
    
    Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
    Output: 3 (1-> 3 -> 8 ->9)
    

First element is 1, so can only go to 3. Second element is 3, so can make at
most 3 steps eg to 5 or 8 or 9.

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

 **Method 1 (Naive Recursive Approach)**  
A naive approach is to start from the first element and recursively call for
all the elements reachable from first element. The minimum number of jumps to
reach end from first can be calculated using minimum number of jumps needed to
reach end from the elements reachable from first.

 _minJumps(start, end) = Min ( minJumps(k, end) ) for all k reachable from
start_  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find Minimum

# number of jumps to reach end

 

# Returns minimum number of jumps

# to reach arr[h] from arr[l]

def minJumps(arr, l, h):

 

 # Base case: when source and

 # destination are same

 if (h == l):

 return 0

 

 # when nothing is reachable 

 # from the given source

 if (arr[l] == 0):

 return float('inf')

 

 # Traverse through all the points 

 # reachable from arr[l]. Recursively 

 # get the minimum number of jumps 

 # needed to reach arr[h] from 

 # these reachable points.

 min = float('inf')

 for i in range(l + 1, h + 1):

 if (i < l + arr[l] + 1):

 jumps = minJumps(arr, i, h)

 if (jumps != float('inf') and

 jumps + 1 < min):

 min = jumps + 1

 

 return min

 

# Driver program to test above function

arr = [1, 3, 6, 3, 2, 3, 6, 8, 9,
5]

n = len(arr)

print('Minimum number of jumps to reach',

 'end is', minJumps(arr, 0, n-1))

 

# This code is contributed by Soumen Ghosh  
  
---  
  
 __

 __

