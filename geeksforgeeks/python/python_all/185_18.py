Python Program for Subset Sum Problem | DP-25



Given a set of non-negative integers, and a value _sum_ , determine if there
is a subset of the given set with sum equal to given _sum_.  
 **Example:**

    
    
    Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
    Output:  True  //There is a subset (4, 5) with sum 9.
    

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

Following is naive recursive implementation that simply follows the recursive
structure mentioned above.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A recursive solution for subset sum

# problem

 

# Returns true if there is a subset 

# of set[] with sun equal to given sum

def isSubsetSum(set, n, sum) :

 

 # Base Cases

 if (sum == 0) :

 return True

 if (n == 0 and sum != 0) :

 return False

 

 # If last element is greater than

 # sum, then ignore it

 if (set[n - 1] > sum) :

 return isSubsetSum(set, n - 1, sum);

 

 # else, check if sum can be obtained

 # by any of the following

 # (a) including the last element

 # (b) excluding the last element 

 return isSubsetSum(set, n-1, sum) or
isSubsetSum(set, n-1, sum-set[n-1])

 

 

# Driver program to test above function

set = [3, 34, 4, 12, 5, 2]

sum = 9

n = len(set)

if (isSubsetSum(set, n, sum) == True) :

 print("Found a subset with given sum")

else :

 print("No subset with given sum")

 

# This code is contributed by Nikita Tiwari.  
  
---  
  
 __

 __

 **Output:**

    
    
    Found a subset with given sum
    

**We can solve the problem inPseudo-polynomial time using Dynamic
programming.**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Dynamic Programming solution for subset sum problem

# Returns true if there is a subset of 

# set[] with sun equal to given sum 

 

# Returns true if there is a subset of set[] 

# with sun equal to given sum

def isSubsetSum(set, n, sum):

 

 # The value of subset[i][j] will be 

 # true if there is a

 # subset of set[0..j-1] with sum equal to i

 subset =([[False for i in range(sum + 1)] 

 for i in range(n + 1)])

 

 # If sum is 0, then answer is true 

 for i in range(n + 1):

 subset[i][0] = True

 

 # If sum is not 0 and set is empty, 

 # then answer is false 

 for i in range(1, sum + 1):

 subset[0][i]= False

 

 # Fill the subset table in bottom up manner

 for i in range(1, n + 1):

 for j in range(1, sum + 1):

 if j<set[i-1]:

 subset[i][j] = subset[i-1][j]

 if j>= set[i-1]:

 subset[i][j] = (subset[i-1][j] or

 subset[i - 1][j-set[i-1]])

 

 # uncomment this code to print table 

 # for i in range(n + 1):

 # for j in range(sum + 1):

 # print (subset[i][j], end =" ")

 # print()

 return subset[n][sum]

 

# Driver program to test above function

if __name__=='__main__':

 set = [3, 34, 4, 12, 5, 2]

 sum = 9

 n = len(set)

 if (isSubsetSum(set, n, sum) == True):

 print("Found a subset with given sum")

 else:

 print("No subset with given sum")

 

# This code is contributed by 

# sahil shelangia.   
  
---  
  
__

__

**Output:**

    
    
    Found a subset with given sum
    

Please refer complete article on Subset Sum Problem | DP-25 for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

