Sum of all array elements less than X and greater than Y for Q queries



Given a sorted array **arr[],** and a set **Q** having **M** queries, where
each query has values **X** and **Y** , the task is to find the sum of all
integers less than **X** and greater than **Y** present in the array.  
 **Note:** X and Y may or may not be present in the array.

 **Examples:**

>  **Input:** arr[] = [3 5 8 12 15], Q = {{5, 12}, {4, 8}}  
>  **Output:**  
>  18  
> 30  
>  **Explanation:**  
>  For query 1, X = 5 and Y = 12. Sum = 3( < 5) + 15( > 12) = 18.  
> For query 2, X = 4 and Y = 8. Sum = 3( < 4) + 15 ( > 8) + 12 ( > 8) = 30.
>
>  **Input:** arr[] = [4 7 7 12 15], Q = {{3, 8}, {4, 8}}  
>  **Output:**  
>  27  
> 27  
>  **Explanation:**  
>  For query 1, X = 3 and Y = 8. Sum = 12( > 8) + 15 ( > 8) = 27.  
> For query 2, Sum = 12 + 15 = 27.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  1. Build a prefix sum array where **prefix_sum[i]** denotes the sum of **arr[0] + arr[1] + … arr[i]**.
  2. Find the last index **i** which has a value less than **X** and extract the prefix sum up to the **i th** index. The index can be obtained in _O(logN)_ complexity by using **bisect_left()** or lower_bound() in Python and C++ respectively..
  3. Similarly, find the first index **i** in the array with a value greater than Y and calculate the sum **prefix_sum[n-1] – prefix_sum[i-1]**. Inbuilt functions bisect() and upper_bound() in Python and C++ respectively, perform the required operation in _O(logN)_.
  4. Sum of the two results calculated in the above two steps is the required answer. Keep repeating these steps for every query.

Below is the implementation of the above approach:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for the above program

from bisect import bisect, bisect_left

 

def createPrefixSum(ar, n):

 

 # Initialize prefix sum 

 # array

 prefix_sum = [0]*n

 

 # Initialize prefix_sum[0]

 # by ar[0]

 prefix_sum[0] = ar[0]

 

 # Compute prefix sum for

 # all indices 

 for i in range(1, n):

 prefix_sum[i] = prefix_sum[i-1]+ar[i]

 return prefix_sum

 

# Function to return sum of all

# elements less than X

def sumLessThanX(ar, x, prefix_xum):

 

 # Index of the last element 

 # which is less than x

 pos_x = bisect_left(ar, x) - 1

 

 

 if pos_x >= 0 :

 return prefix_sum[pos_x]

 # If no element is less than x

 else:

 return 0

 

# Function to return sum of all

# elements greater than Y

def sumGreaterThanY(ar, y, prefix_sum):

 

 # Index of the first element 

 # which is greater than y

 pos_y = bisect(ar, y)

 pos_y -= 1

 

 if pos_y < len(ar)-1 :

 return prefix_sum[-1]-prefix_sum[pos_y]

 # If no element is greater than y

 else:

 return 0

 

 

def solve(ar, x, y, prefix_sum):

 ltx = sumLessThanX(ar, x, prefix_sum)

 gty = sumGreaterThanY(ar, y, prefix_sum)

 

 # printing the final sum

 print(ltx + gty) 

 

 

def print_l(lb, ub):

 print("sum of integers less than {}".format(lb)

 + " and greater than {} is ".format(ub),

 end = '')

 

 

if __name__ == '__main__':

 

 # example 1

 ar = [3, 6, 6, 12, 15]

 n = len(ar)

 prefix_sum = createPrefixSum(ar, n)

 

 # for query 1

 q1x = 5

 q1y = 12

 print_l(q1x, q1y)

 solve(ar, q1x, q1y, prefix_sum)

 

 # for query 2

 q2x = 7

 q2y = 8

 print_l(q2x, q2y)

 solve(ar, q2x, q2y, prefix_sum)  
  
---  
  
 __

 __

 **Output:**

    
    
    sum of integers less than 5 and greater than 12 is 18
    sum of integers less than 7 and greater than 8 is 42
    

_  
**Time Complexity:** O(N + (M * logN))  
 **Auxiliary Space complexity:** O(N)  
_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

