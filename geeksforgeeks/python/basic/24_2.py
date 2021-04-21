Program to check if a number is Positive, Negative, Odd, Even, Zero



 **Prerequisite :** Loops in Python

To check whether a number is positive, negative, odd, even or zero. This
problem is solved using if…elif…else and nested if…else statement.  
 **Approach :**

  * A number is positive if it is greater than zero. We check this in the expression of if.
  * If it is False, the number will either be zero or negative.
  * This is also tested in subsequent expression.
  * In case of odd and even A number is even if it is perfectly divisible by 2.
  *     * When the number is divided by 2, we use the remainder operator % to compute the remainder.
    * If the remainder is not zero, the number is odd.

Examples:

    
    
    Input : 10
    Output :
    Positive number
    10 is Even
    
    
    
    Input : 0
    Output : 0 is Even
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Code to check if a number is

# Positive, Negative, Odd, Even, Zero 

# Using if...elif...else

num = 10

if num > 0:

 print("Positive number")

elif num == 0:

 print("Zero")

else:

 print("Negative number")

 

# Checking for odd and even

if (num % 2) == 0:

 print("{0} is Even".format(num))

else:

 print("{0} is Odd".format(num))  
  
---  
  
 __

 __

    
    
    Output:
    Positive number
    10 is Even

 __

 __  
 __

 __

 __  
 __  
 __

# Python Code to check if a number is

# Positive, Negative, Odd, Even, Zero

# Using Nested if

num = 20

if num >= 0:

 if num == 0:

 print("Zero")

 else:

 print("Positive number")

else:

 print("Negative number")

 

# Cchecking for odd and even

if (num % 2) == 0:

 print("{0} is Even".format(num))

else:

 print("{0} is Odd".format(num))  
  
---  
  
 __

 __

    
    
    Output:
    Positive number
    20 is Even

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

