Python | Find common elements in three sorted arrays by dictionary
intersection



Given three arrays sorted in non-decreasing order, print all common elements
in these arrays.

Examples:

    
    
    Input:  ar1 = [1, 5, 10, 20, 40, 80]
            ar2 = [6, 7, 20, 80, 100]
            ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    Output: [80, 20]
    
    Input:  ar1 = [1, 5, 5]
            ar2 = [3, 4, 5, 5, 10]
            ar3 = [5, 5, 10, 20]
    Output: [5, 5]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Find common elements
in three sorted arrays link. We can solve this problem quickly in python using
**intersection** of dictionaries. Approach is simple,

  1. First convert all three lists into dictionaries having elements as keys and their frequencies as value, using Counter() method.
  2. Now perform intersection operation for three dictionaries, this will result us dictionary having common elements among three array list with their frequencies.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find common elements in three

# sorted arrays

from collections import Counter

 

def commonElement(ar1,ar2,ar3):

 # first convert lists into dictionary

 ar1 = Counter(ar1)

 ar2 = Counter(ar2)

 ar3 = Counter(ar3)

 

 # perform intersection operation

 resultDict = dict(ar1.items() & ar2.items() & ar3.items())

 common = []

 

 # iterate through resultant dictionary

 # and collect common elements

 for (key,val) in resultDict.items():

 for i in range(0,val):

 common.append(key)

 

 print(common)

 

# Driver program

if __name__ == "__main__":

 ar1 = [1, 5, 10, 20, 40, 80]

 ar2 = [6, 7, 20, 80, 100]

 ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

 commonElement(ar1,ar2,ar3)  
  
---  
  
 __

 __

Output:

    
    
    [80, 20]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

