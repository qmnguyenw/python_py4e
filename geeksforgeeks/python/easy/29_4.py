Quickly convert Decimal to other bases in Python



Given a number in decimal number convert it into binary, octal and hexadecimal
number. Here is function to convert decimal to binary, decimal to octal and
decimal to hexadecimal.

Examples:

    
    
    Input : 55
    Output : 55  in Binary :  0b110111
             55 in Octal :  0o67
             55  in Hexadecimal :  0x37
    
    Input : 282
    Output : 282  in Binary :  0b100011010
             282 in Octal :  0o432
             282  in Hexadecimal :  0x11a
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

One solution is to use the approach discussed in below post.

Convert from any base to decimal and vice versa

  

  

Python provides direct functions for standard base conversions like bin(),
hex() and oct()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert decimal to binary,

# octal and hexadecimal

 

# Function to convert decimal to binary

def decimal_to_binary(dec):

 decimal = int(dec)

 

 # Prints equivalent decimal

 print(decimal, " in Binary : ", bin(decimal))

 

# Function to convert decimal to octal

def decimal_to_octal(dec):

 decimal = int(dec)

 

 # Prints equivalent decimal

 print(decimal, "in Octal : ", oct(decimal))

 

# Function to convert decimal to hexadecimal

def decimal_to_hexadecimal(dec):

 decimal = int(dec)

 

 # Prints equivalent decimal

 print(decimal, " in Hexadecimal : ", hex(decimal))

 

# Driver program

dec = 32

decimal_to_binary(dec)

decimal_to_octal(dec)

decimal_to_hexadecimal(dec)  
  
---  
  
 __

 __

Output:

    
    
    32  in Binary :  0b100000
    32 in Octal :  0o40
    32  in Hexadecimal :  0x20
    

This article is contributed by **Pramod Kumar**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

