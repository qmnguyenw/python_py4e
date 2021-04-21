Python | Split dictionary keys and values into separate lists



Given a dictionary, the task is to split that dictionary into keys and values
into different lists. Let’s discuss the different ways we can do this.

 **Method #1: Usingbuilt-in functions**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to split dictionary

# into keys and values

 

# initialising _dictionary

ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c':
'chandan'}

 

# printing iniial_dictionary

print("intial_dictionary", str(ini_dict))

 

# split dictionary into keys and values

keys = ini_dict.keys()

values = ini_dict.values()

 

# printing keys and values separately

print ("keys : ", str(keys))

print ("values : ", str(values))  
  
---  
  
 __

 __

 **Output:**

    
    
    intial_dictionary {'a': 'akshat', 'b': 'bhuvan', 'c': 'chandan'}
    keys :  dict_keys(['a', 'b', 'c'])
    values :  dict_values(['akshat', 'bhuvan', 'chandan'])
    

  
**Method #2: Usingzip()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to split dictionary

# into keys and values

 

# initialising _dictionary

ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c':
'chandan'}

 

# printing iniial_dictionary

print("intial_dictionary", str(ini_dict))

 

# split dictionary into keys and values

keys, values = zip(*ini_dict.items())

 

# printing keys and values separately

print ("keys : ", str(keys))

print ("values : ", str(values))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    intial_dictionary {'a': 'akshat', 'c': 'chandan', 'b': 'bhuvan'}
    keys :  ('a', 'c', 'b')
    values :  ('akshat', 'chandan', 'bhuvan')
    

