Flattening JSON objects in Python



JSON(JavaScript Object Notation) is a data-interchange format that is human-
readable text and is used to transmit data, especially between web
applications and servers. The JSON files will be like nested dictionaries in
Python. To convert a text file into JSON, there is a json module in Python.
This module comes in-built with Python standard modules, so there is no need
to install it externally.

A flatten json is nothing but there is no nesting is present and only key-
value pairs are present.

 **Example:**

>  **Unflattened JSON:**  
>  {‘user’ :{‘Rachel’:{‘UserID’:1717171717,  
> ‘Email’: ‘rachel1999@gmail.com’,  
> ‘friends’: [‘John’, ‘Jeremy’, ‘Emily’]}}}
>
>  **Flattened JSON:**  
>  {‘user_Rachel_friends_2’: ‘Emily’, ‘user_Rachel_friends_0’: ‘John’,
> ‘user_Rachel_UserID’: 1717171717, ‘user_Rachel_Email’:
> ‘rachel1999@gmail.com’, ‘user_Rachel_friends_1’: ‘Jeremy’}
>
>  
>
>
>  
>

#### Need of flattening JSON

There are many reasons for the need of flattening JSON, such as for a better
and understandable view that is there are only key-value pairs are present
without any nesting. It also allows for context-specific security and
constraints to be implemented in a readable, but in more verbose way.

#### Approach to flatten JSON

There are many ways to flatten JSON. There is one recursive way and another by
using the json-flatten library.

 ****

* Recursive Approach:

