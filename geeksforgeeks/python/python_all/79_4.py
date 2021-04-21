hashlib.shake_128() in Python



With the help of **hashlib.shake_128()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.shake_128() method.  
Note, We can adjust the length of encrypted data.

>  **Syntax :** hashlib.shake_128()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.shake_128() method, we are
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

 

# Using hashlib.shake_128() method

gfg = hashlib.shake_128()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest(10))  
  
---  
  
 __

 __

 **Output :**

  

  

> b’b\xfc0\xf2{\x814HG5′

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

 

# Using hashlib.shake_128() method

gfg = hashlib.shake_128()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest(15))  
  
---  
  
 __

 __

 **Output :**

> b’\x80\xa2g\x15>\xcf\xcf\x96\xd60p\x1c\xfc\x00\xfe’

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

