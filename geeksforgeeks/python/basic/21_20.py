Python List Comprehension | Segregate 0’s and 1’s in an array list



You are given an array of 0s and 1s in random order. Segregate 0s on left side
and 1s on right side of the array.

Examples:

    
    
    Input  :  arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
    Output :  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Segregate 0s and 1s in
an array link. We can solve this problem quickly in Python using List
Comprehension. Traverse given list and separate out two different lists, one
contains all 0’s and another one contains all 1’s. Now concatenate both lists
together.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to Segregate 0's and 1's in an array list

 

def segregate(arr):

 res = ([x for x in arr if x==0] + [x for x
in arr if x==1])

 print(res)

 

# Driver program

if __name__ == "__main__":

 arr = [0, 1, 0, 1, 0, 0, 1, 1, 1,
0] 

 segregate(arr)  
  
---  
  
 __

 __

Output:

    
    
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

