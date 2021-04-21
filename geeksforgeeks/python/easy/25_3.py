Python | Minimum number of subsets with distinct elements using Counter



You are given an array of n-element. You have to make subsets from the array
such that no subset contain duplicate elements. Find out minimum number of
subset possible.

Examples:

    
    
    Input : arr[] = {1, 2, 3, 4}
    Output :1
    Explanation : A single subset can contains all 
    values and all values are distinct
    
    Input : arr[] = {1, 2, 3, 3}
    Output : 2
    Explanation : We need to create two subsets
    {1, 2, 3} and {3} [or {1, 3} and {2, 3}] such
    that both subsets have distinct elements.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Minimum number of
subsets with distinct elements link. We will solve this problem quickly in
python using Counter(iterable) method. Approach is very simple, calculate
frequency of each element in array and print value of maximum frequency
because we want each subset to be different and we have to put any repeated
element in different subset, so to get minimum number of subset we should have
at least **maximum frequency number of subsets**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find Minimum number of

# subsets with distinct elements using Counter

 

# function to find Minimum number of subsets 

# with distinct elements

from collections import Counter

 

def minSubsets(input):

 

 # calculate frequency of each element

 freqDict = Counter(input)

 

 # get list of all frequency values

 # print maximum from it 

 print (max(freqDict.values()))

 

# Driver program

if __name__ == "__main__":

 input = [1, 2, 3, 3]

 minSubsets(input)  
  
---  
  
 __

 __

Output:

    
    
    2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

