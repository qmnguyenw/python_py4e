Python | Check Numeric Suffix in String



Sometimes, while programming, we can have such a problem in which we need to
check if any string is ending with a number i.e it has a numeric suffix. This
problem can occur in Web Development domain. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Using regex**  
This problem can be solved using regex. The search and group function can
perform the task of searching the suffix string and printing the number, if it
is required.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check Numeric Suffix in String 

# Using regex

import re

 

# initializing string 

test_str = "Geeks4321"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using regex

# Check Numeric Suffix in String

res = re.search(r'\d+$', test_str)

 

# printing result 

print("Does string contain suffix number ? : " +
str(bool(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks4321
    Does string contain suffix number ? : True
    

**Method #2 :Using isdigit()**  
The isdigit function can be used to perform this particular task using the
fact that if a number at the end, means its very last character is going to be
a number, so by just checking the last character, we can prove that a string
ends with a number.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check Numeric Suffix in String 

# Using isdigit()

 

# initializing string 

test_str = "Geeks4321"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using isdigit()

# Check Numeric Suffix in String

res = test_str[-1].isdigit()

 

# printing result 

print("Does string contain suffix number ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks4321
    Does string contain suffix number ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

