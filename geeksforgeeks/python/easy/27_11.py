Binary to decimal and vice-versa in python



Write Python code for converting a decimal number to it’s binary equivalent
and vice-versa.

 **Example:**

    
    
    From decimal to binary
    **Input :** 8
    **Output :** 1 0 0 0
    
    
    From binary to decimal
    **Input :** 100
    **Output :** 4
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Decimal to binary**

    
    
    Keep calling conversion function with n/2  till n > 1,
    later perform n % 1 to get MSB of converted binary number.  
    Example :- 7
    1). 7/2 = Quotient = 3(grater than 1), Remainder = 1.
    2). 3/2 = Quotient = 1(not grater than 1), Remainder = 1.
    3). 1%2 = Remainder = 1.
    Therefore, answer is 111.
    

__

__  
__

__

__  
__  
__

# Function to print binary number for the

# input decimal using recursion 

def decimalToBinary(n): 

 

 if(n > 1): 

 # divide with integral result 

 # (discard remainder) 

 decimalToBinary(n//2) 

 

 

 print(n%2, end=' ')

 

 

 

# Driver code 

if __name__ == '__main__': 

 decimalToBinary(8) 

 print("\n")

 decimalToBinary(18) 

 print("\n")

 decimalToBinary(7) 

 print("\n")  
  
---  
  
 __

 __

Output:

  

  

    
    
    1 0 0 0 
    1 0 0 1 0 
    1 1 1 
    

**Decimal to binary using bin():**

 __

 __  
 __

 __

 __  
 __  
 __

# Function to convert Decimal number

# to Binary number

 

def decimalToBinary(n):

 return bin(n).replace("0b","")

 

# Driver code

if __name__ == '__main__':

 print(decimalToBinary(8))

 print(decimalToBinary(18))

 print(decimalToBinary(7))  
  
---  
  
 __

 __

Output:

    
    
    1000
    10010
    111
    

**Binary to decimal**

    
    
    Example -: 1011
    1). Take modulo of given binary number with 10. 
        (1011 % 10 = 1)
    2). Multiply rem with 2 raised to the power
        it's position from right end. 
        (1 * 2^0)
        Note that we start counting position with 0. 
    3). Add result with previously generated result.
        decimal = decimal + (1 * 2^0)
    4). Update binary number by dividing it by 10.
        (1011 / 10 = 101)
    5). Keep repeating upper steps till binary > 0.
    
    Final Conversion -: (1 * 2^3) + (0 * 2^2) +
                     (1 * 2^1) + (1 * 2^0) = 11
    
    

__

__  
__

__

__  
__  
__

# Function calculates the decimal equivalent

# to given binary number

 

def binaryToDecimal(binary):

 

 binary1 = binary

 decimal, i, n = 0, 0, 0

 while(binary != 0):

 dec = binary % 10

 decimal = decimal + dec * pow(2, i)

 binary = binary//10

 i += 1

 print(decimal) 

 

 

# Driver code

if __name__ == '__main__':

 binaryToDecimal(100)

 binaryToDecimal(101)

 binaryToDecimal(1001)  
  
---  
  
 __

 __

Output:

    
    
    4
    5
    9
    

**Binary to decimal using int():**

 __

 __  
 __

 __

 __  
 __  
 __

# Function to convert Binary number

# to Decimal number

 

def binaryToDecimal(n):

 return int(n,2)

 

 

# Driver code

if __name__ == '__main__':

 print(binaryToDecimal('100'))

 print(binaryToDecimal('101'))

 print(binaryToDecimal('1001'))  
  
---  
  
 __

 __

Output:

    
    
    4
    5
    9
    

This article is contributed by **Pushpanjali Chauhan**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

