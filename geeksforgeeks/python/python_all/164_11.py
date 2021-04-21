Python | Sum values for each key in nested dictionary



Given a nested dictionary and we have to find sum of particular value in that
nested dictionary. This is basically useful in cases where we are given a JSON
object or we have scraped a particular page and we want to sum the value of a
particular attribute in objects.

 **Code #1:** Find sum of sharpness values using sum() function

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find sum values within nested dictionaries

weapons = {'': None, 'sword': { 'steel': 151,

 'sharpness': 100,

 'age': 2,},

 

 'arrow': {'steel': 120,

 'sharpness': 205,

 'age': 1,}}

 

sumValue1 = sum(d['sharpness'] for d in weapons.values()
if d)

sumValue2 = sum(d['steel'] for d in weapons.values() if
d)

 

print(sumValue1)

print(sumValue2)  
  
---  
  
 __

 __

 **Output:**

    
    
    305
    271
    

**Code #2 :** Using Iteration to convert it into key:value pair.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find sum values within nested dictionaries

 

weapons = {'': None, 'sword': { 'steel': 151,

 'sharpness': 100,

 'age': 2,},

 

 'arrow': {'steel': 120,

 'sharpness': 205,

 'age': 1,}}

 

sum = 0

 

# iterating key value pair

for key ,value in weapons.items():

 

 if value and 'sharpness' in value.keys():

 # Adding value of sharpness to sum

 sum += value['sharpness'] 

 

# printing sum

print(sum)  
  
---  
  
 __

 __

 **Output:**

    
    
    305
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

