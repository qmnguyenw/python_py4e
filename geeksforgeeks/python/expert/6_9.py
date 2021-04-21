json.dumps() in Python



The full-form of JSON is JavaScript Object Notation. It means that a script
(executable) file which is made of text in a programming language, is used to
store and transfer the data. Python supports JSON through a built-in package
called json. To use this feature, we import the json package in Python
script. The text in JSON is done through quoted-string which contains the
value in key-value mapping within { }. It is similar to the dictionary in
Python.

 **Note:** For more information, refer to Read, Write and Parse JSON using
Python

## Json.dumps()

json.dumps() function converts a Python object into a json string.

>  **Syntax:**  
>  json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
> allow_nan=True, cls=None, indent=None, separators=None, default=None,
> sort_keys=False, **kw)
>
>  **Parameters:**  
>  **obj:** Serialize obj as a JSON formatted stream  
>  **skipkeys:** If skipkeys is true (default: False), then dict keys that are
> not of a basic type (str, int, float, bool, None) will be skipped instead of
> raising a TypeError.  
>  **ensure_ascii:** If ensure_ascii is true (the default), the output is
> guaranteed to have all incoming non-ASCII characters escaped. If
> ensure_ascii is false, these characters will be output as-is.  
>  **check_circular :** If check_circular is false (default: True), then the
> circular reference check for container types will be skipped and a circular
> reference will result in an OverflowError (or worse).  
>  **allow_nan :** If allow_nan is false (default: True), then it will be a
> ValueError to serialize out of range float values (nan, inf, -inf) in strict
> compliance of the JSON specification. If allow_nan is true, their JavaScript
> equivalents (NaN, Infinity, -Infinity) will be used.  
>  **indent:** If indent is a non-negative integer or string, then JSON array
> elements and object members will be pretty-printed with that indent level.
> An indent level of 0, negative, or “” will only insert newlines. None (the
> default) selects the most compact representation. Using a positive integer
> indent indents that many spaces per level. If indent is a string (such as
> “\t”), that string is used to indent each level.  
>  **separators :** If specified, separators should be an (item_separator,
> key_separator) tuple. The default is (‘, ‘, ‘: ‘) if indent is None and (‘,
> ‘, ‘: ‘) otherwise. To get the most compact JSON representation, you should
> specify (‘, ‘, ‘:’) to eliminate whitespace.  
>  **default:** If specified, default should be a function that gets called
> for objects that can’t otherwise be serialized. It should return a JSON
> encodable version of the object or raise a TypeError. If not specified,
> TypeError is raised.  
>  **sort_keys :** If sort_keys is true (default: False), then the output of
> dictionaries will be sorted by key.
>
>  
>
>
>  
>

 **Example #1:** Passing the Python dictionary to json.dumps() function will
return a string.

 __

 __  
 __

 __

 __  
 __  
 __

import json

 

# Creating a dictionary

Dictionary ={1:'Welcome', 2:'to',

 3:'Geeks', 4:'for',

 5:'Geeks'}

 

# Converts input dictionary into

# string and stores it in json_string

json_string = json.dumps(Dictionary)

print('Equivalent json string of input dictionary:',

 json_string)

print(" ")

 

# Checking type of object

# returned by json.dumps

print(type(json_string))  
  
---  
  
 __

 __

 **Output**

> Equivalent json string of dictionary: {“1”: “Welcome”, “2”: “to”, “3”:
> “Geeks”, “4”: “for”, “5”: “Geeks”}  
> <class ‘str’>

 **Example #2:** By setting the skipkeys to True(default: False) we
automatically skip the keys that are not of basic type.

 __

 __  
 __

 __

 __  
 __  
 __

import json

 

 

Dictionary ={(1, 2, 3):'Welcome', 2:'to',

 3:'Geeks', 4:'for',

 5:'Geeks'}

 

 

# Our dictionary contains tuple

# as key, so it is automatically 

# skipped If we have not set

# skipkeys = True then the code 

# throws the error 

json_string = json.dumps(Dictionary, 

 skipkeys = True)

 

print('Equivalent json string of dictionary:', 

 json_string)  
  
---  
  
 __

 __

 **Output**

> Equivalent json string of dictionary: {“2”: “to”, “3”: “Geeks”, “4”: “for”,
> “5”: “Geeks”}

 **Example #3:**

 __

 __  
 __

 __

 __  
 __  
 __

import json

 

 

# We are adding nan values

# (out of range float values)

# in dictionary

Dictionary ={(1, 2, 3):'Welcome', 2:'to',

 3:'Geeks', 4:'for',

 5:'Geeks', 6:float('nan')}

 

# If we hadn't set allow_nan to 

# true we would have got 

# ValueError: Out of range float 

# values are not JSON compliant

json_string = json.dumps(Dictionary,

 skipkeys = True,

 allow_nan = True)

 

print('Equivalent json string of dictionary:', 

 json_string)  
  
---  
  
 __

 __

 **Output :**

  

  

> Equivalent json string of dictionary: {“2”: “to”, “3”: “Geeks”, “4”: “for”,
> “5”: “Geeks”, “6”: NaN}

 **Example #4:**

 __

 __  
 __

 __

 __  
 __  
 __

import json

 

 

Dictionary ={(1, 2, 3):'Welcome', 2:'to',

 3:'Geeks', 4:'for',

 5:'Geeks', 6:float('nan')}

 

# Indentation can be used 

# for pretty-printing

json_string = json.dumps(Dictionary, 

 skipkeys = True, 

 allow_nan = True,

 indent = 6)

 

print('Equivalent json string of dictionary:', 

 json_string)  
  
---  
  
 __

 __

 **Output:**

    
    
    Equivalent json string of dictionary: {
          "2": "to",
          "3": "Geeks",
          "4": "for",
          "5": "Geeks",
          "6": NaN
    }

 **Example #5:**

 __

 __  
 __

 __

 __  
 __  
 __

import json

 

Dictionary ={(1, 2, 3):'Welcome', 2:'to',

 3:'Geeks', 4:'for',

 5:'Geeks', 6:float('nan')}

 

# If specified, separators should be

# an (item_separator, key_separator)tuple

# Items are seperated by '.' and key,

# values are seperated by '='

json_string = json.dumps(Dictionary,

 skipkeys = True, 

 allow_nan = True,

 indent = 6,

 separators =(". ", " = "))

 

print('Equivalent json string of dictionary:',

 json_string)  
  
---  
  
 __

 __

 **Output:**

    
    
    Equivalent json string of dictionary: {
          "2" = "to". 
          "3" = "Geeks". 
          "4" = "for". 
          "5" = "Geeks". 
          "6" = NaN
    }

 **Example #6:**

 __

 __  
 __

 __

 __  
 __  
 __

import json

 

Dictionary ={'c':'Welcome', 'b':'to',

 'a':'Geeks'}

 

json_string = json.dumps(Dictionary,

 indent = 6,

 separators =(". ", " = "),

 sort_keys = True)

 

print('Equivalent json string of dictionary:',

 json_string)  
  
---  
  
 __

 __

 **Output:**

    
    
    Equivalent json string of dictionary: {
          "a" = "Geeks". 
          "b" = "to". 
          "c" = "Welcome"
    }

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

