Python | Generate random numbers within a given range and store in a list



Given lower and upper limits, generate a given count of random numbers within
a given range, starting from ‘start’ to ‘end’ and store them in list.

Examples:

    
    
    Input : num = 10, start = 20, end = 40
    Output : [23, 20, 30, 33, 30, 36, 37, 27, 28, 38]
    The output contains 10 random numbers in
    range [20, 40].
    
    Input : num = 5, start = 10, end = 15
    Output : [15, 11, 15, 12, 11]
    The output contains 5 random numbers in
    range [10, 15].
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Python provides a random module to generate random numbers. To generate random
numbers we have used the random function along with the use of the randint
function.  
 **Syntax:**

    
    
    randint(start, end)

randint accepts two parameters: a starting point and an ending point. Both
should be integers and the first value should always be less than the second.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to generate

# random numbers and

# append them to a list

import random

 

# Function to generate

# and append them 

# start = starting range,

# end = ending range

# num = number of 

# elements needs to be appended

def Rand(start, end, num):

 res = []

 

 for j in range(num):

 res.append(random.randint(start, end))

 

 return res

 

# Driver Code

num = 10

start = 20

end = 40

print(Rand(start, end, num))  
  
---  
  
 __

 __

Output:

    
    
    [23, 20, 30, 33, 30, 36, 37, 27, 28, 38]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

