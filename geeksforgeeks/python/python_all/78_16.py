hashlib.sha3_224() in Python



With the help of **hashlib.sha3_224()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.sha3_224() method.

>  **Syntax :** hashlib.sha3_224()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.sha3_224() method, we are
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

 

# Using hashlib.sha3_224() method

gfg = hashlib.sha3_224()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

  

  

>
> b”\xa1\x155\xec\x93\xb1\xdcf)\x1c\xea\xf0\xf5\xe6\xdf\xc5I\x94’r{2\x04\xe8\xc9\xceY\xa8″

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

 

# Using hashlib.sha3_224() method

gfg = hashlib.sha3_224()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

> b’:\xddo\xd7\xb9Y\xc9%\xd1\x9f\x06u”g\x89*{\xbd\x18\x07\xcdIC\xbc<UQ\xed'

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

