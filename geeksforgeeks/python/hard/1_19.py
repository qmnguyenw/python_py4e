How to use Pickle to save and load Variables in Python?



Serialization is a technique used to save the state of an object from any
process. We can later use this state by deserialization, to continue the
process. Pickle is a python module that makes it easy to serialize or save
variables and load them when needed. Unlike JSON serialization, Pickle
converts the object into a binary string. JSON is text specific, but Pickle is
python specific, and it can serialize the custom classes which JSON fails to
serialize. Due to this feature, it is heavily used in training machine
learning models. This article discusses how variables can be saved and loaded
in python using pickle.

### Functions used:

  * In python, dumps() method is used to save variables to a pickle file.

 **Syntax:**

> pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)

  * In python, loads() is used to load saved data from a pickled file

 **Syntax:**

> pickle.loads(data, /, *, fix_imports=True, encoding=”ASCII”,
> errors=”strict”, buffers=None)
>
>  
>
>
>  
>

### Saving a variable:

  *  **Method 1:** Passing the variable

In dumps() method, we can pass the variable, and it will return us the binary
string for the same. We can then transmit it to other python modules or save
in a database.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pickle

 

# Create a variable

myvar = [{'This': 'is', 'Example': 1}, 'of',

 'serialisation', ['using', 'pickle']]

 

# Use dumps() to make it serialized

serialized = pickle.dumps(myvar)

 

print(serialized)  
  
---  
  
 __

 __

 **Output:**

>
> b’\x80\x04\x95K\x00\x00\x00\x00\x00\x00\x00]\x94(}\x94(\x8c\x04This\x94\x8c\x02is\x94\x8c\x07Example\x94K\x01u\x8c\x02of\x94\x8c\rserialisation\x94]\x94(\x8c\x05using\x94\x8c\x06pickle\x94ee.’

  *  **Method 2:** We can directly save the variable in a file itself.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pickle

 

# Create a variable

myvar = [{'This': 'is', 'Example': 2}, 'of',

 'serialisation', ['using', 'pickle']]

 

# Open a file and use dump()

with open('file.pkl', 'wb') as file:

 

 # A new file will be created

 pickle.dump(myvar, file)  
  
---  
  
 __

 __

### Loading a Variable:  

  * **Method 1:**

The loads() method takes a binary string and returns the corresponding
variable. If the string is invalid, it throws a PickleError.

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pickle

 

# This is the result of previous code

binary_string =
b'\x80\x04\x95K\x00\x00\x00\x00\x00\x00\x00]\x94(}\x94(\x8c\x04This\x94\x8c\x02is\x94\x8c\x07Example\x94K\x01u\x8c\x02of\x94\x8c\rserialisation\x94]\x94(\x8c\x05using\x94\x8c\x06pickle\x94ee.'

 

# Use loads to load the variable

myvar = pickle.loads(binary_string)

 

print(myvar)  
  
---  
  
 __

 __

 **Output:**

> [{‘This’: ‘is’, ‘Example’: 1}, ‘of’, ‘serialisation’, [‘using’, ‘pickle’]]

  *  **Method 2:**

The load() method loads a pickled file and returns a deserialized variable.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pickle

 

# Open the file in binary mode

with open('file.pkl', 'rb') as file:

 

 # Call load method to deserialze

 myvar = pickle.load(file)

 

 print(myvar)  
  
---  
  
 __

 __

 **Output:**

> [{‘This’: ‘is’, ‘Example’: 2}, ‘of’, ‘serialisation’, [‘using’, ‘pickle’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

