How to convert JSON to Ordereddict?



The full-form of JSON is JavaScript Object Notation. It means that a script
(executable) file which is made of text in a programming language, is used to
store and transfer the data. Python supports JSON through a built-in package
called _json_. To use this feature, we import the _json_ package in Python
script. The text in JSON is done through quoted-string which contains a value
in key-value mapping within { }. It is similar to the dictionary in Python.

An _OrderedDict_ is a dictionary subclass that remembers the order that keys
were first inserted. The only difference between _dict()_ and _OrderedDict()_
is that: _OrderedDict_ preserves the order in which the keys are inserted. A
regular _dict_ doesn’t track the insertion order and iterating it gives the
values in an arbitrary order.

In this article we are going to discuss various methods to convert _JSON_ to
_Ordereddict_.

 **Method #1**

By specifying the _object_pairs_hook_ argument to _JSONDecoder._

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# import required modules

import json

from collections import OrderedDict

 

# assign json file

jsonFile = '{"Geeks":1, "for": 2, "geeks":3}'

print(jsonFile)

 

# convert to Ordereddict

data =
json.JSONDecoder(object_pairs_hook=OrderedDict).decode(jsonFile)

print(data)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    {"Geeks":1, "for": 2, "geeks":3}
    OrderedDict([(u'Geeks', 1), (u'for', 2), (u'geeks', 3)])

 **Method #2**

By passing the JSON data as a parameter to __json.loads().

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# import required modules

import json

from collections import OrderedDict

 

# assign json file

jsonFile = '{"Geeks":1, "for": 2, "geeks":3}'

print(jsonFile)

 

# convert to Ordereddict

data = json.loads(jsonFile, 

 object_pairs_hook=OrderedDict)

print(data)  
  
---  
  
 __

 __

 **Output:**

    
    
    {"Geeks":1, "for": 2, "geeks":3}
    OrderedDict([(u'Geeks', 1), (u'for', 2), (u'geeks', 3)])

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

