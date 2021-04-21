Serializing Data Using the pickle and cPickle Modules



Serialization is a process of storing an object as a stream of bytes or
characters in order to transmit it over a network or store it on the disk to
recreate it along with its state whenever required. The reverse process is
called deserialization.

In Python, the Pickle module provides us the means to serialize and
deserialize the python objects. Pickle is a powerful library that can
serialize many complex and custom objects that other library fails to do. Just
like pickle, there is a cPickle module that shares the same methods as pickle,
but it is written in C. The cPickle module is written as a C function instead
of a class format.

### Difference between Pickle and cPickle:

  * Pickle uses python class-based implementation while cPickle is written as C functions. As a result, cPickle is many times faster than pickle.
  * Pickle is available in both python 2.x and python 3.x while cPickle is available in python 2.x by default. To use cPickle in python 3.x, we can import _pickle.
  * cPickle does not support subclass from pickle. cPickle is better if subclassing is not important otherwise Pickle is the best option.

Since both pickle and cPickle share the same interface, we can use both of
them in the same way. Below is an example code as a reference:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

try:

 

 # In python 2.x it is available as default

 import cPickle as pickle

except ImportError:

 

 # In python 3.x cPickle is not available

 import pickle

 

import random

 

# A custom class to demonstrate pickling 

class ModelTrainer:

 def __init__(self) -> None:

 self.weights = [0,0,0]

 

 def train(self):

 for i in range(len(self.weights)):

 self.weights[i] = random.random()

 

 def get_weights(self):

 return self.weights

 

# Create an object 

model = ModelTrainer()

 

# Populate the data

model.train()

 

print('Weights before pickling', model.get_weights())

 

# Open a file to write bytes

p_file = open('model.pkl', 'wb')

 

# Pickle the object

pickle.dump(model, p_file)

p_file.close()

 

# Deserialization of the file

file = open('model.pkl','rb')

new_model = pickle.load(file)

 

print('Weights after pickling', new_model.get_weights())  
  
---  
  
 __

 __

 **Output:**

  

  

> Weights before pickling [0.6089721131909885, 0.7891019431265203,
> 0.5653418337976294]
>
> Weights after pickling [0.6089721131909885, 0.7891019431265203,
> 0.5653418337976294]

In the above code, we have created a custom class ModelTrainer that
initializes a list of 0’s. The train() method populates the list with some
random values and get_weight() method returns the generated values. Next, we
have created the model object and printed the generated weights. We have
created a new file in ‘wb’ (Write bytes) mode. The dump() method dumped the
object as bytes stream into the file. Verification is done by loading the file
in a new object and printing the weights.

Pickle module is very powerful for python objects. But it can only preserve
the data, not the class structure. Hence, any custom class object won’t load
if we don’t provide the class definition. Below is an example when depickling
fails:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

try:

 # In python 2.x it is available as default

 import cPickle as pickle

except ImportError:

 

 # In python 3.x cPickle is not available

 import pickle

 

# Deserialization of the file

file = open('model.pkl','rb')

new_model = pickle.load(file)

 

print('Weights of model', new_model.get_weights())  
  
---  
  
 __

 __

 **Output:**

> Traceback (most recent call last):
>
> File “des.py”, line 12, in <module>
>
>  
>
>
>  
>
>
> new_model = pickle.load(file)
>
> AttributeError: Can’t get attribute ‘ModelTrainer’ on <module ‘__main__’
> from ‘des.py’>

The above error was generated because our current script doesn’t know about
the class of this object. Thus, we can say that pickle is only preserving the
data inside the object but it cannot save the methods and class structure.

To rectify the above error, we must provide the class definition to the
script. Below is an example of how to correctly load custom objects:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

try:

 

 # In python 2.x it is available as default

 import cPickle as pickle

except ImportError:

 

 # In python 3.x cPickle is not available

 import pickle

 

import random

 

# If the file is available,

# we can use import statement to import the class

 

# A custom class to demonstrate pickling

class ModelTrainer:

 def __init__(self) -> None:

 self.weights = [0, 0, 0]

 

 def train(self):

 for i in range(len(self.weights)):

 self.weights[i] = random.random()

 

 def get_weights(self):

 return self.weights

 

# Deserialization of the file

file = open('model.pkl', 'rb')

new_model = pickle.load(file)

 

print('Weights of model', new_model.get_weights())  
  
---  
  
 __

 __

 **Output:**

> Weights of model [0.6089721131909885, 0.7891019431265203,
> 0.5653418337976294]

We have provided a reference for ModelTrainer class. The script now recognizes
the class, and it can call the constructor again to build the object. Instead
of typing the whole class code, we can simply import it from the previous
file.

#### Serialization as string

We can also serialize an object as a string. Pickle and cPickle modules
provide dumps() and loads() methods. The dumps() method takes the object as
the parameter and returns the encoded string. The load() method does the
reverse. It takes the encoded string and returns the original object. Below is
the code to serialize a custom object as a string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

try:

 

 # In python 2.x it is available as default

 import cPickle as pickle

except ImportError:

 

 # In python 3.x cPickle is not available

 import pickle

 

import random

 

# A custom class to demonstrate pickling 

class ModelTrainer:

 def __init__(self) -> None:

 self.weights = [0,0,0]

 

 def train(self):

 for i in range(len(self.weights)):

 self.weights[i] = random.random()

 

 def get_weights(self):

 return self.weights

 

# Create an object 

model = ModelTrainer()

 

# Populate the data

model.train()

 

print('Weights before pickling', model.get_weights())

 

# Pickle the object

byte_string = pickle.dumps(model)

 

print("The bytes of object are:",byte_string)

 

# Deserialization of the object using same byte string

new_model = pickle.loads(byte_string)

 

print('Weights after depickling', new_model.get_weights())  
  
---  
  
 __

 __

 **Output:**

> Weights before pickling [0.923474126606742, 0.34909608824193983,
> 0.3761122243447367]
>
> The bytes of object are:
> b’\x80\x03c__main__\nModelTrainer\nq\x00)\x81q\x01}q\x02X\x07\x00\x00\x00weightsq\x03]q\x04(G?\xed\x8d\x19\x9c\x8fL\xc3G?\xd6W\x97\x1e\x8aHHG?\xd8\x129\x01\xcb\xee\xf2esb.’
>
> Weights after depickling [0.923474126606742, 0.34909608824193983,
> 0.3761122243447367]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

