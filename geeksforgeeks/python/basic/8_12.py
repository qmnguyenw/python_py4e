Python Program to create an OTP by squaring and concatenating the odd digits
of a number



Given a number n. The task is to create an OTP by squaring and concatenating
the odd digits of the number.

 **Examples:**

    
    
    **Input:** 4365188
    **Output:** 9256
    
    **Input:** 123456
    **Output:** 4163
    

**Explanation:** In the First example, the integers at odd places are 3, 5,
and 8. So we have to return a 4 digit OTP by squaring the digits. The square
of the above digits are 9, 25, 65 so the OTP to be returned is the first four
digits 9256.

 **Approach:** Iterate through the length of the string (number) with the
starting index as 1 and taking the step as 2. Initialize an empty string and
then concatenate the squares of the odd digit to that string. Finally, return
the first four characters of the string as an OTP.

Below is the implementation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# python program to generate

# an OTP from the squares of the

# odd digits

 

 

def OTP(number):

 

 # Finding the length 

 # of the string

 length = len(number)

 

 # Declaring an empty string 

 # for storing otp

 otp = ''

 

 # Iterating from index 1 

 # with step as 2

 for odd in range(1, length, 2):

 

 # Concatenating the output

 # to the string 

 otp+= str(int(number[odd])**2)

 

 print(otp[0:4])

 

# Driver code

number = '4365188'

OTP(number)  
  
---  
  
 __

 __

 **Output:**

    
    
    9256
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

