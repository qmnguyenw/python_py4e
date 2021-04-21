Count frequencies of all elements in array in Python using collections module



Given an unsorted array of n integers which can contains n integers. Count
frequency of all elements that are present in array.  
Examples:

    
    
    Input : arr[] = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
    Output : 1 -> 4
             2 -> 4
             3 -> 2
             4 -> 1
             5 -> 2
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem can be solved in many ways, refer Count frequencies of all
elements in array link. In Python, we can quickly solve this problem in using
Collections module.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to count frequency of each element

import collections

 

# it returns a dictionary data structure whose 

# keys are array elements and values are their 

# corresponding frequencies {1: 4, 2: 4, 3: 2, 

# 5: 2, 4: 1}

def CountFrequency(arr):

 return collections.Counter(arr) 

 

# Driver function

if __name__ == "__main__":

 

 arr = [1, 1, 1, 1, 2, 2, 2, 2, 3,
3, 4, 5, 5]

 freq = CountFrequency(arr)

 

 # iterate dictionary named as freq to print

 # count of each element

 for (key, value) in freq.items():

 print (key, " -> ", value)  
  
---  
  
 __

 __

Output:

    
    
    1 -> 4
    2 -> 4
    3 -> 2
    4 -> 1
    5 -> 2
    

  

  

**Related Article :**  
Counting the frequencies in a list using dictionary in Python

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

