hashlib.sha3_384() in Python



With the help of **hashlib.sha3_384()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.sha3_384() method.

>  **Syntax :** hashlib.sha3_384()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.sha3_384() method, we are
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

 

# Using hashlib.sha3_384() method

gfg = hashlib.sha3_384()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

  

  

>
> b’\x90\xb3\xee\xa6i\x8e\xc1\xc63\xc6\xe1_#\xbe\xe2F\xb2~\xe2[\xca\xb1I\xc9i\xef\xa5\xb32\xf9\xcc\xd8\x9c\x8c\x89\xd6\xc9\xb1\x9b!\x02\xb4\xaeN\xb9\x90Xo’

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

 

# Using hashlib.sha3_384() method

gfg = hashlib.sha3_384()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

>
> b’\xfc\xc4/q\xb0x\x0cp\xa7\xfa\xd34\x18{\xaa\xb6\xbb\x08\xb5\xe8\xa9\xc4\xd2\xc6\x9c\xcd-#\xc6\xedt\xbc\t\x0b\x11\xe4\x8bxQAx.C\nv\x1ev’

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

