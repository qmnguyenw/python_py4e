hashlib.blake2b() in Python



With the help of **hashlib.blake2b()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.blake2b() method.

>  **Syntax :** hashlib.blake2b()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.blake2b() method, we are
able to encrypt the byte string or passwords to protect them by using this
method.

 __

 __  
 __

 __

 __  
 __  
 __

# import hashlib

import hashlib

 

# Using hashlib.blake2b() method

gfg = hashlib.blake2b()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

  

  

>
> b’G\x04\x97\xc5\xa2\x88:\x87{j\xda\x19\xa3\xd9[\x9f\xaa\x9d\tV\xc7~\x82\xee\x1d\xae\xed\xa8\xf7\x92bI&~x\xf7\xfc\x82\xb5\x80GV\x8aLE\xe1\x89\x19\xe4\x0c\xd1\xda\x97\x18\x00\xdbo\xda\xf7-\xb5\xe8\xff’

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import hashlib

import hashlib

 

# Using hashlib.blake2b() method

gfg = hashlib.blake2b()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

>
> b’\xd4\x8e\xd4\\\\\x8a&\xe1\xa7D!\x90\xce\x9d\x03v\x9a\x05\xf7\n\xf0H\xd37\x81O\r{\xed5~.\x8f\xde\x83\x8a\x05\xad\xa0\xc2&\xc2\x104\x8eu\x96\xb6\xde1-\xcc\xcaRq\xc5+\xaa\xcc\x88\x14p\xed\xf9T’

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

