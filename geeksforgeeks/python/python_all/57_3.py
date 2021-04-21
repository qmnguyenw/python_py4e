Python program to convert any base to decimal by using int() method



Given a number and its base, the task is to convert the given number into its
corresponding decimal number. The base of number can be anything like digits
between 0 to 9 and A to Z. Where the value of A is 10, value of B is 11, value
of C is 12 and so on.

**Examples:**

    
    
    **Input :** '1011' 
    **base** = 2 
    **Output :** 11 
    
    **Input :** '1A' 
    **base** = 16
    **Output :** 26
    
    **Input :** '12345' 
    **base =** 8
    **Output :** 5349
    

**Approach –**

  * Given number in string form and base 
  * Now call the builtin function int(‘number’, base) by passing the two parameters any base number in String form and base of that number and store the value in temp 
  * Print the value temp  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert any base

# number to its corresponding decimal

# number

 

# Function to convert any base number

# to its corresponding decimal number

def any_base_to_decimal(number, base):

 

 # calling the builtin function 

 # int(number, base) by passing 

 # two arguments in it number in

 # string form and base and store

 # the output value in temp

 temp = int(number, base)

 

 # printing the corresponding decimal

 # number

 print(temp)

 

# Driver's Code

if __name__ == '__main__' :

 hexadecimal_number = '1A'

 base = 16

 any_base_to_decimal(hexadecimal_number, base)  
  
---  
  
 __

 __

 **Output:**

    
    
    26

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

