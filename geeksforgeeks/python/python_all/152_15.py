Python | Extract only characters from given string



Given a string, the task is to extract only alphabetical characters from a
string. Given below are few methods to solve the given problem.

 **Method #1: Usingre.split**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to get characters from string

import re

 

# initialising string

ini_string = "123()#$ABGFDabcjw"

ini_string2 = "abceddfgh"

 

# printing strings

print ("initial string : ", ini_string, ini_string2)

 

# code to find characters in string

res1 = " ".join(re.split("[^a-zA-Z]*", ini_string))

res2 = " ".join(re.split("[^a-zA-Z]*", ini_string2))

 

# printing resultant string

print ("first string result: ", str(res1))

print ("second string result: ", str(res2))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  123()#$ABGFDabcjw abceddfgh
    first string result:   ABGFDabcjw
    second string result:  abceddfgh

  
**Method #2: Usingre.fidall**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to get characters in string

import re

 

# initialising string

ini_string = "123()#$ABGFDabcjw"

ini_string2 = "abceddfgh"

 

# printing strings

print ("initial string : \n", ini_string, "\n", ini_string2)

 

# code to find characters in string

res1 = " ".join(re.findall("[a-zA-Z]+", ini_string))

res2 = " ".join(re.findall("[a-zA-Z]+", ini_string2))

 

# printing resultant string

print ("first string result: ", str(res1))

print ("second string result: ", str(res2))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial string : 
     123()#$ABGFDabcjw 
     abceddfgh
    
    first string result:  ABGFDabcjw
    second string result:  abceddfgh

  
**Method #3: Usingisalpha()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to get characters in a string

# if present

 

# initialising string

ini_string = "123()#$ABGFDabcjw"

 

# printing string and its length

print ("initial string : ", ini_string)

 

# code to find characters in string

res1 = ""

for i in ini_string:

 if i.isalpha():

 res1 = "".join([res1, i])

 

 

# printing resultant string

print ("first result: ", str(res1))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  123()#$ABGFDabcjw
    first result:  ABGFDabcjw
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

