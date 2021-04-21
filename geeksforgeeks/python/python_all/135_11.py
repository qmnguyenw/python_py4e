Python | Interconversion between Dictionary and Bytes



Interconversion between data is quite popular and this particular article
discusses about how interconversion of dictionary into bytes and vice versa
can be obtained. Let’s look at the method that can help us achieve this
particular task.

 **Method : Usingencode() + dumps() + decode() + loads()**  
The encode and dumps function together performs the task of converting the
dictionary to string and then to corresponding byte value. This can be
interconverted using the decode and loads function which returns the string
from bytes and converts that to the dictionary again.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Interconversion between Dictionary and Bytes

# Using encode() + dumps() + decode() + loads()

import json

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using encode() + dumps() to convert to bytes

res_bytes = json.dumps(test_dict).encode('utf-8')

 

# printing type and binary dict 

print("The type after conversion to bytes is : " +
str(type(res_bytes)))

print("The value after conversion to bytes is : " +
str(res_bytes))

 

# using decode() + loads() to convert to dictionary

res_dict = json.loads(res_bytes.decode('utf-8'))

 

# printing type and dict 

print("The type after conversion to dict is : " +
str(type(res_dict)))

print("The value after conversion to dict is : " + str(res_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': 1, 'best': 3, 'is': 2}
    The type after conversion to bytes is : <class 'bytes'>
    The value after conversion to bytes is : b'{"Gfg": 1, "best": 3, "is": 2}'
    The type after conversion to dict is : <class 'dict'>
    The value after conversion to dict is : {'Gfg': 1, 'best': 3, 'is': 2}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

