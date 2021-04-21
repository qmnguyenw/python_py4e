Python | Get items in sorted order from given dictionary



Given a dictionary, the task is to get all items from the dictionary in sorted
order. Let’s discuss different ways we can do this task.

 **Method #1: Usingsorted()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to get sorted items from dictionary

 

# initialising _dictionary

ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c':
'chandan'}

 

# printing iniial_dictionary

print ("iniial_dictionary", str(ini_dict))

 

# getting items in sorted order

print ("\nItems in sorted order")

for key in sorted(ini_dict):

 print (ini_dict[key])  
  
---  
  
 __

 __

 **Output:**

    
    
    iniial_dictionary {'b': 'bhuvan', 'c': 'chandan', 'a': 'akshat'}
    
    Items in sorted order
    akshat
    bhuvan
    chandan
    

  
**Method #2: Using d.items()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to get sorted items from dictionary

 

# initialising _dictionary

ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c':
'chandan'}

 

# printing iniial_dictionary

print ("iniial_dictionary", str(ini_dict))

 

# getting items in sorted order

print ("\nItems in sorted order")

for key, value in sorted(ini_dict.items()):

 print(value)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    iniial_dictionary {'a': 'akshat', 'b': 'bhuvan', 'c': 'chandan'}
    
    Items in sorted order
    akshat
    bhuvan
    chandan
    

