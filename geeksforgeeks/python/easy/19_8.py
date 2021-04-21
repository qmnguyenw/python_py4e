Python Program to generate one-time password (OTP)



One-time Passwords (OTP) is a password that is valid for only one login
session or transaction in a computer or a digital device. Now a days OTP’s are
used in almost every service like Internet Banking, online transactions etc.
They are generally combination of 4 or 6 numeric digits or a 6-digit
alphanumeric.

random() function can be used to generate random OTP which is predefined in
random library. Let’s see how to generate OTP using Python.

>  **Used Function:**
>
>  **random.random():** This function returns any random number between 0 to
> 1.  
>  **math.floor():** It returns floor of any floating number to a integer
> value.
>
> Using the above function pick random index of string array which contains
> all the possible candidates of a particular digit of the OTP.
>
>  
>
>
>  
>

 **Example #1 :** Generate 4 digit Numeric OTP

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import math, random

 

# function to generate OTP

def generateOTP() :

 

 # Declare a digits variable 

 # which stores all digits 

 digits = "0123456789"

 OTP = ""

 

 # length of password can be chaged

 # by changing value in range

 for i in range(4) :

 OTP += digits[math.floor(random.random() * 10)]

 

 return OTP

 

# Driver code

if __name__ == "__main__" :

 

 print("OTP of 4 digits:", generateOTP())  
  
---  
  
 __

 __

 **Output:**

    
    
    OTP of 4 digits: 3211
    

**Example #2:** Generate alphanumeric OTP of length 6

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import math, random

 

# function to generate OTP

def generateOTP() :

 

 # Declare a string variable 

 # which stores all string 

 string =
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

 OTP = ""

 length = len(string)

 for i in range(6) :

 OTP += string[math.floor(random.random() * length)]

 

 return OTP

 

# Driver code

if __name__ == "__main__" :

 

 print("OTP of length 6:", generateOTP())  
  
---  
  
 __

 __

 **Output:**

    
    
    OTP of length 6: pyelJl
    

  
**Example #3:** Using String constants

 __

 __  
 __

 __

 __  
 __  
 __

# Importing random to generate

# random string sequence 

import random 

 

# Importing string library function 

import string 

 

def rand_pass(size): 

 

 # Takes random choices from 

 # ascii_letters and digits 

 generate_pass = ''.join([random.choice( string.ascii_uppercase +

 string.ascii_lowercase +

 string.digits) 

 for n in range(size)]) 

 

 return generate_pass 

 

# Driver Code 

password = rand_pass(10) 

print(password)   
  
---  
  
__

__

**Output:**

    
    
    2R8gaoDKqn

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

