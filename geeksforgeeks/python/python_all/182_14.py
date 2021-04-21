Python Program for Maximum height when coins are arranged in a triangle



We have N coins which need to arrange in form of a triangle, i.e. first row
will have 1 coin, second row will have 2 coins and so on, we need to tell
maximum height which we can achieve by using these N coins.

Examples:

    
    
    Input : N = 7
    Output : 3
    Maximum height will be 3, putting 1, 2 and
    then 3 coins. It is not possible to use 1 
    coin left.
    
    Input : N = 12
    Output : 4
    Maximum height will be 4, putting 1, 2, 3 and 
    4 coins, it is not possible to make height as 5, 
    because that will require 15 coins.
    

__

__  
__

__

__  
__  
__

# Python3 program to find

# maximum height of arranged

# coin triangle

 

# Returns the square root of n.

# Note that the function 

def squareRoot(n):

 

 # We are using n itself as

 # initial approximation

 # This can definitely be improved 

 x = n 

 y = 1

 

 e = 0.000001 # e decides the accuracy level 

 while (x - y > e):

 x = (x + y) / 2

 y = n/x

 

 return x 

 

 

# Method to find maximum height

# of arrangement of coins

def findMaximumHeight(N):

 

 # calculating portion inside the square root

 n = 1 + 8*N 

 maxH = (-1 + squareRoot(n)) / 2

 return int(maxH) 

 

 

# Driver code to test above method

N = 12

print(findMaximumHeight(N))

 

# This code is contributed by

# Smitha Dinesh Semwal  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

Please refer complete article on Maximum height when coins are arranged in a
triangle for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

