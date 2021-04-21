Python | Remove punctuation from string



Many times while working with Python strings, we have a problem in which we
need to remove certain characters from strings. This can have application in
data preprocessing in Data Science domain and also in day-day programming.
Lets discuss certain ways in which we can perform this task.

 **Method #1 : Using loop + punctuation string**  
This is brute way in which this task can be performed. In this, we check for
the punctuations using raw string which contain punctuations and then we
construct string removing those punctuations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing punctuations in string

# Using loop + punctuation string

 

# initializing string

test_str = "Gfg, is best : for ! Geeks ;"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing punctuations string 

punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

 

# Removing punctuations in string

# Using loop + punctuation string

for ele in test_str: 

 if ele in punc: 

 test_str = test_str.replace(ele, "") 

 

# printing result 

print("The string after punctuation filter : " + test_str)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg, is best : for ! Geeks ;
    The string after punctuation filter : Gfg is best  for  Geeks 
    

**Method #2 : Using regex**  
The part of replacing with punctuation can also be performed using regex. In
this, we replace all punctuation by empty string using certain regex.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing punctuations in string

# Using regex

import re

 

# initializing string

test_str = "Gfg, is best : for ! Geeks ;"

 

# printing original string

print("The original string is : " + test_str)

 

# Removing punctuations in string

# Using regex

res = re.sub(r'[^\w\s]', '', test_str)

 

# printing result 

print("The string after punctuation filter : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg, is best : for ! Geeks ;
    The string after punctuation filter : Gfg is best  for  Geeks 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

