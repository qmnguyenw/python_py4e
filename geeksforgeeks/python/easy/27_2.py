bin() in Python



Converting an decimal to binary is always an important utility that is
required in python dev projects and competitive programming as well. Having a
shorthand function to achieve this can always be handy in the situations which
require the swift conversion of it without writing a long code for same, this
is provided by “ **bin()** “. This has been discussed in this article.

 **Naive Methods to convert decimal to binary**

 **1\. Using recursion**  

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

 

 if n > 1:

 # divide with integral result 

 # (discard remainder) 

 decimalToBinary(n//2) 

 

 

 print (n%2,end="") 

 

# Driver code

if __name__ == '__main__':

 decimalToBinary(8)

 print("\r")

 decimalToBinary(18)

 print("\r")

 decimalToBinary(7)

 print  
  
---  
  
 __

 __

Output :

    
    
    1000
    10010
    111
    

**2\. Using loop**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate naive method

# using loop 

 

# function returning binary string

def Binary(n):

 binary = ""

 i = 0

 while n > 0 and i<=8:

 s1 = str(int(n%2))

 binary = binary + s1

 n /= 2

 i = i+1

 d = binary[::-1]

 return d

 

print("The binary representation of 100 (using loops) is :
",end="")

print(Binary(100))  
  
---  
  
 __

 __

Output:

  

  

    
    
    The binary representation of 100 (using loops) is : 001100100
    

**Using bin()**

Using bin() reduces the time required to code and also removes the hassle that
you may see in the above two mentioned methods.

    
    
    **Syntax :**
    bin(a)
    **Parameters :**
    **a :** an integer to convert
    **Return Value :**
    A binary string of an integer or int object.
    **Exceptions :**
    Raises TypeError when a float value is sent in arguments.
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate working of

# bin()

 

# function returning binary string

def Binary(n):

 s = bin(n)

 

 # removing "0b" prefix

 s1 = s[2:]

 return s1

 

print("The binary representation of 100 (using bin()) is :
",end="")

print(Binary(100))  
  
---  
  
 __

 __

Output :

    
    
    The binary representation of 100 (using bin()) is : 1100100
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
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

