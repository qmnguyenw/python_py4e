Python Program to check Armstrong Number



Given a number x, determine whether the given number is Armstrong number or
not. A positive integer of **n digits** is called an Armstrong number of
**order n** (order is number of digits) if.

    
    
    **abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....**
    

**Example:**

    
    
    Input : 153
    Output : Yes
    153 is an Armstrong number.
    1*1*1 + 5*5*5 + 3*3*3 = 153
    
    Input : 120
    Output : No
    120 is not a Armstrong number.
    1*1*1 + 2*2*2 + 0*0*0 = 9
    
    Input : 1253
    Output : No
    1253 is not a Armstrong Number
    1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723
    
    Input : 1634
    Output : Yes
    1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
    

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to determine whether

# the number is Armstrong number or not

 

# Function to calculate x raised to 

# the power y

def power(x, y):

 

 if y == 0:

 return 1

 if y % 2 == 0:

 return power(x, y // 2) * power(x, y // 2)

 

 return x * power(x, y // 2) * power(x, y // 2)

 

# Function to calculate order of the number

def order(x):

 

 # Variable to store of the number

 n = 0

 while (x != 0):

 n = n + 1

 x = x // 10

 

 return n

 

# Function to check whether the given 

# number is Armstrong number or not

def isArmstrong(x):

 

 n = order(x)

 temp = x

 sum1 = 0

 

 while (temp != 0):

 r = temp % 10

 sum1 = sum1 + power(r, n)

 temp = temp // 10

 

 # If condition satisfies

 return (sum1 == x)

 

# Driver code

x = 153

print(isArmstrong(x))

 

x = 1253

print(isArmstrong(x))  
  
---  
  
 __

 __

Please refer complete article onProgram for Armstrong Numbers for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

