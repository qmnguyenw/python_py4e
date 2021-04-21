Python Program for Check if count of divisors is even or odd



Given a number “n”, find its total number of divisors are even or odd.

Examples :

    
    
    Input  : n = 10      
    Output : Even
    
    Input:  n = 100
    Output: Odd
    
    Input:  n = 125
    Output: Even

A **naive approach** would be to find all the divisors and then see if the
total number of divisors is even or odd.

Time complexity for such a solution would be O(sqrt(n))

 __

 __  
 __

 __

 __  
 __  
 __

# Naive Solution to

# find if count of 

# divisors is even

# or odd

import math

 

# Function to count 

# the divisors

def countDivisors(n) :

 

 # Initialize count 

 # of divisors

 count = 0

 

 # Note that this loop 

 # runs till square 

 # root

 for i in range(1, (int)(math.sqrt(n)) + 2) :

 if (n % i == 0) :

 

 # If divisors are

 # equal,increment

 # count by one

 # Otherwise increment

 # count by 2

 if( n // i == i) :

 count = count + 1

 else :

 count = count + 2

 

 if (count % 2 == 0) :

 print("Even")

 else :

 print("Odd")

 

 

# Driver program to test above function */

print("The count of divisor: ")

countDivisors(10)

 

#This code is contributed by Nikita Tiwari.*/  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The count of divisor: Even 

**Efficient Solution:**  
We can observe that the number of divisors is odd only in case of perfect
squares. Hence the best solution would be to check if the given number is
perfect square or not. If it\’s a perfect square, then the number of divisors
would be odd, else it\’d be even.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for

# Efficient Solution to find

# find if count of divisors

# is even or odd

 

# Python program for

# Efficient Solution to find

# find if count of divisors

# is even or odd

 

def NumOfDivisor(n):

 if n < 1:

 return

 root_n = n**0.5

 

 # If n is a perfect square,

 # then it has odd divisors

 if root_n**2 == n:

 print("Odd")

 else:

 print("Even")

 

# Driver code 

if __name__ == '__main__':

 print("The count of divisor"+

 "of 10 is: ")

 NumOfDivisor(10)

 

# This code is contributed by Yt R 

   
  
---  
  
__

__

**Output :**

    
    
    The count of divisorof 10 is: 
    Even 

Please refer complete article on Check if count of divisors is even or odd for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

