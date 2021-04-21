atan2() function in Python



 **atan2(y, x)** returns value of atan(y/x) in radians. The atan2() method
returns a numeric value between –![\\pi](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-8874a17fc40c8e51a122ea351eb44182_l3.png) and
![\\pi](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8874a17fc40c8e51a122ea351eb44182_l3.png) representing the
angle ![\\theta](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a372b7ef1ffaec3b4ad80e0141550990_l3.png) of a (x, y)
point and positive x-axis.

 **Syntax :**

    
    
    atan2(y, x)

 **Parameter :**

    
    
     **(y, x) -** Both must be a numeric value.

 **Returns :**

    
    
    Returns atan(y / x), in radians.
    The double value is ![\\theta](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a372b7ef1ffaec3b4ad80e0141550990_l3.png) from polar coordinate (r, theta). 

**TypeError :**

  

  

    
    
    Returns a TypeError if anything other than float is passed. 

**Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate

# the atan2() method 

 

# imports math 

import math

 

# prints the theta value of

# two negative co-ordinates 

theta1 = math.atan2(-0.9, -0.9) 

print("atan2(-0.9, -0.9) : ", theta1) 

 

# prints the theta value of

# two positive co-ordinates 

theta2 = math.atan2(1.2, 1.5) 

print("atan2(1.2, 1.5) : ", theta2) 

 

# prints the theta value of one

# positive and one negative co-ordinates 

theta3 = math.atan2(1.2, -1.5) 

print("atan2(1.2, -1.5):", theta3)  
  
---  
  
 __

 __

 **Output :**

    
    
    atan2(-0.5, -0.5): -2.356194490192345
    atan2(1.2, 1.5): 0.6747409422235526
    atan2(1.2, -1.5): 2.4668517113662407
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the atan() method

 

# imports math 

import math

 

# list containing x and y coordinates 

y = [1, 2, 3, 4] 

x = [6, 3, 7, 8] 

 

# traversing in range to get theta 

# for all y and x co-ordinates 

for i in range(len(x)):

 theta = math.atan2(y[i], x[i]) 

 print(theta)   
  
---  
  
__

__

**Output :**

    
    
    0.16514867741462683
    0.5880026035475675
    0.40489178628508343
    0.4636476090008061
    

  
**Code #3 :** Program demonstrating the error

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the

# TypeError in atan() method 

 

# importing math 

import math

 

y, x = 3, 6

 

# when integer values are passed 

# it returns a TypeError

theta = math.atan2([y], [x]) 

print(theta)  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
      File "/home/622586ab389561bcdbfff258aca01e65.py", line 9, in 
        theta = math.atan2([y],[x]) 
    TypeError: a float is required
    

  
**Practical Application :**  
This function is used to find the slope in radians when Y and X co-ordinates
are given.

 **Code #4 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Let's find the slope when X

# and Y co-ordinates are given 

 

# imports math 

import math

 

# X and Y are co-ordinates

X = 2; Y = 2

 

# slope in radians 

theta1 = math.atan2(Y, X) 

 

# print the Slope in radians

print(theta1)  
  
---  
  
 __

 __

 **Output :**

    
    
    0.7853981633974483
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

