Python Program for Egg Dropping Puzzle | DP-11



The following is a description of the instance of this famous puzzle involving
n=2 eggs and a building with k=36 floors.

Suppose that we wish to know which stories in a 36-story building are safe to
drop eggs from, and which will cause the eggs to break on landing. We make a
few assumptions:

…..An egg that survives a fall can be used again.  
…..A broken egg must be discarded.  
…..The effect of a fall is the same for all eggs.  
…..If an egg breaks when dropped, then it would break if dropped from a higher
floor.  
…..If an egg survives a fall then it would survive a shorter fall.  
…..It is not ruled out that the first-floor windows break eggs, nor is it
ruled out that the 36th-floor do not cause an egg to break.

If only one egg is available and we wish to be sure of obtaining the right
result, the experiment can be carried out in only one way. Drop the egg from
the first-floor window; if it survives, drop it from the second floor window.
Continue upward until it breaks. In the worst case, this method may require 36
droppings. Suppose 2 eggs are available. What is the least number of egg-
droppings that is guaranteed to work in all cases?  
The problem is not actually to find the critical floor, but merely to decide
floors from which eggs should be dropped so that total number of trials are
minimized.

Source: Wiki for Dynamic Programming

  

  

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

 **Dynamic Programming Solution**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Dynamic Programming based Python

# Program for the Egg Dropping Puzzle

INT_MAX = 32767

 

# Function to get minimum number of trials needed in worst

# case with n eggs and k floors

def eggDrop(n, k):

 # A 2D table where entery eggFloor[i][j] will represent minimum

 # number of trials needed for i eggs and j floors.

 eggFloor = [[0 for x in range(k + 1)] for x
in range(n + 1)]

 

 # We need one trial for one floor and0 trials for 0 floors

 for i in range(1, n + 1):

 eggFloor[i][1] = 1

 eggFloor[i][0] = 0

 

 # We always need j trials for one egg and j floors.

 for j in range(1, k + 1):

 eggFloor[1][j] = j

 

 # Fill rest of the entries in table using optimal substructure

 # property

 for i in range(2, n + 1):

 for j in range(2, k + 1):

 eggFloor[i][j] = INT_MAX

 for x in range(1, j + 1):

 res = 1 + max(eggFloor[i-1][x-1],
eggFloor[i][j-x])

 if res < eggFloor[i][j]:

 eggFloor[i][j] = res

 

 # eggFloor[n][k] holds the result

 return eggFloor[n][k]

 

# Driver program to test to pront printDups

n = 2

k = 36

print("Minimum number of trials in worst case with" + str(n) +
"eggs and "

 + str(k) + " floors is " + str(eggDrop(n, k)))

 

# This code is contributed by Bhavya Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    Minimum number of trials in worst case with2eggs and 36 floors is 8
    

Please refer complete article on Egg Dropping Puzzle | DP-11 for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

