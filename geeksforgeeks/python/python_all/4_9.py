Python program to get all subsets having sum x



We are given a list of n numbers and a number x, the task is to write a python
program to find out all possible subsets of the list such that their sum is x.

 **Examples:**

>  **Input:** arr = [2, 4, 5, 9], x = 15
>
>  **Output:** [2, 4, 9]
>
> 15 can be obtained by adding 2, 4 and 9 from the given list.
>
>  
>
>
>  
>
>
>  **Input :** arr = [10, 20, 25, 50, 70, 90], x = 80
>
>  **Output :** [10, 70]
>
> [10, 20, 50]
>
> 80 can be obtained by adding 10 and 70 or by adding 10, 20 and 50 from the
> given list.

 **Approach #1:**

It is a Brute Force approach. Find all possible subset sums of the given list
and check if the sum is equal to x. The time complexity using this approach
would be O(2^n) which is quite large.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code with time complexity

# O(2^n)to print all subsets whose

# sum is equal to a given value

from itertools import combinations

 

 

def subsetSum(n, arr, x):

 

 # Iterating through all possible

 # subsets of arr from lengths 0 to n:

 for i in range(n+1):

 for subset in combinations(arr, i):

 

 # printing the subset if its sum is x:

 if sum(subset) == x:

 print(list(subset))

 

 

# Driver Code:

n = 6

arr = [10, 20, 25, 50, 70, 90]

x = 80

subsetSum(n, arr, x)  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 70]
    [10, 20, 50]

 **Approach #2:**

Meet in the middle is a technique that divides the search space into two
equal-sized parts, performs a separate search on both the parts and then
combines the search results. Using this technique, the two searches may
require less time than one large search and turn the time complexity from
O(2^n) to O(2^(n/2)).

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Efficient Python code to

# print all subsets whose sum

# is equal to a given value

from itertools import combinations

 

 

def subsetSum(li, comb, sums):

 # Iterating through all subsets of

 # list li from length 0 to length of li:

 for i in range(len(li)+1):

 for subset in combinations(li, i):

 

 # Storing all the subsets in list comb:

 comb.append(list(subset))

 

 # Storing the subset sums in list sums:

 sums.append(sum(subset))

 

 

def calcSubsets(n, arr, x):

 

 # Dividing the list arr into two lists

 # arr1 and arr2 of about equal sizes

 # by slicing list arr about index n//2:

 arr1, arr2 = arr[:n//2], arr[n//2:]

 

 # Creating empty lists comb1 and sums1

 # to run the subsetSum function and

 # store subsets of arr1 in comb1

 # and the subset sums in sums1:

 comb1, sums1 = [], []

 subsetSum(arr1, comb1, sums1)

 

 # Creating empty lists comb2 and sums2

 # to run the subsetSum function and

 # store subsets of arr2 in comb2

 # and the subset sums in sums2:

 comb2, sums2 = [], []

 subsetSum(arr2, comb2, sums2)

 

 # Iterating i through the indices of sums1:

 for i in range(len(sums1)):

 

 # Iterating j through the indices of sums2:

 for j in range(len(sums2)):

 

 # If two elements (one from sums1

 # and one from sums2) add up to x,

 # the combined list of elements from

 # corresponding subsets at index i in comb1

 # and j in comb2 gives us the required answer:

 if sums1[i] + sums2[j] == x:

 print(comb1[i] + comb2[j])

 

 

# Driver Code:

n = 6

arr = [10, 20, 25, 50, 70, 90]

x = 80

calcSubsets(n, arr, x)  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 70]
    [10, 20, 50]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

