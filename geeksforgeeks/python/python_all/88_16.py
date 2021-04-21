Python Program to Generate Random binary string



Given a number n, the task is to generate a random binary string of length n.

 **Examples:**

    
    
    **Input:** 7
    **Output:** Desired length random binary string is:  1000001
    
    **Input:** 5
    **Output:** Desired length random binary string is:  01001
    

**Approach**

  * Initialize an empty string, say key
  * Generate a randomly either “0” or “1” using randint function from random package.
  * Append the randomly generated “0” or “1” to the string, key
  * Repeat step 2 and 3 for the desired length of the string

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for random

# binary string generation

 

 

import random

 

 

# Function to create the

# random binary string

def rand_key(p):

 

 # Variable to store the 

 # string

 key1 = ""

 

 # Loop to find the string

 # of desired length

 for i in range(p):

 

 # randint function to generate

 # 0, 1 randomly and converting 

 # the result into str

 temp = str(random.randint(0, 1))

 

 # Concatenatin the random 0, 1

 # to the final result

 key1 += temp

 

 return(key1)

 

# Driver Code

n = 7

str1 = rand_key(n)

print("Desired length random binary string is: ", str1)  
  
---  
  
 __

 __

 **Output:**

    
    
    Desired length random binary string is:  1000001

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

