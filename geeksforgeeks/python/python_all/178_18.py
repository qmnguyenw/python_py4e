Python program to convert floating to binary



Python doesn’t provide any inbuilt method to easily convert floating point
decimal numbers to binary number. So, Let’s do this manually.

 **Approach :**  
To convert a floating point decimal number into binary, first convert the
integer part into binary form and then fractional part into binary form and
finally combine both results to get the final answer.  
For Integer Part, keep dividing the number by 2 and noting down the remainder
until and unless the dividend is less than 2. If so, stop and copy all the
remainders together.  
For Decimal Part, keep multiplying the decimal part with 2 until and unless 0
left as fractional part. After multiplying the first time, note down integral
part and again multiply decimal part of the new value by 2. Keep doing this
until reached a perfect number.  

> **Above steps can be written as :**  
>  1(base 10) = 1(base 2) and .234(base 10) = .0011(base 2)
>
> Now, to get the binary of 1.234, merge both results as a complete number.
>
> (1)10 = (1)2  
> (.234)10 = (.0011)2  
> (1.234)10 = (1.0011...)2  
> (1.234)10 = (1.0011)2 [approx.]
>
>  
>
>
>  
>

Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert float

# decimal to binary number

 

# Function returns octal representation

def float_bin(number, places = 3):

 

 # split() seperates whole number and decimal 

 # part and stores it in two seperate variables

 whole, dec = str(number).split(".")

 

 # Convert both whole number and decimal 

 # part from string type to integer type

 whole = int(whole)

 dec = int (dec)

 

 # Convert the whole number part to it's

 # respective binary form and remove the

 # "0b" from it.

 res = bin(whole).lstrip("0b") + "."

 

 # Iterate the number of times, we want

 # the number of decimal places to be

 for x in range(places):

 

 # Multiply the decimal value by 2 

 # and seperate the whole number part

 # and decimal part

 whole, dec = str((decimal_converter(dec)) * 2).split(".")

 

 # Convert the decimal part

 # to integer again

 dec = int(dec)

 

 # Keep adding the integer parts 

 # receive to the result variable

 res += whole

 

 return res

 

# Function converts the value passed as

# parameter to it's decimal representation

def decimal_converter(num): 

 while num > 1:

 num /= 10

 return num

 

# Driver Code

 

# Take the user input for 

# the floating point number

n = input("Enter your floating point value : \n")

 

# Take user input for the number of

# decimal places user want result as

p = int(input("Enter the number of decimal places of the result :
\n"))

 

print(float_bin(n, places = p))  
  
---  
  
 __

 __

 **Output :**

    
    
    Enter your floating point value : 
    1.234
    Enter the number of decimal places of the result :
    4
    
    **1.0011**
    
    
    
    Enter your floating point value : 
    11.234
    Enter the number of decimal places of the result : 
    4
    
    **1011.0011**
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

