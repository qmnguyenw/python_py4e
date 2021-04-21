Move all zeroes to end of array using List Comprehension in Python



Given an array of random numbers, Push all the zeros of a given array to the
end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7,
0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order
of all other elements should be same. Expected time complexity is O(n) and
extra space is O(1).

Examples:

    
    
    Input :  arr = [1, 2, 0, 4, 3, 0, 5, 0]
    Output : arr = [1, 2, 4, 3, 5, 0, 0, 0]
    
    Input : arr  = [1, 2, 0, 0, 0, 3, 6]
    Output : arr = [1, 2, 3, 6, 0, 0, 0]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Move all zeroes to end
of array link. We will solve this problem in python using List Comprehension
in a single line of code.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to append all zeros at the end

# of array

def moveZeros(arr):

 

 # first expression returns a list of

 # all non zero elements in arr in the 

 # same order they were inserted into arr

 # second expression returns a list of 

 # zeros present in arr

 return [nonZero for nonZero in arr if nonZero!=0] +
\

 [Zero for Zero in arr if Zero==0]

 

# Driver function

if __name__ == "__main__":

 arr = [1, 2, 0, 4, 3, 0, 5, 0]

 print (moveZeros(arr))  
  
---  
  
 __

 __

Output:

    
    
    [1, 2, 4, 3, 5, 0, 0, 0]
    

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

