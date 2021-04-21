Python | Number of elements to be removed such that product of adjacent
elements is always even



Given an array of N integers. The task is to eliminate the number of elements
such that in the resulting array the product of any two adjacent values is
even.

 **Examples:**

    
    
    **Input  :** arr[] = {1, 2, 3}
    **Output :** 0
    
    **Input  :** arr[] = {1, 3, 5, 4, 2}
    **Output :** 2
    Remove 1 and 3.

 **Approach:** The product of 2 numbers is even if any one of them is even.
This means for every pair of consecutive numbers if both are odd then
eliminate one of them.  
So, to make the product of the adjacent elements even, either all elements
should be even or alternative even-odd elements. So the following greedy
algorithm works:

  * Go through all the elements in order.
  * If all elements are even then “0” is returned.
  * If all elements are odd then “n” is returned.
  * Otherwise, count the number of consecutive odd pair.
  * Return the minimum count.

Below is the Python implementation –  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 implementation of the

# above approach

 

# Function to find minimum number of 

# eliminations such that product of all 

# adjacent elements is even

def min_elimination(n, arr):

 countOdd = 0

 counteven = 0

 # Stores the new value

 for i in range(n):

 

 # Count odd and even numbers

 if (arr[i] % 2):

 countOdd += 1

 else:

 counteven+= 1

 # if all are even

 if counteven == n:

 return 0

 # if all are odd

 if countOdd == n:

 return n

 else:

 countpair = 0

 for i in range(1, n):

 if (arr[i] % 2 == 1 and arr[i-1] % 2 ==
1):

 countpair+= 1

 return countpair

 

# Driver code

if __name__ == '__main__':

 arr = [1, 2, 3, 7, 9]

 n = len(arr)

 

 print(min_elimination(n, arr))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2

 **Time Complexity:** O(N )

 **Auxiliary Space:** O(N)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

