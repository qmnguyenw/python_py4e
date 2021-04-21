Determining the inconsistently weighted object



Given N objects numbered from 1 to N out of which all are of the same weights
except only one object which is not known beforehand. We are also given Q
comparisons, in each of which an equal number of objects are placed on both
sides of a balance scale, and we are told the heavier side.

The task is to find the inconsistently weighted object or determine if the
data is not sufficient enough.

 **Examples** :

    
    
    **Input** : N = 6
    Q = 3
    1 2 = 5 6
    1 2 3 > 4 5 6
    3 4 < 5 6
    **Output** : 4
    **Explanation** : Object 4 is lighter than all other objects.
    
    **Input** : N = 10
    Q = 4
    1 2 3 4 < 7 8 9 10
    1 = 9
    2 3 4 > 1 5 10
    6 = 2
    **Output** : Insufficient data
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

It is told that except only one element, the rest of the elements are of the
same weights. So, if we observe carefully, it can be said that:

  1. In a ‘=’ comparison, none of the objects on both sides is the inconsistently weighted one.
  2. If an object appears on the heavier side in one comparison and on the lighter side in another, then it is not the inconsistently weighted object. This is because, if an object appears on the heavier side then it is of the maximum weight and if it appears on the lighter side then it is of the minimum weight. Since a single element can’t be both maximum and minimum at the same time. So, this case will never occur.
  3. The inconsistently weighted object must appear in all of the non-balanced (‘>’ or ‘<') comparisons.

We can use the above three observations to narrow down the potential
candidates for the inconsistently weighted object. We will consider only those
objects which are either on the heavier side or the lighter side; if there is
only one such object then it is the required one. If there is no such object,
then we will consider all those objects which do not appear in any comparison.
If there is only one such object then it is the inconsistently weighted
object. If none of these scenarios arises, the data is insufficient.

  

  

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to determine the

# inconsistently weighted object 

 

# Function to get the difference of two lists 

def subt(A, B): 

 return list(set(A) - set(B)) 

 

# Function to get the intersection of two lists 

def intersection(A, B): 

 return list(set(A).intersection(set(B))) 

 

# Function to get the intersection of two lists 

def union(A, B): 

 return list(set(A).union(set(B))) 

 

# Function to find the inconsistently weighted object 

def inconsistentlyWeightedObject(N, Q, comparisons): 

 # Objects which appear on the heavier side 

 heavierObj = [i for i in range(1, N + 1)] 

 

 # Objects which appear on the lighter side 

 lighterObj = [i for i in range(1, N + 1)] 

 equalObj = [] # Objects which appear in '=' comparisons 

 

 # Objects which don't appear in any comparison 

 objectNotCompared = [i for i in range(1, N + 1)] 

 

 for c in comparisons: 

 objectNotCompared = subt(objectNotCompared, union(c[0], c[2]))


 

 if c[1] == '=': 

 equalObj = union(equalObj, union(c[0], c[2])) 

 elif c[1] == '<': 

 # Removing those objects which do 

 # not appear on the lighter side 

 lighterObj = intersection(lighterObj, c[0]) 

 

 # Removing thoe objects which do 

 # not appear on the heavier side 

 heavierObj = intersection(heavierObj, c[2]) 

 else: 

 # Removing those objects which do 

 # not appear on the lighter side 

 lighterObj = intersection(lighterObj, c[2]) 

 

 # Removing those objects which do 

 # not appear on the heavier side 

 heavierObj = intersection(heavierObj, c[0]) 

 

 L_iwo = subt(union(heavierObj, lighterObj), equalObj) # Potential
candidates 

 

 if len(L_iwo) == 1: 

 return L_iwo[0] 

 elif not len(L_iwo): 

 if len(objectNotCompared) == 1: 

 return objectNotCompared[0] 

 else: 

 return 'Insufficient data'

 else: 

 return 'Insufficient data'

 

 

# Driver code 

N = 6

Q = 3

comparisons = [ [[1, 2], '=', [5, 6]], [[1,
2, 3], '>', [4, 5, 6]], 

 [[3, 4], '<', [5, 6]] ] 

print(inconsistentlyWeightedObject(N, Q, comparisons))   
  
---  
  
__

__

**Output:**

    
    
    4
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

