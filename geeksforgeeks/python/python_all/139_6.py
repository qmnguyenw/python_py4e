Python | Convert Bytearray to Hexadecimal String



Sometimes, we might be in a problem in which we need to handle the unusual
datatype conversions. One such conversion can be converting the list of
bytes(bytearray) to the Hexadecimal string format. Let’s discuss certain ways
in which this can be done.

 **Method #1 : Usingformat() + join()**  
The combination of above functions can be used to perform this particular
task. The format function converts the bytes in hexadecimal format. “02” in
format is used to pad required leading zeroes. The join function allows to
join the hexadecimal result into a string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting bytearray to hexadecimal string

# Using join() + format()

 

# initializing list 

test_list = [124, 67, 45, 11]

 

# printing original list 

print("The original string is : " + str(test_list))

 

# using join() + format()

# Converting bytearray to hexadecimal string

res = ''.join(format(x, '02x') for x in test_list)

 

# printing result 

print("The string after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : [124, 67, 45, 11]
    The string after conversion : 7c432d0b
    

**Method #2 : Usingbinascii.hexlify()**  
The inbuilt function of hexlify can be used to perform this particular task.
This function is recommended for this particular conversion as it is
tailormade to solve this specific problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting bytearray to hexadecimal string

# Using binascii.hexlify()

import binascii

 

# initializing list 

test_list = [124, 67, 45, 11]

 

# printing original list 

print("The original string is : " + str(test_list))

 

# using binascii.hexlify()

# Converting bytearray to hexadecimal string

res = binascii.hexlify(bytearray(test_list))

 

# printing result 

print("The string after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : [124, 67, 45, 11]
    The string after conversion : 7c432d0b
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

