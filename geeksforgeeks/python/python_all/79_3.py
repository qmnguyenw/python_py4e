hashlib.sha3_512() in Python



With the help of **hashlib.sha3_512()** method, we can convert the normal
string in byte format is converted to an encrypted form. Passwords and
important files can be converted into hash to protect them with the help of
hashlib.sha3_512() method.

>  **Syntax :** hashlib.sha3_512()
>
>  **Return :** Return the hash code for the string.

 **Example #1 :**  
In this example we can see that by using hashlib.sha3_512() method, we are
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

 

# Using hashlib.sha3_512() method

gfg = hashlib.sha3_512()

gfg.update(b'GeeksForGeeks')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

  

  

>
> b’N\x1a\xf5\x8e\xbc\x95\xbb\xe1\x9fR\x13\xdfO\x06\xbce\x8a\x81q\x18R\xa7\x92j\x17u\x03\xee\xdf\x89\xf4\xdd$\xaf\xca\xb7\x9f\xb5\xe2\xd9\xab\xa1
> W\x03O\xdev%\xf7\x8d\xe0\xf2l\xf39\x84\xfcX9\xcf+\x1c0′

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

 

# Using hashlib.sha3_512() method

gfg = hashlib.sha3_512()

gfg.update(b'xyz@1234_GFG')

 

print(gfg.digest())  
  
---  
  
 __

 __

 **Output :**

>
> b’Q\xf8Q\x00\xb6r\xcf\xf3\xf7\xfeb\xf6\x81S\x92l\xfd\x93L\x0eI\xb0v\x08g\\\\\x8cc-\x12\ri\x05\xe6y<\xee\x8f4\x9bn\xa1-QI\xfcE\xa8=&\xdbGJ\xe7\xfa\x82\xdf\x9a%\xd0\x14\xb2\xef'

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

