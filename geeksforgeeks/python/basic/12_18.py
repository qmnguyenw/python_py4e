Python | Generate random string of given length



The issue of generation of random numbers is quite common, but sometimes, we
have applications that require us to better that and provide some
functionality of generating a random string of digits and alphabets for
applications such as passwords. Let’s discuss certain ways in which this can
be performed.

 **Method #1 : Usingrandom.choices()**

This function of random module can help us achieve this task, and provides a
one liner alternative to a whole loop that might be required for this
particular task. Works with Python > v3.6 .

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# generating random strings 

# using random.choices()

import string

import random

 

# initializing size of string 

N = 7

 

# using random.choices()

# generating random strings 

res = ''.join(random.choices(string.ascii_uppercase +

 string.digits, k = N))

 

# print result

print("The generated random string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The generated random string : 0D5YE91
    

  

  

**Method #2 : Usingsecrets.choice()**

For Cryptographically more secure random numbers, this function of secret
module can be used as it’s internal algorithm is framed in a way to generate
less predictable random numbers. Works with Python > v3.6 .

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# generating random strings 

# using secrets.choice()

import secrets

import string

 

# initializing size of string 

N = 7

 

# using random.choices()

# generating random strings 

res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)

 for i in range(N))

 

# print result

print("The generated random string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The generated random string : T7HPKVR
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

