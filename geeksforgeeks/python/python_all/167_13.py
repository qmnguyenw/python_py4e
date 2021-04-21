Count distinct elements in an array in Python



Given an unsorted array, count all distinct elements in it.

 **Examples:**

    
    
    **Input : arr[] = {10, 20, 20, 10, 30, 10}** 
    **Output : 3**
    
    **Input : arr[] = {10, 20, 20, 10, 20}**
    **Output : 2**
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this article. We can solve this problem in
Python3 using Counter method.

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

def countDistinct(arr):

 

 # counter method gives dictionary of elements in list

 # with their corresponding frequency.

 # using keys() method of dictionary data structure

 # we can count distinct values in array

 return len(Counter(arr).keys()) 

 

if __name__=="__main__":

 arr = [10, 20, 20, 10, 30, 10]

 print (countDistinct(arr))  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

