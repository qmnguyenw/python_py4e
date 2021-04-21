hashlib.blake2s() in Python



With the help of **hashlib.blake2s()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.blake2s() method.

>  **Syntax :** hashlib.blake2s()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.blake2s() method, we are
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

 

# Using hashlib.blake2s() method

gfg = hashlib.blake2s()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

  

  

> b’\xb6\x88\x94, \x0fF*\x02\x163\x9e\x1f\\\0
> \xaa\x8c{\x17\xca\xfc\x14\xc3\xe5n\x89\x8e\xbbV\xf8\xa1\xdb’

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

 

# Using hashlib.blake2s() method

gfg = hashlib.blake2s()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

>
> b’\xad\x1bPqk\xbf\xdc\xbb\xea\xb0{j\xdb\x83B!\x14\xb3\xbfT\x03\xfa\xac\x93Zb\xb6\xd3\t\x7f\x14\t’

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

