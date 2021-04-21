Python bit functions on int (bit_length, to_bytes and from_bytes)



The int type implements the **numbers.Integral abstract base class.**

1\. **int.bit_length()**  
Returns the number of bits required to represent an integer in binary,
excluding the sign and leading zeros.

Code to demonstrate

 __

 __  
 __

 __

 __  
 __  
 __

num= 7

print(num.bit_length())

 

num = -7

print(num.bit_length())  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    3
    

2\. **int.to_bytes(length, byteorder, *, signed=False)**  
Return an array of bytes representing an integer.If byteorder is “big”, the
most significant byte is at the beginning of the byte array. If byteorder is
“little”, the most significant byte is at the end of the byte array. The
signed argument determines whether two’s complement is used to represent the
integer.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Returns byte representation of 1024 in a

# big endian machine.

print((1024).to_bytes(2, byteorder ='big'))  
  
---  
  
 __

 __

 **Output:**

    
    
    b'\x04\x00'
    

3\. **int.from_bytes(bytes, byteorder, *, signed=False)**  
Returns the integer represented by the given array of bytes.

 __

 __  
 __

 __

 __  
 __  
 __

# Returns integer value of '\x00\x10' in big endian machine.

print(int.from_bytes(b'\x00\x10', byteorder ='big'))  
  
---  
  
 __

 __

 **Output:**

    
    
    16
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

