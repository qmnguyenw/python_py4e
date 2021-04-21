Python program to convert float decimal to Octal number



Python doesn’t support any inbuilt function to easily convert floating point
decimal numbers to octal representation. Let’s do this manually.  
  
**Approach :** To convert a decimal number having fractional part into octal,
first convert the integer part into octal form and then fractional part into
octal form and finally combine the two results to get the final answer.  
For Integer Part, Keep dividing the number by 8 and noting down the remainder
until and unless the dividend is less than 8 and copy all the remainders
together.  
For the Decimal Part, Keep multiplying the decimal part with 8 until and
unless we get 0 left as fractional part. After multiplying the first time,
note down an integral part and then again multiply the decimal part of new
value by 8 and keep doing this until perfect number is reached.

>  **Above steps can be written as :**  
> 7(base 10) = 7(base 8) and .16(base 10) = .1217(base 8)
>
> Now, to get the octal of the decimal number 7.16, merge the two octal
> results.  
> (7)10 = (7)8
>
> (0.16)10 = (0.1217...)8  
> So, (7.16)10 = (7.1217...)8  
> or, (7.16)10 = (7.1217)8 (approx. value)
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

# Python3 program to demonstrate

# octal type conversion

 

# Function returns the octal representation

# of the value passed as parameters. 'number'

# is floating point decimal number and 'places'

# is the number of decimal places

def float_octal(number, places = 3):

 

 # split() separates whole number and decimal 

 # part and stores it in two separate variables

 whole, dec = str(number).split(".")

 

 # Convert both whole number and decimal 

 # part from string type to integer type

 whole = int(whole)

 dec = int (dec)

 

 # Convert the whole number part to it's

 # respective octal form and remove the

 # "0o" from it.

 res = oct(whole).lstrip("0o") + "."

 

 # Iterate the number of times we want

 # the number of decimal places to be

 for x in range(places):

 

 # Multiply the decimal value by 8 and separate 

 # the whole number part and decimal part

 whole, dec = str((decimal_converter(dec)) * 8).split(".")

 

 # Convert the decimal part

 # to integer again

 dec = int(dec)

 

 # keep adding the integer parts 

 # received to the result variable

 res += whole

 

 return res

 

# Function converts the value passed as

# parameter to it's respective decimal

# representation

def decimal_converter(num):

 while num > 1:

 num /= 10

 return num

 

# Driver Code

 

# Take the user input for 

# the floating point number

n = input("Enter your floating point value : \n")

 

# Take user input for the number of decimal 

# places user would like the result as

p = int(input("Enter the number of decimal places of the result :
\n"))

 

print(float_octal(n, places = p))  
  
---  
  
 __

 __

 **Output :**

    
    
    Enter your floating point value :
    7.16
    
    Enter the number of decimal places of the result :
    10
    
    **7.1217273146**
    
    
    
    Enter your floating point value :
    7.1234
    
    Enter the number of decimal places of the result : 
    5
    
    **7.07713**
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

