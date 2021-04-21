codecs.encode() in Python



With the help of **codecs.encode()** method, we can encode the string into
the binary form .

>  **Syntax :** codecs.encode(string)
>
>  **Return :** Return the encoded string.

 **Example #1 :**  
In this example we can see that by using codecs.encode() method, we are able
to get the encoded string which can be in binary form by using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# import codecs

import codecs

 

s = 'GeeksForGeeks'

# Using codecs.encode() method

gfg = codecs.encode(s)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

  

  

> b’GeeksForGeeks’

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import codecs

import codecs

 

s = 'I love python.'

# Using codecs.encode() method

gfg = codecs.encode(s)

 

print(gfg)  
  
---  
  
 __

 __

 **Output :**

> b’I love python.’

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

