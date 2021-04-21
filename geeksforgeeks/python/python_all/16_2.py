Python program to find the sum of sine series



 **Prerequisite:** **math**

Given n and x, where n is the number of terms in the series and x is the value
of the angle in degree. The Task here is, write a program to calculate the sum
of sine series of x.

 **Formula Used:**

![sinx=x-\(x3/3!\)+\(x5/5!\)-\(x7/7!\)+…](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-9dcf9a50f63a992f4a2c0b745c04cc89_l3.png)

 **Example:**

  

  

    
    
     **Input:** n = 10
            x = 30
    **Ouput:** sum of sine series is 0.5 
    
    **Input:** n = 10
            x = 60
    **Ouput:** sum of sine series is 0.87

 **Below is the program to calculate the sum of sine series:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import Module

import math

 

# Create sine function

def sin( x, n):

 sine = 0

 for i in range(n):

 sign = (-1)**i

 pi = 22/7

 y = x*(pi/180)

 sine +=
((y**(2.0*i+1))/math.factorial(2*i+1))*sign


 return sine

 

# driver nodes

# Enter value in degree in x

x = 10

 

# Enter number of terms

n = 90

 

# call sine function

print(round(sin(x,n),2))  
  
---  
  
 __

 __

 **Output:**

    
    
    0.17

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

