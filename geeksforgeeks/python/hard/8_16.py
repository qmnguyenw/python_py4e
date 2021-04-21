Prefix sum array in Python using accumulate function



We are given an array, find prefix sums of given array.

Examples:

    
    
    Input : arr = [1, 2, 3]
    Output : sum = [1, 3, 6]
    
    Input : arr = [4, 6, 12]
    Output : sum = [4, 10, 22]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **prefix sum** is a sequence of partial sums of a given sequence. For
example, the cumulative sums of the sequence {a, b, c, …} are a, a+b, a+b+c
and so on. We can solve this problem in python quickly using
**accumulate(iterable)** method.

 __

 __  
 __

 __

 __  
 __  
 __

# function to find cumulative sum of array

from itertools import accumulate

 

def cumulativeSum(input):

 print ("Sum :", list(accumulate(input)))

 

# Driver program

if __name__ == "__main__":

 input = [4, 6, 12]

 cumulativeSum(input)  
  
---  
  
 __

 __

Output:

    
    
    Sum = [4, 10, 22]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

