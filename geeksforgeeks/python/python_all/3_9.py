Python Program to get all unique keys from a List of Dictionaries



Given a list **arr[]** consisting of **N** dictionaries, the task is to find
the sum of unique keys from the given list of the dictionary.

 **Examples:**

>  **Input:** arr = [{‘my’: 1, ‘name’: 2}, {‘is’: 1, ‘my’: 3}, {‘ria’: 2}]  
>  **Output:** [‘ria’, ‘my’, ‘is’, ‘name’]  
>  **Explanation:** The set of unique keys are {“ria”, “my”, “Is”, “name”}.
>
>  **Input:** arr = [{‘X’: 100, ‘Y’: 2}, {‘Z’: 1, ‘Z’: 30}, {‘X’: 21}]  
>  **Output:** [‘Z’, ‘X’, ‘Y’]  
>  **Explanation:** The set of unique keys are {“X”, “Y”, “Z”}.

 **Approach usingChain iterable tools: **The problem can be solved using
_set()_ and keys() methods and chain iterable tools to solve the above
problem.

  

  

Follow the steps below to solve the problem:

  * Traverse all keys of every dictionary using **chain iterable tools**
  * Store the set of keys in a list, say **res**.
  * Print the list **res** as the required answer.

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for the above approach

from itertools import chain

 

 

# Function to print all unique keys

# present in a list of dictionaries

def UniqueKeys(arr):

 

 # Stores the list of unique keys

 res = list(set(chain.from_iterable(sub.keys() for sub in
arr)))

 

 # Print the list

 print(str(res))

 

# Driver Code

arr = [{'my': 1, 'name': 2}, 

 {'is': 1, 'my': 3},

 {'ria': 2}]

UniqueKeys(arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['is', 'ria', 'my', 'name']
    

_**Time Complexity:** O(N * maxm), where **maxm** denotes the size of the
longest dictionary.  
 **Auxiliary Space:** O(N * maxm)_

 **Approach usingList Comprehension and Dictionary Comprehension: **The
problem can be solved alternately using set() and keys() method and list
comprehension and dictionary comprehension to solve the problem.

Follow the steps below to solve the problem:

  * Traverse all the keys of every dictionary using List Comprehension and Dictionary Comprehension and then store the set of keys in a list, say **res**.
  * Print the list **res** as the required answer.

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for the above approach

 

from itertools import chain

 

# Function to print all unique keys

# from a list of dictionaries

def UniqueKeys(arr):

 

 # Stores the list of unique keys

 res = list(set(val for dic in arr for val in
dic.keys()))

 

 # Print the list

 print(str(res))

 

# Driver Code

 

# Input

arr = [{'my': 1, 'name': 2}, 

 {'is': 1, 'my': 3},

 {'ria': 2}]

 

UniqueKeys(arr)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['ria', 'my', 'name', 'is']
    

_**Time Complexity:** O(N * maxm), where **maxm** denotes the size of the
longest dictionary.  
 **Auxiliary Space:** O(N * maxm)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

