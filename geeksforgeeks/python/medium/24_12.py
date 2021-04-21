Python program to check the validity of a Password



In this program, we will be taking a password as a combination of alphanumeric
characters along with special characters, and check whether the password is
valid or not with the help of few conditions.

 **Primary conditions for password validation :**

  1. Minimum 8 characters.
  2. The alphabets must be between [a-z]
  3. At least one alphabet should be of Upper Case [A-Z]
  4. At least 1 number or digit between [0-9].
  5. At least 1 character from [ _ or @ or $ ].

Examples:

    
    
    Input : R@m@_f0rtu9e$
    Output : Valid Password
    
    Input : Rama_fortune$
    Output : Invalid Password
    Explanation: Number is missing
    
    Input : Rama#fortu9e 
    Output : Invalid Password
    Explanation: Must consist from _ or @ or $
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Here we have used the **re** module that provide support for regular
expressions in Python. Along with this the re.search() method returns False
(if the first parameter is not found in the second parameter) This method is
best suited for testing a regular expression more than extracting data. We
have used the re.search() to check the validation of alphabets, digits or
special characters. To check for white spaces we use the “\s” which comes in
the module of the regular expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check validation of password

# Module of regular expression is used with search()

import re

password = "R@m@_f0rtu9e$"

flag = 0

while True: 

 if (len(password)<8):

 flag = -1

 break

 elif not re.search("[a-z]", password):

 flag = -1

 break

 elif not re.search("[A-Z]", password):

 flag = -1

 break

 elif not re.search("[0-9]", password):

 flag = -1

 break

 elif not re.search("[_@$]", password):

 flag = -1

 break

 elif re.search("\s", password):

 flag = -1

 break

 else:

 flag = 0

 print("Valid Password")

 break

 

if flag ==-1:

 print("Not a Valid Password")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Valid Password
    

