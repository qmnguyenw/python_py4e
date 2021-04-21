Python | Convert a set into dictionary



Sometimes we need to convert one data structure into another for various
operations and problems in our day to day coding and web development. Like we
may want to get a dictionary from the given set elements.

Let’s discuss a few methods to convert given set into a dictionary.

 **Method #1:** Using fromkeys()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting set into dictionary

# using fromkeys()

 

# initializing set

ini_set = {1, 2, 3, 4, 5}

 

# printing intialized set

print ("initial string", ini_set)

print (type(ini_set))

 

# Converting set to dictionary

res = dict.fromkeys(ini_set, 0)

 

# printing final result and its type

print ("final list", res)

print (type(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string {1, 2, 3, 4, 5}
    <class 'set'>
    final list {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    <class 'dict'>
    

  
**Method #2:** Using dict comprehension

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting set into dictionary

# using dict comprehension

 

 

# initializing set

ini_set = {1, 2, 3, 4, 5}

 

# printing intialized set

print ("initial string", ini_set)

print (type(ini_set))

 

str = 'fg'

# Converting set to dict

res = {element:'Geek'+str for element in ini_set}

 

# printing final result and its type

print ("final list", res)

print (type(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string {1, 2, 3, 4, 5}
    <class 'set'>
    final list {1: 'Geek', 2: 'Geek', 3: 'Geek', 4: 'Geek', 5: 'Geek'}
    <class 'dict'>
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

