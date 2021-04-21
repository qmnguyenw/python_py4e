Python | Convert string dictionary to dictionary



Interconversions of data types have been discussed many times and have been
quite a popular problem to solve. This article discusses yet another problem
of interconversion of dictionary, in string format to a dictionary. Let’s
discuss certain ways in which this can be done.

 **Method #1 : Usingjson.loads()**

This task can easily be performed using the inbuilt function of loads of json
library of python which converts the string of valid dictionary into json
form, dictionary in Python.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# convert dictionary string to dictionary

# using json.loads()

import json

 

# initializing string 

test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using json.loads()

# convert dictionary string to dictionary

res = json.loads(test_string)

 

# print result

print("The converted dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
    The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}
    

  

  

**Method #2 : Usingast.literal_eval()**

The above method can also be used to perform a similar conversion. Function
safer than the eval function and can be used for interconversion of all data
types other than dictionary as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# convert dictionary string to dictionary

# using ast.literal_eval()

import ast

 

# initializing string 

test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using ast.literal_eval()

# convert dictionary string to dictionary

res = ast.literal_eval(test_string)

 

# print result

print("The converted dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
    The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

