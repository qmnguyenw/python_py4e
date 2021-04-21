Python | Convert nested dictionary into flattened dictionary



Given a nested dictionary, the task is to convert this dictionary into a
flattened dictionary where the key is separated by ‘_’ in case of the nested
key to be started.

Given below are a few methods to solve the above task.

 **Method #1: Using Naive Approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of nested dictionary

# into flattened dictionary

 

# code to convert ini_dict to flattened dictionary

# default seperater '_'

def flatten_dict(dd, separator ='_', prefix =''):

 return { prefix + separator + k if prefix else k : v

 for kk, vv in dd.items()

 for k, v in flatten_dict(vv, separator, kk).items()

 } if isinstance(dd, dict) else { prefix : dd }

 

# initialising_dictionary

ini_dict = {'geeks': {'Geeks': {'for': 7}},

 'for': {'geeks': {'Geeks': 3}},

 'Geeks': {'for': {'for': 1, 'geeks': 4}}}

 

# priniting initial dictionary

print ("initial_dictionary", str(ini_dict))

 

 

# printing final dictionary

print ("final_dictionary", str(flatten_dict(ini_dict)))  
  
---  
  
 __

 __

 **Output:**

> initial_dictionary {‘geeks’: {‘Geeks’: {‘for’: 7}}, ‘Geeks’: {‘for’:
> {‘geeks’: 4, ‘for’: 1}}, ‘for’: {‘geeks’: {‘Geeks’: 3}}}  
> final_dictionary {‘Geeks_for_for’: 1, ‘geeks_Geeks_for’: 7,
> ‘for_geeks_Geeks’: 3, ‘Geeks_for_geeks’: 4}
>
>  
>
>
>  
>

  
**Method #2: Using _mutuableMapping_**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of nested dictionary

# into flattened dictionary

 

from collections import MutableMapping

 

# code to convert ini_dict to flattened dictionary

# default seperater '_'

def convert_flatten(d, parent_key ='', sep ='_'):

 items = []

 for k, v in d.items():

 new_key = parent_key + sep + k if parent_key else k

 

 if isinstance(v, MutableMapping):

 items.extend(convert_flatten(v, new_key, sep = sep).items())

 else:

 items.append((new_key, v))

 return dict(items)

 

# initialising_dictionary

ini_dict = {'geeks': {'Geeks': {'for': 7}},

 'for': {'geeks': {'Geeks': 3}},

 'Geeks': {'for': {'for': 1, 'geeks': 4}}}

 

# priniting initial dictionary

print ("initial_dictionary", str(ini_dict))

 

 

# printing final dictionary

print ("final_dictionary", str(convert_flatten(ini_dict)))  
  
---  
  
 __

 __

 **Output:**

> initial_dictionary {‘Geeks’: {‘for’: {‘for’: 1, ‘geeks’: 4}}, ‘for’:
> {‘geeks’: {‘Geeks’: 3}}, ‘geeks’: {‘Geeks’: {‘for’: 7}}}  
> final_dictionary {‘Geeks_for_geeks’: 4, ‘for_geeks_Geeks’: 3,
> ‘geeks_Geeks_for’: 7, ‘Geeks_for_for’: 1}

  
**Method #3: Using Python _Generators_**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of nested dictionary

# into flattened dictionary

 

my_map = {"a" : 1,

 "b" : {

 "c": 2,

 "d": 3,

 "e": {

 "f":4,

 6:"a",

 5:{"g" : 6},

 "l":[1,"two"]

 }

 }}

 

# Expected Output

# {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 'a', 'b_e_5_g': 6,
'b_e_l': [1, 'two']}

 

 

ini_dict = {'geeks': {'Geeks': {'for': 7}},

 'for': {'geeks': {'Geeks': 3}},

 'Geeks': {'for': {'for': 1, 'geeks': 4}}}

 

# Expected Output

# {‘Geeks_for_geeks’: 4, ‘for_geeks_Geeks’: 3, ‘Geeks_for_for’: 1,
‘geeks_Geeks_for’: 7}

 

def flatten_dict(pyobj, keystring=''):

 if type(pyobj) == dict:

 keystring = keystring + '_' if keystring else keystring

 for k in pyobj:

 yield from flatten_dict(pyobj[k], keystring + str(k))

 else:

 yield keystring, pyobj

 

print("Input : %s\nOutput : %s\n\n" %

 (my_map, { k:v for k,v in flatten_dict(my_map) }))

 

print("Input : %s\nOutput : %s\n\n" %

 (ini_dict, { k:v for k,v in flatten_dict(ini_dict) }))  
  
---  
  
 __

 __

 **Output:**

> initial_dictionary {‘for’: {‘geeks’: {‘Geeks’: 3}}, ‘geeks’: {‘Geeks’:
> {‘for’: 7}}, ‘Geeks’: {‘for’: {‘for’: 1, ‘geeks’: 4}}}  
> final_dictionary {‘Geeks_for_geeks’: 4, ‘for_geeks_Geeks’: 3,
> ‘Geeks_for_for’: 1, ‘geeks_Geeks_for’: 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

