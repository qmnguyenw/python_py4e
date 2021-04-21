Python program to concatenate two Integer values into one



Given two integers a and b. The task is to concatenate these two integers into
one integer.

 **Examples:**

    
    
    **Input :** a = 806, b = 91
    **Output :** 80691
    
    **Input :** a = 5, b = 1091
    **Output :** 51091
    
    

**Method 1:** One method of achieving this can be counting the number of
digits of second number. Then multiply the first number with 10^digits and
adding both the numbers. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to concatenate

# two numbers

 

 

def numConcat(num1, num2):

 

 # find number of digits in num2

 digits = len(str(num2))

 

 # add zeroes to the end of num1

 num1 = num1 * (10**digits)

 

 # add num2 to num1

 num1 += num2

 

 return num1

 

 

# Driver's code

a = 906

b = 91

print(numConcat(a, b))  
  
---  
  
 __

 __

 **Output:**

    
    
    90691
    

**Method 2:** Another method can be converting both the numbers to the string.
Then concatenate them and convert them back to integers. Below is the
implementation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to concatenate

# two numbers

 

 

def numConcat(num1, num2):

 

 # Convert both the numbers to

 # strings

 num1 = str(num1)

 num2 = str(num2)

 

 # Concatenate the strings

 num1 += num2

 

 return int(num1)

 

 

# Driver's code

a = 906

b = 91

print(numConcat(a, b))  
  
---  
  
 __

 __

 **Output:**

    
    
    90691
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

