Python | Finding Solutions of a Polynomial Equation



Given a quadratic equation, the task is to find the possible solutions to it.

 **Examples:**

    
    
    **Input :** 
    enter the coef of x2 : 1
    enter the coef of x  : 2
    enter the costant    : 1
    **Output :**
    the value for x is -1.0
    
    **Input :**
    enter the coef of x2 : 2
    enter the coef of x  : 3
    enter the costant    : 2
    **Output :**
    x1 = -3+5.656854249492381i/4 and x2 = -3-5.656854249492381i/4
    

**Algorithm :**

    
    
    Start.
    Prompt the values for a, b, c. 
    Compute i = b**2-4*a*c
    If i get negative value g=square root(-i)
    Else h = sqrt(i)
    Compute e = -b+h/(2*a)
    Compute f = -b-h/(2*a)
    If condition e==f then
        Print e
    Else
        Print e and f
    If i is negative then
        Print -b+g/(2*a) and -b-g/(2*a)
    stop
    

**Below is the Python implementation of the above mentioned task.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for solving a quadratic equation.

 

from math import sqrt 

try: 

 

 # if user gives non int values it will go to except block

 a = 1

 b = 2

 c = 1

 i = b**2-4 * a * c

 

 # magic condition for complex values

 g = sqrt(-i)

 try:

 d = sqrt(i)

 # two resultants

 e = (-b + d) / 2 * a 

 f = (-b-d) / 2 * a

 if e == f:

 print("the values for x is " + str(e))

 else:

 print("the value for x1 is " + str(e) +

 " and x2 is " + str(f))

 except ValueError:

 print("the result for your equation is in complex")

 

 # to print complex resultants.

 print("x1 = " + str(-b) + "+" + str(g) + "i/"
+ str(2 * a) +

 " and x2 = " + str(-b) + "-" + str(g) + "i/" +

 str(2 * a)) 

 

except ValueError:

 print("enter a number not a string or char")  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    the values for x is -1.0

 **Explanation :**  
First, this program will get three inputs from the user. The values are the
coefficient of ![x2](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-cbe895edb65ce0223c1e99b3e4a5dc77_l3.png), coefficient of
![x](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4fdd037713ae07c442e4e7d7e059e818_l3.png) and constant.
Then it performs the formula  
![\(-b + \(or\) - sqrt\(b2 - 4 * a * c\) /
2a\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8de9bc857a5b9885836425916e1113d6_l3.png)  
For complex the value of ![\(b2 - 4 * a *
c\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8c31af8e3a0987ee4212ea8b0f3924f4_l3.png) gets negative.
Rooting negative values will throw a value error. In this case, turn the
result of ![-\(b2 - 4 * a * c\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-18dbad885a99b90ee54f135957767abf_l3.png) and then root
it. Don’t forget to include ![i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-aeba42a2346918ec8531199b1d5c206d_l3.png) at last.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

