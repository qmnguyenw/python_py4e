MD5 hash in Python



Cryptographic hashes are used in day-day life like in digital signatures,
message authentication codes, manipulation detection, fingerprints, checksums
(message integrity check), hash tables, password storage and much more. They
are also used in sending messages over network for security or storing
messages in databases.  
  
There are many hash functions defined in the “ **hashlib** ” library in
python.  
This article deals with explanation and working of MD5 hash.

 **MD5 Hash**

This hash function accepts sequence of bytes and returns **128 bit hash
value** , usually used to check data integrity but has security issues.

 **Functions associated :**

  *  **encode() :** Converts the string into bytes to be acceptable by hash function.
  *  **digest() :** Returns the encoded data in byte format.
  *  **hexdigest() :** Returns the encoded data in hexadecimal format.

The below code demonstrates the working of MD5 hash accepting bytes and output
as bytes.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate the

# working of MD5 (byte - byte)

 

import hashlib

 

# encoding GeeksforGeeks using md5 hash

# function 

result = hashlib.md5(b'GeeksforGeeks')

 

# printing the equivalent byte value.

print("The byte equivalent of hash is : ", end ="")

print(result.digest())  
  
---  
  
 __

 __

Output:

  

  

    
    
    The byte equivalent of hash is : b'\xf1\xe0ix~\xcetS\x1d\x11%Y\x94\\hq'
    

**Explanation :** The above code takes byte and can be accepted by the hash
function. The md5 hash function encodes it and then using digest(), byte
equivalent encoded string is printed.  

Below code demonstrated how to take string as input and output hexadecimal
equivalent of the encoded value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate the

# working of MD5 (string - hexadecimal)

 

import hashlib

 

# initializing string

str2hash = "GeeksforGeeks"

 

# encoding GeeksforGeeks using encode()

# then sending to md5()

result = hashlib.md5(str2hash.encode())

 

# printing the equivalent hexadecimal value.

print("The hexadecimal equivalent of hash is : ", end ="")

print(result.hexdigest())  
  
---  
  
 __

 __

Output:

    
    
    The hexadecimal equivalent of hash is : f1e069787ece74531d112559945c6871
    

**Explanation :** The above code takes string and converts it into the byte
equivalent using encode() so that it can be accepted by the hash function. The
md5 hash function encodes it and then using hexdigest(), hexadecimal
equivalent encoded string is printed.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

