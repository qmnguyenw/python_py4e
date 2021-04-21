hashlib.shake_256() in Python



With the help of **hashlib.shake_256()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.shake_256() method.  
Note, We can adjust the length of encrypted data.

>  **Syntax :** hashlib.shake_256()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.shake_256() method, we are
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

 

# Using hashlib.shake_256() method

gfg = hashlib.shake_256()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest(10))  
  
---  
  
 __

 __

 **Output :**

  

  

> b’e\xd6\xdf\x8d\x88\x19\x8d\xe6\x9b<'

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

 

# Using hashlib.shake_256() method

gfg = hashlib.shake_256()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest(15))  
  
---  
  
 __

 __

 **Output :**

> b’Mh\xf9X\xd0\xee=\x03\xa5a\xbc\xd0\xbf).’

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

