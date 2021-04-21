Python Program to Flatten a List without using Recursion



The task is to convert a nested list into a single list in Python i.e no
matter how many levels of nesting are there in the Python list, all the nested
has to be removed in order to convert it to a single containing all the values
of all the lists inside the outermost brackets but without any brackets
inside. In other words, an element in a list can be a number or a list. It
needs to be converted to a list where each element in the list is only a
number.

 **Examples:**

>  **Input:** [1,2,[3,4,[5,6],7],[[[8,9],10]],[11,[12,13]]]  
>  **Output:** [1,2,3,4,5,6,7,8,9,11,12,13]
>
>  **Input:** [1, [2, 3]]
>
>  **Output:** [1, 2, 3]
>
>  
>
>
>  
>

There are two methods to do this without recursion.

 **Method 1: Using a** **stack**

 **Approach:**

  * Initialization: Push the main list in a stack
  * Make an empty list to store the final result (result variable)
  * Loop till stack is not empty
    1. Pop the last added element of the stack and store it (current variable)
    2. If the popped element is a list than pushing all the elements of that list in the stack
    3. If the popped element is not a list, append that element in the result
  * Reverse the result list to get the final output in the original list’s order

 **Below is the implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Input list

l = [1, 2, [3, 4, [5, 6], 7],

 [[[8, 9], 10]],

 [11, [12, 13]]]

 

# Function to flatten the the list

 

 

def flatten(input_list):

 # Final list to be returned

 result = []

 

 # Creating stack and adding 

 # all elements into it

 stack = [input_list]

 

 # Iterate stack till it

 # does not get empty

 while stack:

 

 # Get the last element of the stack

 current = stack.pop(-1)

 

 # If the last element is a list,

 # add all the elements of that list in stack

 if isinstance(current, list):

 stack.extend(current)

 

 # Else add that element in the result

 else:

 result.append(current)

 

 # Reverse the result to get the

 # list in original order

 result.reverse()

 

 return result

 

 

# output list

ans = flatten(l)

print(ans)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

 **Method 2: Using libraries**

The package iteration_utilities can also be used to flatten a list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from iteration_utilities import deepflatten

 

l = [1, 2, [3, 4, [5, 6], 7], 

 [[[8, 9], 10]], [11, [12, 13]]]

 

ans = list(deepflatten(l))

print(ans)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

