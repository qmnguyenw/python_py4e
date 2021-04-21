Generate all permutation of a set in Python



Permutation is an arrangement of objects in a specific order. Order of
arrangement of object is very important. The number of permutations on a set
of n elements is given by n!. For example, there are 2! = 2*1 = 2 permutations
of {1, 2}, namely {1, 2} and {2, 1}, and 3! = 3*2*1 = 6 permutations of {1, 2,
3}, namely {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2} and {3, 2,
1}.

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.

 **Method 1 (Backtracking)**  
We can use the backtracking based recursive solution discussed here.

 **Method 2**  
The idea is to one by one extract all elements, place them at first position
and recur for remaining list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python function to print permutations of a given list

def permutation(lst):

 

 # If lst is empty then there are no permutations

 if len(lst) == 0:

 return []

 

 # If there is only one element in lst then, only

 # one permuatation is possible

 if len(lst) == 1:

 return [lst]

 

 # Find the permutations for lst if there are

 # more than 1 characters

 

 l = [] # empty list that will store current permutation

 

 # Iterate the input(lst) and calculate the permutation

 for i in range(len(lst)):

 m = lst[i]

 

 # Extract lst[i] or m from the list. remLst is

 # remaining list

 remLst = lst[:i] + lst[i+1:]

 

 # Generating all permutations where m is first

 # element

 for p in permutation(remLst):

 l.append([m] + p)

 return l

 

 

# Driver program to test above function

data = list('123')

for p in permutation(data):

 print p  
  
---  
  
 __

 __

Output:

    
    
    ['1', '2', '3']
    ['1', '3', '2']
    ['2', '1', '3']
    ['2', '3', '1']
    ['3', '1', '2']
    ['3', '2', '1']

 **Method 3 (Direct Function)**  
We can do it by simply using the built-in permutation function in itertools
library. It is the shortest technique to find the permutation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import permutations

l = list(permutations(range(1, 4)))

print l  
  
---  
  
 __

 __

Output:

    
    
    [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 

This article is contributed by **Arpit Agarwal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

