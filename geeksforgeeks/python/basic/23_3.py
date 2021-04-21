Python map function to find row with maximum number of 1’s



Given a boolean 2D array, where each row is sorted. Find the row with the
maximum number of 1s.

Examples:

    
    
    Example
    Input: matrix =
    [[0, 1, 1, 1],
     [0, 0, 1, 1],
     [1, 1, 1, 1],  
     [0, 0, 0, 0]]
    Output: 2
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Find the row with
maximum number of 1’s. We can solve this problem in python quickly using map()
function. Approach is very simple, find sum of all 1’s in each row and then
print **index** of maximum sum in a list because row having maximum 1 will
also have maximum sum.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find the row with maximum number of 1's

def maxOnes(input):

 

 # map sum function on each row of

 # given matrix

 # it will return list of sum of all one's

 # in each row, then find index of maximum element

 result = list(map(sum,input))

 print (result.index(max(result)))

 

# Driver program

if __name__ == "__main__":

 input = [[0, 1, 1, 1],[0, 0, 1,
1],[1, 1, 1, 1],[0, 0, 0, 0]]

 maxOnes(input)  
  
---  
  
 __

 __

 **Complexity :** O(M*N)

  

  

Output:

    
    
    2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

