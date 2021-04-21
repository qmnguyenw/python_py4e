Python | Ways to convert hex into binary



Conversion of hex to binary is a very common programming question. In this
article, we will see a few methods to solve the above problem.

 **Method #1: Using bin and zfill**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of a hex string

# to the binary string

 

# Initialising hex string

ini_string = "1a"

scale = 16

 

# Printing initial string

print ("Initial string", ini_string)

 

# Code to convert hex to binary

res = bin(int(ini_string, scale)).zfill(8)

 

# Print the resultant string

print ("Resultant string", str(res))  
  
---  
  
 __

 __

 **Output:**

> Initial string 1a  
> Resultant string 00b11010

  
**Method #2: Using Naive Method**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of hex string

# to binary string

 

import math

 

# Initialising hex string

ini_string = "1a"

 

# Printing initial string

print ("Initial string", ini_string)

 

# Code to convert hex to binary

n = int(ini_string, 16) 

bStr = ''

while n > 0:

 bStr = str(n % 2) + bStr

 n = n >> 1

res = bStr

 

# Print the resultant string

print ("Resultant string", str(res))  
  
---  
  
 __

 __

 **Output:**

> Initial string 1a  
> Resultant string 11010

  
**Method #3: Using .format**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of hex string

# to binary string

 

import math

 

# Initialising hex string

ini_string = "1a"

 

# Printing initial string

print ("Initial string", ini_string)

 

# Code to convert hex to binary

res = "{0:08b}".format(int(ini_string, 16))

 

# Print the resultant string

print ("Resultant string", str(res))  
  
---  
  
 __

 __

 **Output:**

> Initial string 1a  
> Resultant string 00011010

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

