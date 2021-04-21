Python | Difference in keys of two dictionaries



Given two dictionaries _dic1_ and _dic2_ which may contain same-keys, find the
difference of keys in given dictionaries.

 **Code #1 :** Using set to find keys that are _missing_.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find the difference in

# keys in two dictionary

 

# Initialising dictionary 

dict1= {'key1':'Geeks', 'key2':'For',
'key3':'geeks'}

dict2= {'key1':'Geeks', 'key2:':'Portal'}

 

diff = set(dict2) - set(dict1)

 

# Printing difference in

# keys in two dictionary

print(diff)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'key2:'}
    

  
**Code #2 :** Finding keys in dict2 which are _not_ in dict1.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find difference in keys in two dictionary

 

# Initialising dictionary 

dict1= {'key1':'Geeks', 'key2':'For'}

dict2= {'key1':'Geeks', 'key2':'For',
'key3':'geeks',

 'key4': {'GeekKey1': 12, 'GeekKey2': 22, 'GeekKey3':
32 }}

 

for key in dict2.keys():

 if not key in dict1:

 

 # Printing difference in

 # keys in two dictionary

 print(key)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    key4
    key3
    

