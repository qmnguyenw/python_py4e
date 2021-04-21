getpass() and getuser() in Python (Password without echo)



getpass() prompts the user for a password without echoing. The getpass module
provides a secure way to handle the password prompts where programs interact
with the users via the terminal.

This module provides two functions :

  1.  **getpass()**
    
    
    getpass. **getpass** (prompt='Password: ', stream=None) 

The getpass() function is used to prompt to users using the string prompt and
reads the input from the user as Password. The input read deafults to
“Password: ” is returned to the caller as a string.

Let’s walk through some examples to understand its implementation.

 **Example 1 : No Prompt provided by the caller**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# A simple Python program to demonstrate

# getpass.getpass() to read password

import getpass

 

try:

 p = getpass.getpass()

except Exception as error:

 print('ERROR', error)

else:

 print('Password entered:', p)  
  
---  
  
 __

 __

Here, no prompt is provided by the caller. So, it is set to the default prompt
“Password”.  
 **Output :**

    
    
    $ python3 getpass_example1.py
    
    Password: 
    ('Password entered:', 'aditi')
    

**Example 2 : Security Question**  
There are certain programs that ask for security questions rather than asking
for passwords for better security. Here, the prompt can be changed to any
value.

 __

 __  
 __

 __

 __  
 __  
 __

# A simple Python program to demonstrate

# getpass.getpass() to read security question

import getpass

 

p = getpass.getpass(prompt='Your favorite flower? ')

 

if p.lower() == 'rose':

 print('Welcome..!!!')

else:

 print('The answer entered by you is incorrect..!!!')  
  
---  
  
 __

 __

 **Output :**

    
    
    $ python3 getpass_example2.py
    
    Your favorite flower?
    Welcome..!!!
    
    $ python3 getpass_example2.py
    
    Your favorite flower?
    The answer entered by you is incorrect..!!!
    

  2. **getuser()**  
getpass. **getuser** ()

The getuser() function displays the login name of the user. This function
checks the environment variables LOGNAME, USER, LNAME and USERNAME, in order,
and returns the value of the first non-empty string.

 **Example 3 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate working of

# getpass.getuser()

import getpass

 

user = getpass.getuser()

 

while True:

 pwd = getpass.getpass("User Name : %s" % user)

 

 if pwd == 'abcd':

 print "Welcome!!!"

 break

 else:

 print "The password you entered is incorrect."  
  
---  
  
 __

 __

 **Output :**

    
    
    $ python3 getpass_example3.py
    
    User Name : bot
    Welcome!!!
    
    $ python3 getpass_example3.py
    
    User Name : bot
    The password you entered is incorrect.
    
    

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

