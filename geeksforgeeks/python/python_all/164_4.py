Python | Initialize a dictionary with only keys from a list



Given a List, the task is to create a dictionary with only keys by using given
list as keys.

Let’s see the different methods we can do this task.

 **Method #1** : By iterating through list

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to initialize a dictionary

# with only keys from a list

 

# List of keys

keyList = ["Paras", "Jain", "Cyware"]

 

# initialize dictionary

d = {}

 

# iterating through the elements of list

for i in keyList:

 d[i] = None

 

print(d)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Cyware': None, 'Paras': None, 'Jain': None}
    

  
**Method #2 :** Using dictionary comprehension

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to initialize a dictionary

# with only keys from a list

 

# List of Keys

keyList = ["Paras", "Jain", "Cyware"]

 

# Using Dictionary comprehension

myDict = {key: None for key in keyList}

print(myDict)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Paras': None, 'Jain': None, 'Cyware': None}
    

  
**Method #3 :** Using zip() function

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to initialize a dictionary

# with only keys from a list

 

# List of keys

listKeys = ["Paras", "Jain", "Cyware"]

 

# using zip() function to create a dictionary

# with keys and same length None value 

dct = dict(zip(listKeys, [None]*len(listKeys)))

 

# print dict

print(dct)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Cyware': None, 'Paras': None, 'Jain': None}
    

  
**Method #4 :** Using fromkeys() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to initialize a dictionary

# with only keys from a list

 

# List of keys

Student = ["Paras", "Jain", "Cyware"]

 

# using fromkeys() method

StudentDict = dict.fromkeys(Student, None)

 

# printing dictionary

print(StudentDict)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Cyware': None, 'Jain': None, 'Paras': None}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

