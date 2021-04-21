Python | Remove all characters except letters and numbers



Given a string, the task is to remove all the characters except numbers and
alphabets.

String manipulation is a very important task in a day to day coding and web
development. Most of the request and response in HTTP queries are in the form
of strings with sometimes some useless data which we need to remove. Let’s
discuss some Pythonic ways to remove all the characters except numbers and
alphabets.

 **Method #1: Usingre.sub**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove all the characters

# except numbers and alphabets

 

import re

 

# initialising string

ini_string = "123abcjw:, .@! eiw"

 

# printing initial string

print ("initial string : ", ini_string)

 

# function to demonstrate removal of characters

# which are not numbers and alphabets using re

 

result = re.sub('[\W_]+', '', ini_string)

 

# printing final string

print ("final string", result)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  123abcjw:, .@! eiw
    final string 123abcjweiw
    

  
**Method #2: Usingisalpha() and isnumeric()**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove all the characters

# except numbers and alphabets

 

import re

 

# initialising string

ini_string = "123abcjw:, .@! eiw"

 

# printing initial string

print ("initial string : ", ini_string)

 

# function to demonstrate removal of characters

# which are not numbers and alphabets using re

getVals = list([val for val in ini_string

 if val.isalpha() or val.isnumeric()])

 

result = "".join(getVals)

 

# printing final string

print ("final string", result)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  123abcjw:, .@! eiw
    final string 123abcjweiw
    

  
**Method #3: Usingalnum()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove all the characters

# except numbers and alphabets

 

# initialising string

ini_string = "123abcjw:, .@! eiw"

 

# printing initial string

print ("initial string : ", ini_string)

 

# function to demonstrate removal of characters

# which are not numbers and alphabets using re

getVals = list([val for val in ini_string if
val.isalnum()])

result = "".join(getVals)

 

# printing final string

print ("final string", result)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  123abcjw:, .@! eiw
    final string 123abcjweiw
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

