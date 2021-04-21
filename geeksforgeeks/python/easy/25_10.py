Reverse bits of a positive integer number in Python



Given an positive integer and size of bits, reverse all bits of it and return
the number with reversed bits.

Examples:

    
    
    Input : n = 1, bitSize=32
    Output : 2147483648  
    On a machine with size of 
    bit as 32. Reverse of 0....001 is
    100....0.
    
    Input : n = 2147483648, bitSize=32
    Output : 1  
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We can solve this problem quickly in Python. Approach is very simple,

  1. Convert integer number into it’s binary representation using bin(num) function.
  2.  **bin()** function appends **0b** as a prefix in binary representation of number, skip first two characters of binary representation and reverse remaining part of string.
  3. As we know in memory any binary representation of a number is filled with leading zeros after last set bit from left that means we need to append **bitSize – len(reversedBits)** number of zeros after reversing remaining string.
  4. Now convert binary representation into integer number using **int(string,base)** method.

### How int() method wroks ?

 **int(string,base)** method takes a string and base to identify that string
is referring to what number system ( binary=2, heaxadecimal=16, octal=8 etc. )
and converts string into decimal number system accordingly. For example ;
int(‘1010’,2) = 10.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to reverse bits of positive

# integer number 

 

def reverseBits(num,bitSize): 

 

 # convert number into binary representation 

 # output will be like bin(10) = '0b10101' 

 binary = bin(num) 

 

 # skip first two characters of binary 

 # representation string and reverse 

 # remaining string and then append zeros 

 # after it. binary[-1:1:-1] --> start 

 # from last character and reverse it until 

 # second last character from left 

 reverse = binary[-1:1:-1] 

 reverse = reverse + (bitSize - len(reverse))*'0'

 

 # converts reversed binary string into integer 

 print (int(reverse,2)) 

 

# Driver program 

if __name__ == "__main__": 

 num = 1

 bitSize = 32

 reverseBits(num,bitSize)  
  
---  
  
 __

 __

Output:

    
    
    2147483648
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

