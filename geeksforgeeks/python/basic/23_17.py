Print first m multiples of n without using any loop in Python



Given n and m, print first m multiples of a m number without using any loops
in Python.

Examples:

    
    
    Input : n = 2, m = 3
    Output : 2 4 6 
    
    Input : n = 3, m = 4
    Output : 3 6 9 12 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We can use range() function in Python to store the multiples in a range.  
First we store the numbers till m multiples using range() function in an
array, and then print the array with using **(*a)** which print the array
without using loop.

Below is the Python implementation of the above approach:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# function to print the first m multiple

# of a number n without using loop.

def multiple(m, n):

 

 # inserts all elements from n to 

 # (m * n)+1 incremented by n.

 a = range(n, (m * n)+1, n)

 

 print(*a)

 

# driver code 

m = 4

n = 3

multiple(m, n)  
  
---  
  
 __

 __

 **Output:**

    
    
    3 6 9 12
    

**Note :** In Python 3, print(*(range(x)) is equivalent to print("
".join([str(i) for i in range(x)]))

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

