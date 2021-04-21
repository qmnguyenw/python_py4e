Python program to print an array of bytes representing an integer



Given an integer **N** , the task is to write a Python program to represent
the bytes of this number as an array.

A byte is a group of 8 bits. Any integer can be represented in the form of
bytes and bits. We generally use hexadecimal codes to represent a byte. A
single hexadecimal character can represent 4 bits so a pair of hexadecimal
characters are used to represent a byte.

**Example:**

>  **Input:** N = 543
>
>  **Output:** [‘0x2’, ‘0x1f’]
>
>  
>
>
>  
>
>
>  **Explanation:** 543 can be represented as 1000011111 in binary which can
> be grouped as (10)(00011111), each group representing a byte. In hexadecimal
> form, this number will be (0x02)(0x1F).
>
>  **Input:** N = 17292567
>
>  **Output:** [‘0x1’, ‘0x7’, ‘0xdd’, ‘0x17’]
>
>  **Explanation:** 17292567 can be represented as 1000001111101110100010111
> in binary which can be grouped as (1)(00000111)(11011101)(00010111), each
> group representing a byte. In hexadecimal form, this number will be (0x1),
> (0x7), (0xdd), (0x17).

 **Method 1 (Manual conversion):**

Just like we convert decimal numbers to binary numbers, we can convert it into
a base-256 number which will give us 8-bit numbers that represent bytes for
the given number.

Below is the code to implement the above-discussed method:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

n= 17292567

 

# Initialize the empty array

array = []

 

# Get the hexadecimal form

while(n):

 r = n % 256

 n = n//256

 array.append(hex(r))

 

# Reverse the array to get the MSB to left

array.reverse()

print(array)  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    ['0x1', '0x7', '0xdd', '0x17']

