Python Program for Check if all digits of a number divide it



Given a number n, find whether all digits of n divide it or not.  

**Examples:**

    
    
    **Input :** 128
    **Output :** Yes
    128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
    
    **Input :** 130
    **Output :** No
    
    
    
    

We want to test whether each digit is non-zero and divides the number. For
example, with 128, we want to test d != 0 && 128 % d == 0 for d = 1, 2, 8. To
do that, we need to iterate over each digit of the number.  

## python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to

# check the number is

# divisible by all

# digits are not.

# Function to check

# the divisibility

# of the number by

# its digit.

def checkDivisibility(n, digit) :

 

 # If the digit divides the

 # number then return true

 # else return false.

 return (digit != 0 and n % digit == 0)

 

# Function to check if

# all digits of n divide

# it or not

def allDigitsDivide( n) :

 

 temp = n

 while (temp > 0) :

 

 # Taking the digit of

 # the number into digit

 # var.

 digit = temp % 10

 if ((checkDivisibility(n, digit)) == False) :

 return False

 temp = temp // 10

 

 return True

# Driver function

n = 128

if (allDigitsDivide(n)) :

 print("Yes")

else :

 print("No" )

 

# This code is contributed by Nikita Tiwari.  
  
---  
  
 __

 __

 **Output:**  

    
    
    Yes
    
    
    
    

Please refer complete article on Check if all digits of a number divide it for
more details!  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

