Secrets | Python module to Generate secure random numbers



The secrets module is used for generating random numbers for managing
important data such as passwords, account authentication, security tokens, and
related secrets, that are cryptographically strong. This module is responsible
for providing access to the most secure source of randomness. This module is
present in **Python 3.6** and above.

 **Random Numbers: class secrets.SystemRandom**

This class uses the os.urandom() function for the generation of random numbers
from sources provided by the operating system.

  1.  **secrets.choice(sequence):** This function returns a randomly-chosen element from a non-empty sequence to manage a basic level of security.  
 **Example 1 :** Generate a ten-character alphanumeric password.

 __

 __  
 __

 __

 __  
 __  
 __

import secrets

import string

 

alphabet = string.ascii_letters + string.digits

password = ''.join(secrets.choice(alphabet) for i in
range(10))

 

print(password)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    'tmX47l1uo4'
    

**Example 2 :** Generate a ten-character alphanumeric password with at least
one lowercase character, at least one uppercase character, and at least three
digits.

 __

 __  
 __

 __

 __  
 __  
 __

import secrets

import string

 

alphabet = string.ascii_letters + string.digits

while True:

 password = ''.join(secrets.choice(alphabet) for i in
range(10))

 if (any(c.islower() for c in password) and
any(c.isupper() 

 for c in password) and sum(c.isdigit() for c in
password) >= 3):

 print(password)

 break  
  
---  
  
 __

 __

 **Output :**

    
    
    Tx8LppU05Q
    

  2. **secrets.randbelow(n)** : This function returns a random integer in the range [0, n).

 __

 __  
 __

 __

 __  
 __  
 __

import secrets

 

passwd = secrets.randbelow(20)

print(passwd)  
  
---  
  
 __

 __

 **Output :**

    
    
    2
    

  3. **secrets.randbits(k):** This function returns an int with k random bits.

 __

 __  
 __

 __

 __  
 __  
 __

import secrets

 

passwd = secrets.randbits(7)

print(passwd)  
  
---  
  
 __

 __

 **Output :**

    
    
    61
    

**Generating tokens**

This module provides several functions for generating secure tokens for
applications such as password resets, hard-to-guess URLs etc.

  1.  **secrets.token_bytes([nbytes=None]) :** This function is responsible for generating a random byte string containing nbytes number of bytes. If no value is provided, a reasonable default is used.

 __

 __  
 __

 __

 __  
 __  
 __

import secrets

 

token1 = secrets.token_bytes()

token2 = secrets.token_bytes(10)

 

print(token1)

print(token2)  
  
---  
  
 __

 __

 **Output :**

    
    
    b"\x86?\x85\xcf\x8ek8ud\x8a\x92\x8b>R\xc7\x89_\xc4x\xce'u]\x95\x0c\x05*?HG8\xfb"
    b'Dx\xe8\x7f\xc05\xdf\xe0\xf6\xe1'
    

  2. **secrets.token_hex([nbytes=None]) :** This function is responsible for generating a random text string in hexadecimal containing nbytes random bytes. If no value is provided, a reasonable default is used.

 __

 __  
 __

 __

 __  
 __  
 __

import secrets

 

token1 = secrets.token_hex(16)

token2 = secrets.token_hex(9)

 

print(token1)

print(token2)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    5d894a501c88fbe735c6ff496a6d3e51
    78baed9057e597dce4
    

  3. **secrets.token_urlsafe([nbytes=None]) :** This function is responsible for generating a random URL-safe text string containing nbytes random bytes. This is suitable for password recovery applications.  
 **Example :** Generate a hard-to-guess temporary URL containing a security
token.

 __

 __  
 __

 __

 __  
 __  
 __

import secrets

 

url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()

print(url)  
  
---  
  
 __

 __

 **Output :**

    
    
    https://mydomain.com/reset=GbOiFIvhMoqWsfaTQKbj8ydbo8G1lsMx1ECa6SXjb1s
    

**How many bytes should tokens use?**  
At least 32 bytes for tokens should be used to be secure against a brute-force
attack.

 **Reference:**Official Python Documentation  
This article is contributed by **Aditi Gupta**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

