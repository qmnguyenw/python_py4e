Python | Intersect two dictionaries through keys



Given two dictionaries, the task is to find the intersection of these two
dictionaries through keys. Let’s see different ways to do this task.  
  
 **Method #1: Using dict comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# intersection of two dictionaries 

# using dict comprehension

 

# inititialising dictionary

ini_dict1 = {'nikhil': 1, 'vashu' : 5, 

 'manjeet' : 10, 'akshat' : 15}

ini_dict2 = {'akshat' :15, 'nikhil' : 1, 'me' :
56}

 

# printing initial json

print ("initial 1st dictionary", ini_dict1)

print ("initial 2nd dictionary", ini_dict2)

 

# intersecting two dictionaries

final_dict = {x:ini_dict1[x] for x in ini_dict1 

 if x in ini_dict2}

 

# printing final result

print ("final dictionary", str(final_dict))  
  
---  
  
 __

 __

 **Output:**

> initial 1st dictionary {‘vashu’: 5, ‘manjeet’: 10, ‘nikhil’: 1, ‘akshat’:
> 15}  
> initial 2nd dictionary {‘nikhil’: 1, ‘me’: 56, ‘akshat’: 15}  
> final dictionary {‘nikhil’: 1, ‘akshat’: 15}

  
**Method #2: Using& operator**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# intersection of two dictionaries 

# using dict comprehension

 

# inititialising dictionary

ini_dict1 = {'nikhil': 1, 'vashu' : 5,

 'manjeet' : 10, 'akshat' : 15}

ini_dict2 = {'akshat' :15, 'nikhil' : 1, 'me' :
56}

 

# printing initial json

print ("initial 1st dictionary", ini_dict1)

print ("initial 2nd dictionary", ini_dict2)

 

# intersecting two dictionaries

final_dict = dict(ini_dict1.items() & ini_dict2.items())

 

# printing final result

print ("final dictionary", str(final_dict))  
  
---  
  
 __

 __

 **Output:**

  

  

> initial 1st dictionary {‘vashu’: 5, ‘manjeet’: 10, ‘nikhil’: 1, ‘akshat’:
> 15}  
> initial 2nd dictionary {‘nikhil’: 1, ‘akshat’: 15, ‘me’: 56}  
> final dictionary {‘nikhil’: 1, ‘akshat’: 15}

