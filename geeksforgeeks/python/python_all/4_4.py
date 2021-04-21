Python program to sort digits of a number in ascending order



Given an integer **N** , the task is to sort the digits in ascending order.
Print the new number obtained after excluding leading zeroes.

 **Examples:**

>  **Input:** N = 193202042  
>  **Output:** 1222349  
>  **Explanation:**  
>  Sorting all digits of the given number generates 001222349.  
> Final number obtained after removal of leading 0s is 1222349.
>
>  **Input:** N = 78291342023  
>  **Output:** 1222334789

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Follow the steps below to solve the problem:

  

  

  * Convert the given integer to its equivalent string
  * Sort the characters of the string using **join()**and **sorted()** **.**
  * Convert string to integer using type casting
  * Print the integer obtained.

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# implement the above approach

 

# Function to sort the digits

# present in the number n

def getSortedNumber(n):

 

 # Convert to equivalent string

 number = str(n)

 

 # Sort the string

 number = ''.join(sorted(number))

 

 # Convert to equivalent integer

 number = int(number)

 

 # Return the integer

 return number

 

 

# Driver Code

n = 193202042

 

print(getSortedNumber(n))  
  
---  
  
 __

 __

 **Output:**

    
    
    1222349
    

_**Time Complexity:** O(N*log(N))_  
 _ **Auxiliary Space:** O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

