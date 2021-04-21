Python | Ways to convert string to json object



Data send and get generally in a string of dictionary(JSON objects) forms in
many web API’s to use that data to extract meaningful information we need to
convert that data in dictionary form and use for further operations.

Let’s see some ways to convert string to json.  
  
 **Method #1:** dict object to string object using json.loads

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting string to json 

# using json.loads

import json

 

# inititialising json object

ini_string = {'nikhil': 1, 'akash' : 5, 

 'manjeet' : 10, 'akshat' : 15}

 

# printing initial json

ini_string = json.dumps(ini_string)

print ("initial 1st dictionary", ini_string)

print ("type of ini_object", type(ini_string))

 

# converting string to json

final_dictionary = json.loads(ini_string)

 

# printing final result

print ("final dictionary", str(final_dictionary))

print ("type of final_dictionary", type(final_dictionary))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial 1st dictionary {'manjeet': 10, 'nikhil': 1, 'akshat': 15, 'akash': 5}
    type of ini_object <type 'str'>
    final dictionary {'nikhil': 1, 'manjeet': 10, 'akshat': 15, 'akash': 5}
    type of final_dictionary <type 'dict'>
    

**Method #2:** str object to dict object using eval()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting string to json 

# using eval

 

 

# inititialising json object string

ini_string = """{'nikhil': 1, 'akash' : 5,

 'manjeet' : 10, 'akshat' : 15}"""

 

# printing initial json

print ("initial 1st dictionary", ini_string)

print ("type of ini_object", type(ini_string))

 

# converting string to json

final_dictionary = eval(ini_string)

 

# printing final result

print ("final dictionary", str(final_dictionary))

print ("type of final_dictionary", type(final_dictionary))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial 1st dictionary {'nikhil': 1, 'akash' : 5, 'manjeet' : 10, 'akshat' : 15}
    type of ini_object <class 'str'>
    final dictionary {'nikhil': 1, 'manjeet': 10, 'akash': 5, 'akshat': 15}
    type of final_dictionary <class 'dict'>
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

