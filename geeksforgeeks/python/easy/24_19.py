Python List Comprehension to find pair with given sum from two arrays



Given two unsorted arrays of distinct elements, the task is to find all pairs
from both arrays whose sum is equal to x.

Examples:

    
    
    Input :  arr1 = [-1, -2, 4, -6, 5, 7]
             arr2 = [6, 3, 4, 0]  
             x = 8
    Output : [(5, 3), (4, 4)]
             
    
    Input : arr1 = [1, 2, 4, 5, 7] 
            arr2 = [5, 6, 3, 4, 8]  
            x = 9
    Output : [(1, 8), (4, 5), (5, 4)]
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Given two unsorted
arrays, find all pairs whose sum is x link. We can solve this problem quickly
in python using List comprehension. Approach is very simple, we will consider
all those pairs for which **if k lies in arr2** then **x-k should lie in
arr1** , so pair will be (x-k,k).

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find all pairs whose sum is x in

# two arrays

 

def allPairs(arr1,arr2,x):

 

 # finds all pairs in two arrays

 # whose sum is x

 print ([(x-k,k) for k in arr2 if (x-k) in
arr1])

 

# Driver program

if __name__ == "__main__":

 arr1 = [-1, -2, 4, -6, 5, 7]

 arr2 = [6, 3, 4, 0] 

 x = 8

 allPairs(arr1,arr2,x)  
  
---  
  
 __

 __

 **Complexity :** O(n*n)  
Output:

    
    
    [(5, 3), (4, 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

