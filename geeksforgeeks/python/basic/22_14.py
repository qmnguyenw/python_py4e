Print all sublists of a list in Python



Given a list, print all the sublists of a list.  
 **Examples:**  

    
    
    Input  : list = [1, 2, 3] 
    Output : [[], [1], [1, 2], [1, 2, 3], [2], 
             [2, 3], [3]]
    
    Input : [1, 2, 3, 4] 
    Output : [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], 
             [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
    
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
The approach will be run two nested loop till the length of the given list.
The outer loop picks the starting element and the inner loop considers all
elements on the right of the picked elements as the ending element of the
subarray. To get the subarray we can use slicing to get the subarray.  

> Step 1: Run a loop till length of the given list.  
> Step 2: Run a loop from i+1 to length of the list to get all the subarrays
> from i to its right.  
> Step 3: Slice the subarray from i to j.  
> Step 4: Append it to a another list to store it  
> Step 5: Print it at the end

Below is the Python implementation of the above approach:  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print all

# sublist from a given list 

 

# function to generate all the sub lists

def sub_lists (l):

 base = [] 

 lists = [base]

 for i in range(len(l)):

 orig = lists[:]

 new = l[i]

 for j in range(len(lists)):

 lists[j] = lists[j] + [new]

 lists = orig + lists

 

 return lists

 

# driver code

l1 = [1, 2, 3]

print(sub_lists(l1))  
  
---  
  
 __

 __

 **Output:**  

    
    
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

