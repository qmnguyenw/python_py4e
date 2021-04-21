struct module in Python



This module performs conversions between Python values and C structs
represented as Python bytes objects. Format strings are the mechanism used to
specify the expected layout when packing and unpacking data. Module struct is
available in Python 3.x and not on 2.x, thus these codes will run on Python3
interpreter.

 **Struct Functions**

  *  **struct.pack()**
    
         **Syntax: 
    struct.pack(format, v1, v2, ...)**

Return a string containing the values v1, v2, … , that are packed according to
the given format (Format strings are the mechanism used to specify the
expected layout when packing and unpacking data).The values followed by the
format must be as per the format only, else struct.error is raised.

 __

 __  
 __

 __

 __  
 __  
 __

import struct

 

# Format: h is short in C type

# Format: l is long in C type

# Format 'hhl' stands for 'short short long'

var = struct.pack('hhl',1,2,3)

print(var)

 

# Format: i is int in C type

# Format 'iii' stands for 'int int int'

var = struct.pack('iii',1,2,3)

print(var)  
  
---  
  
 __

 __

Output:

    
    
    b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'
    b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
    

  * **struct.unpack()**
    
         **Syntax:
    struct.unpack(fmt, string)**

Return the values v1, v2, … , that are unpacked according to the given
format(1st argument). Values returned by this function are returned as tuples
of size that is equal to the number of values passed through struct.pack()
during packing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import struct

 

# '?' -> _BOOL , 'h' -> short, 'i' -> int and 'l' -> long

var = struct.pack('?hil', True, 2, 5, 445)

print(var)

 

# struct.unpack() return a tuples

# Variables V1, V2, V3,.. are returned as elements of tuple

tup = struct.unpack('?hil', var)

print(tup)

 

# q -> long long int and f -> float

var = struct.pack('qf', 5, 2.3)

print(var)

tup = struct.unpack('qf', var)

print(tup)  
  
---  
  
 __

 __

Output:

    
    
    b'\x01\x00\x02\x00\x05\x00\x00\x00\xbd\x01\x00\x00\x00\x00\x00\x00'
    (True, 2, 5, 445)
    b'\x05\x00\x00\x00\x00\x00\x00\x0033\x13@'
    (5, 2.299999952316284)
    

Note: ‘b’ in the Output stands for binary.

  *  **struct.calcsize()**
    
         **Syntax:
    struct.calcsize(fmt)**
    **fmt:** format 

Return the size of the struct (and hence of the string) corresponding to the
given format. calcsize() is important function, and is required for function
such as struct.pack_into() and struct.unpack_from(), which require offset
value and buffer as well.

 __

 __  
 __

 __

 __  
 __  
 __

import struct

var = struct.pack('?hil', True, 2, 5, 445)

print(var)

# Returns the size of the structure

print(struct.calcsize('?hil'))

print(struct.calcsize('qf'))  
  
---  
  
 __

 __

Output:

    
    
    b'\x01\x00\x02\x00\x05\x00\x00\x00\xbd\x01\x00\x00\x00\x00\x00\x00'
    16
    12
    

__

__  
__

__

__  
__  
__

import struct

var = struct.pack('bi', 56, 0x12131415)

print(var)

print(struct.calcsize('bi'))

var = struct.pack('ib', 0x12131415, 56)

print(var)

print(struct.calcsize('ib'))  
  
---  
  
 __

 __

Output:

    
    
    b'8\x00\x00\x00\x15\x14\x13\x12'
    8
    b'\x15\x14\x13\x128'
    5
    

Note: The ordering of format characters may have an impact on size.

  *  **Exception struct.error**  
Exception struct.error describes what is wrong at passing arguments, when a
wrong argument is passed struct.error is raised.

 __

 __  
 __

 __

 __  
 __  
 __

from struct import error

print(error)  
  
---  
  
 __

 __

Note: This is piece of code is not useful, anywhere other than exception
handling, and is used to show that ‘error’ upon interpreted shows about the
class.

  *  **struct.pack_into()**
    
         **Syntax:
    struct.pack_into(fmt, buffer, offset, v1, v2, ...) **fmt:** data type format
    **buffer:** writable buffer which starts at offset (optional)
    **v1,v2..** : values **

  * **struct.unpack_from()**
    
         **Syntax:
    struct.unpack_from(fmt, buffer[,offset = 0])** **fmt:** data type format
    **buffer:** writable buffer which starts at offset (optional)

Returns a tuple, similar to struct.unpack()

 __

 __  
 __

 __

 __  
 __  
 __

import struct

 

# ctypes in imported to create string buffer

import ctypes

 

# SIZE of the format is calculated using calcsize()

siz = struct.calcsize('hhl')

print(siz)

 

# Buffer 'buff' is created

buff = ctypes.create_string_buffer(siz)

 

# struct.pack() returns packed data

# struct.unpack() returns unpacked data

x = struct.pack('hhl', 2, 2, 3)

print(x)

print(struct.unpack('hhl', x))

 

# struct.pack_into() packs data into buff, doesn't return any value

# struct.unpack_from() unpacks data from buff, returns a tuple of values

struct.pack_into('hhl', buff, 0, 2, 2, 3)

print(struct.unpack_from('hhl', buff, 0))  
  
---  
  
 __

 __

Output:

    
    
    16
    b'\x02\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'
    (2, 2, 3)
    (2, 2, 3)
    

Reference https://docs.python.org/2/library/struct.html  
This article is contributed by **Piyush Doorwar**. If you like GeeksforGeeks
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

