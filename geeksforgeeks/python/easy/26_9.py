itertools.combinations() module in Python to print all possible combinations



Given an array of size n, generate and print all possible combinations of r
elements in array.

Examples:

    
    
    Input : arr[] = [1, 2, 3, 4],  
                r = 2
    Output : [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing recursive solution please refer Print all possible
combinations of r elements in a given array of size n link. We will solve this
problem in python using **itertools.combinations()** module.

### What does itertools.combinations() do ?

It returns r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sort order. So, if the input
iterable is sorted, the combination tuples will be produced in sorted order.

  

  

  *  ** _itertools.combinations(iterable, r) :_**  
It return r-length tuples in sorted order with no repeated elements. For
Example, combinations(‘ABCD’, 2) ==> [AB, AC, AD, BC, BD, CD].

  *  ** _itertools.combinations_with_replacement(iterable, r) :_**  
It return r-length tuples in sorted order with repeated elements. For Example,
combinations_with_replacement(‘ABCD’, 2) ==> [AA, AB, AC, AD, BB, BC, BD, CC,
CD, DD].

 __

 __  
 __

 __

 __  
 __  
 __

# Function which returns subset or r length from n

from itertools import combinations

 

def rSubset(arr, r):

 

 # return list of all subsets of length r

 # to deal with duplicate subsets use 

 # set(list(combinations(arr, r)))

 return list(combinations(arr, r))

 

# Driver Function

if __name__ == "__main__":

 arr = [1, 2, 3, 4]

 r = 2

 print (rSubset(arr, r))  
  
---  
  
 __

 __

Output:

    
    
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    

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

