Python program to print number of bits to store an integer and also the number
in Binary format



Given an integer, the task is to write a Python program to print the number of
bits to store that integer and also print the same number in Binary format.

 **Example:**

>  **Input:** n = 10
>
>  **Output:**
>
> Number of bits to store the number: 4
>
>  
>
>
>  
>
>
> Binary value: 0b1010
>
>  **Input:** n = 120
>
>  **Output:**
>
> Number of bits to store the number: 7
>
> Binary value: 0b1111000

The Task can be done in 3 ways and all of them are given below:

###  **Method 1: Using loops**

In this, we will use the most basic method of converting the given number into
binary form by dividing it by 2 until the number becomes zero and storing the
remainder after each division. Continuing in this fashion, the size of the
array will give the number of bits to store an integer and the reverse of the
array with give the Binary format of the integer.

 **Approach**

  

  

  * Declare or take input
  * Keep dividing it by 2 and store remainder obtained
  * At the end of the process print its binary equivalent as well as the number of bits required to store it.

 **Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

list1= []

num = 10

 

while (num > 0):

 list1.append(num % 2)

 num = num//2

 

print("Number of bits required to store 10:", len(list1))

print("Binary Representatiaon:", end="")

for i in reversed(list1):

 print(list1[i], end="")  
  
---  
  
 __

 __

 **Output:**

> Number of bits required to store 10: 4
>
> Binary Representatiaon:1010

###  **Method 2:Using Recursion**

This code perform same task as given in method 1, but instead of using loops
we will use recursion.

 **Approach:**

  * Declare or take input
  * Keep dividing it by 2 and store remainder obtained using a recursive function
  * At the end of the process print its binary equivalent as well as the number of bits required to store it.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def decimalToBinary(n, x):

 

 if n > 1:

 # divide with integral result

 # (discard remainder)

 x = decimalToBinary(n//2, x)

 

 print(n % 2, end="")

 return x+1

 

 

# Driver code

if __name__ == '__main__':

 x = 0

 print("Binary Representation of 17:", end=" ")

 

 x = decimalToBinary(17, x)

 

 print()

 print("Number of bits required to store 17:", end=" ")

 print(x)  
  
---  
  
 __

 __

 **Output:**

> Binary Representation of 17: 10001
>
> Number of bits required to store 17: 5

###  **Method 3: Using in-built function**

Python comes with built-in sophisticated functions to perform the same tasks
in just few lines. To find the total number of bits to store an integer, we
use **bit_length()** function, it is called with the number (an integer value)
and returns the total number of bits to store the given number.

>  **Syntax:** int.bit_length(n)
>
>  **Parameter:** n, where it is an integer
>
> **Returns:** The number of bits required to represent an integer in binary,
> excluding the sign and leading zeros.

To print binary value of a given integer, we use **bin()** function it accepts
the number as an argument and returns the binary value.

>  **Syntax :** bin(a)
>
>  **Parameters :**
>
> a : an integer to convert
>
>  **Return Value :**  
>  A binary string of an integer or int object.
>
>  **Exceptions :**  
>  Raises TypeError when a float value is sent in arguments.

The output produced will have 0b in front of a number, it is just an indicator
that what follows it is a binary representation. You can remove it if you
want.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

num= 120

 

s = bin(120)

 

print("Number of bits required to store 120:", end=" ")

print(num.bit_length())

 

print("Binary Represenation", end=" ")

print(s)  
  
---  
  
 __

 __

 **Output:**

> Number of bits required to store 120: 7
>
> Binary Represenation 0b1111000

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

