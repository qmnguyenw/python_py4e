Python | Convert flattened dictionary into nested dictionary



Given a flattened dictionary, the task is to convert that dictionary into a
nested dictionary where keys are needed to be split at ‘_’ considering where
nested dictionary will be started.

 **Method #1: Using Naive Approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conersion of flattened dictionary

# into nested dictionary

 

 

def insert(dct, lst):

 for x in lst[:-2]:

 dct[x] = dct = dct.get(x, dict())

 dct.update({lst[-2]: lst[-1]})

 

 

def convert_nested(dct):

 # empty dict to store the result

 result = dict()

 

 # create an iterator of lists 

 # representing nested or hierarchial flow

 lsts = ([*k.split("_"), v] for k, v in dct.items())

 

 # insert each list into the result

 for lst in lsts:

 insert(result, lst)

 return result

 

# initialising_dictionary

ini_dict = {'Geeks_for_for':1,'Geeks_for_geeks':4,

 'for_geeks_Geeks':3,'geeks_Geeks_for':7}

 

# priniting initial dictionary

print ("initial_dictionary", str(ini_dict))

 

# code to convert ini_dict to nested 

# dictionary splitting_dict_keys

_split_dict = [[*a.split('_'), b] for a, b in
ini_dict.items()]

 

 

# printing final dictionary

print ("final_dictionary", str(convert_nested(ini_dict)))  
  
---  
  
 __

 __

 **Output:**

> initial_dictionary {‘for_geeks_Geeks’: 3, ‘Geeks_for_geeks’: 4,
> ‘geeks_Geeks_for’: 7, ‘Geeks_for_for’: 1}  
> final_dictionary {‘Geeks’: {‘for’: {‘for’: 1, ‘geeks’: 4}}, ‘for’: {‘geeks’:
> {‘Geeks’: 3}}, ‘geeks’: {‘Geeks’: {‘for’: 7}}}

  
**Method #2: Using default _dict_ and recursive approach**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conersion of flattened dictionary

# into nested dictionary

 

# code to conert dict into nested dict

def nest_dict(dict1):

 result = {}

 for k, v in dict1.items():

 

 # for each key call method split_rec which

 # will split keys to form recursively 

 # nested dictionary

 split_rec(k, v, result)

 return result

 

def split_rec(k, v, out):

 

 # splitting keys in dict

 # calling_recursively to break items on '_'

 k, *rest = k.split('_', 1)

 if rest:

 split_rec(rest[0], v, out.setdefault(k, {}))

 else:

 out[k] = v

 

 

# initialising_dictionary

ini_dict = {'Geeks_for_for':1,'Geeks_for_geeks':4,

 'for_geeks_Geeks':3,'geeks_Geeks_for':7}

 

# priniting initial dictionary

print ("initial_dictionary", str(ini_dict))

 

# printing final dictionary

print ("final_dictionary", str(nest_dict(ini_dict)))  
  
---  
  
 __

 __

 **Output:**

> initial_dictionary {‘for_geeks_Geeks’: 3, ‘Geeks_for_for’: 1,
> ‘Geeks_for_geeks’: 4, ‘geeks_Geeks_for’: 7}  
> final_dictionary {‘for’: {‘geeks’: {‘Geeks’: 3}}, ‘geeks’: {‘Geeks’: {‘for’:
> 7}}, ‘Geeks’: {‘for’: {‘for’: 1, ‘geeks’: 4}}}

  
**Method #3: Using _reduce_ and _getitem_**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conersion of flattened dictionary

# into nested dictionary

 

from collections import defaultdict

from functools import reduce

from operator import getitem

 

 

def getFromDict(dataDict, mapList):

 

 # Iterate nested dictionary

 return reduce(getitem, mapList, dataDict)

 

# instantiate nested defaultdict of defaultdicts

tree = lambda: defaultdict(tree)

d = tree()

 

# conerting default_dict_to regular dict

def default_to_regular(d):

 

 """Convert nested defaultdict to regular dict of dicts."""

 if isinstance(d, defaultdict):

 d = {k: default_to_regular(v) for k, v in d.items()}

 return d

 

# initialising_dictionary

ini_dict = {'Geeks_for_for':1,'Geeks_for_geeks':4,

 'for_geeks_Geeks':3,'geeks_Geeks_for':7}

 

# priniting initial dictionary

print ("initial_dictionary", str(ini_dict))

 

 

# code to convert ini_dict to nested dictionary

# iterating_over_dict

for k, v in ini_dict.items():

 

 # splitting keys

 * keys, final_key = k.split('_')

 getFromDict(d, keys)[final_key] = v

 

# printing final dictionary

print ("final_dictionary", str(default_to_regular(d)))  
  
---  
  
 __

 __

 **Output:**

> initial_dictionary {‘Geeks_for_for’: 1, ‘Geeks_for_geeks’: 4,
> ‘for_geeks_Geeks’: 3, ‘geeks_Geeks_for’: 7}  
> final_dictionary {‘Geeks’: {‘for’: {‘geeks’: 4, ‘for’: 1}}, ‘geeks’:
> {‘Geeks’: {‘for’: 7}}, ‘for’: {‘geeks’: {‘Geeks’: 3}}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

