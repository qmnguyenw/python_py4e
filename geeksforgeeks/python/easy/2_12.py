How to Convert Bytes to String in Python ?



Data types are the classification or categorization of data items. It
represents the kind of value that tells what operations can be performed on a
particular data. Since everything is an object in Python programming, data
types are actually classes and variables are instance (object) of these
classes.

We can convert bytes to string using the below methods:

 **Method #1:** Using _decode()_ method

This method is used to convert from one encoding scheme, in which the argument
string is encoded to the desired encoding scheme. This works opposite to the
encode.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program for converting bytes

# to string using decode()

 

data = b'GeeksForGeeks'

 

# display input

print('\nInput:')

print(data)

print(type(data))

 

# converting

output = data.decode()

 

# display output

print('\nOutput:')

print(output)

print(type(output))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Input:
    b'GeeksForGeeks'
    <class 'bytes'>
    
    Output:
    GeeksForGeeks
    <class 'str'>

 **Method #2:** Using _str()_ function

The _str()_ function of Python returns the string version of the object.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program for converting bytes to string using decode()

data = b'GeeksForGeeks'

 

# display input

print('\nInput:')

print(data)

print(type(data))

 

# converting

output = str(data, 'UTF-8')

 

# display output

print('\nOutput:')

print(output)

print(type(output))  
  
---  
  
 __

 __

 **Output:**

    
    
    Input:
    b'GeeksForGeeks'
    <class 'bytes'>
    
    Output:
    GeeksForGeeks
    <class 'str'>

 **Method #3:** Using _codecs.decode()_ method

This method is used to decode the binary string into normal form.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program for converting bytes to string using decode()

 

# import required module

import codecs

 

data = b'GeeksForGeeks'

 

# display input

print('\nInput:')

print(data)

print(type(data))

 

# converting

output = codecs.decode(data)

 

# display output

print('\nOutput:')

print(output)

print(type(output))  
  
---  
  
 __

 __

 **Output:**

    
    
    Input:
    b'GeeksForGeeks'
    <class 'bytes'>
    
    Output:
    GeeksForGeeks
    <class 'str'>

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

