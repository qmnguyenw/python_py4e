Python Counter | Majority Element



 **Majority Element:** A majority element in an array A[] of size n is an
element that appears more than n/2 times (and hence there is at most one such
element).

Write a function which takes an array and emits the majority element (if it
exists), otherwise prints NONE as follows:

Examples:

    
    
    Input : 3 3 4 2 4 4 2 4 4
    Output : 4 
    
    Input : 3 3 4 2 4 4 2 4
    Output : NONE
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Majority Element link.
We can solve this problem quickly in Python using Counter(iterable) function.
Approach is simple,

  

  

  1. Convert given list of elements into dictionary using **Counter()** method, having elements as keys and their frequencies as value.
  2. Now traverse complete dictionary and check for element whose frequency follows the condition greater than (n/2) where n is size of list. That element will be majority element.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find majority element

from collections import Counter

 

def majority(arr):

 

 # convert array into dictionary

 freqDict = Counter(arr)

 

 # traverse dictionary and check majority element

 size = len(arr)

 for (key,val) in freqDict.items():

 if (val > (size/2)):

 print(key)

 return

 print('None')

 

# Driver program

if __name__ == "__main__":

 arr = [3,3,4,2,4,4,2,4,4] 

 majority(arr)  
  
---  
  
 __

 __

Output:

    
    
    4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

