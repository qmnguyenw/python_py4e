Python | Ways to change keys in dictionary



Given a dictionary, the task is to change the key based on the requirement.
Let’s see different methods we can do this task.

 **Method #1 : Using naive method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# changing keys of dictionary

# using naive method

 

# inititialising dictionary

ini_dict = {'nikhil': 1, 'vashu' : 5,

 'manjeet' : 10, 'akshat' : 15}

 

# printing initial json

print ("initial 1st dictionary", ini_dict)

 

# changing keys of dictionary

ini_dict['akash'] = ini_dict['akshat']

del ini_dict['akshat']

 

 

# printing final result

print ("final dictionary", str(ini_dict))  
  
---  
  
 __

 __

 **Output:**

> initial 1st dictionary {‘akshat’: 15, ‘nikhil’: 1, ‘manjeet’: 10, ‘vashu’:
> 5}  
> final dictionary {‘akash’: 15, ‘nikhil’: 1, ‘manjeet’: 10, ‘vashu’: 5}

  
**Method #2: Usingpop()**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# changing keys of dictionary

# using pop() method

 

# inititialising dictionary

ini_dict = {'nikhil': 1, 'vashu' : 5, 

 'manjeet' : 10, 'akshat' : 15}

 

# printing initial json

print ("initial 1st dictionary", ini_dict)

 

# changing keys of dictionary

ini_dict['akash'] = ini_dict.pop('akshat')

 

# printing final result

print ("final dictionary", str(ini_dict))  
  
---  
  
 __

 __

 **Output:**

> initial 1st dictionary {‘akshat’: 15, ‘manjeet’: 10, ‘vashu’: 5, ‘nikhil’:
> 1}  
> final dictionary {‘akash’: 15, ‘manjeet’: 10, ‘vashu’: 5, ‘nikhil’: 1}

  
**Method #3: Using zip()**

Suppose we want to change all keys of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# changing all keys of dictionary

# corresponding to list using zip()

 

# inititialising dictionary

ini_dict = {'nikhil': 1, 'vashu' : 5, 

 'manjeet' : 10, 'akshat' : 15}

 

# initialising list

ini_list = ['a', 'b', 'c', 'd']

 

# printing initial json

print ("initial 1st dictionary", ini_dict)

 

# changing keys of dictionary

final_dict = dict(zip(ini_list, list(ini_dict.values())))

 

# printing final result

print ("final dictionary", str(final_dict))  
  
---  
  
 __

 __

 **Output:**

> initial 1st dictionary {‘akshat’: 15, ‘manjeet’: 10, ‘vashu’: 5, ‘nikhil’:
> 1}  
> final dictionary {‘c’: 5, ‘d’: 1, ‘a’: 15, ‘b’: 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

