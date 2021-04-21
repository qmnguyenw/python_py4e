hashlib.sha3_256() in Python



With the help of **hashlib.sha3_256()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.sha3_256() method.

>  **Syntax :** hashlib.sha3_256()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.sha3_256() method, we are
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

 

# Using hashlib.sha3_256() method

gfg = hashlib.sha3_256()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

  

  

> b’\x14\xf7h\xf7\xb2w<\xe5\x8fQ\xe9s
> i\xd0\x89\x1c$\xfe\xac\xdb\xdfV\xe8c|\xb9\xdf\x96\xe3\x93z'

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

 

# Using hashlib.sha3_256() method

gfg = hashlib.sha3_256()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

>
> b”b\xea\x7f’\x8a\xd3\x93\xb1k\t5\xa5J|U\xea\xad\x03\xc8\x9eGw\xdeW\x03\xa6\xb8\x85}\xd5~\xb6″

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

