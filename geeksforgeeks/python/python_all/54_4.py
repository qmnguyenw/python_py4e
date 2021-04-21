Python program to Find the Jumbo GCD subarray



Given an array, write a program to find the maximum GCD among all the subarray
of the size >= 2 of the given array.

 **Examples:**

    
    
     **Input list:** [2, 3, 4, 4, 4]
    **Output:** 4
    
    **Input list:** [3, 7, 2, 9, 18, 5, 1, 13 ]
    **Output:** 9

### Approach:

  * Import the math module for python
  * Introduce a variable(say, V1) to store the gcd of each element of the list while looping through the list.
  * Iterate through the elements of the array or list using a loop.
  * At each iteration call the _**math.gcd() function.**_
  * Store the outcome of the math.gcd() function to another variable (say, V2) at each iteration.
  * Now compare V1 and V2. If V2 is greater than V1, set V1 equal to V2 else pass.
  * Let the loop run through and print out the final value of V1.

Below you can find the implementation of the above-mentioned approach:  
 **Examples 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import math

 

# input list

List = [2, 3, 4, 4, 4 ]

 

max1 = 0

for i in range(len(List)-1):

 

 # use math.gcd() function

 gcd1 = math.gcd(List[i], List[i + 1])

 if(gcd1>max1):

 max1 = gcd1

 

# print max1

# as the result

print(max1)  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Explanation:**  
For the given array one of the subarrays having maximum gcd is[3, 5] which has
gcd 4.

  

  

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import math

 

# input list

List = [3, 7, 2, 9, 18, 5, 1, 13 ]

 

max1 = 0

for i in range(len(List)-1):

 

 # use math.gcd() function

 gcd1 = math.gcd(List[i], List[i + 1])

 if(gcd1>max1):

 max1 = gcd1

 

# print max1

# as the result

print(max1)  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    

**Explanation:**  
For the given array one of the subarrays having maximum gcd is[4, 5] which has
gcd 9.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

