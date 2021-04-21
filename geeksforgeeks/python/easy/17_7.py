Python program to convert decimal to binary number



Given a decimal number as input, the task is to write a Python program to
convert the given decimal number into equivalent binary number.  
 **Examples :**

    
    
    Input : 7                                                         
    Output :111
    
    Input :10
    Output :1010

 **Method #1:** Recursive solution

    
    
    DecimalToBinary(num):
            if num >= 1:
                DecimalToBinary(num // 2)
                print num % 2 

![](https://media.geeksforgeeks.org/wp-
content/uploads/decimal2binaryPython.png)

Below is the implementation of above recursive solution:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function to convert decimal number

# to binary using recursion

def DecimalToBinary(num):

 

 if num >= 1:

 DecimalToBinary(num // 2)

 print(num % 2, end = '')

# Driver Code

if __name__ == '__main__':

 

 # decimal value

 dec_val = 24

 

 # Calling function

 DecimalToBinary(dec_val)  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    011000

