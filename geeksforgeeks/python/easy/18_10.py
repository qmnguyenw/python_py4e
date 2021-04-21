Iterate over a dictionary in Python



Dictionary in Python is an unordered collection of data values, used to store
data values like a map, which unlike other Data Types that hold only single
value as an element, Dictionary holds key:value pair.

There are multiple ways to iterate over a dictionary in Python.

  * Iterate through all keys
  * Iterate through all values
  * Iterate through all key, value pairs

 **Iterate through all keys:**

The order of states in the below code will change every time because the
dictionary doesn’t store keys in a particular order.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to iterate through all keys in a dictionary

 

statesAndCapitals = {

 'Gujarat' : 'Gandhinagar',

 'Maharashtra' : 'Mumbai',

 'Rajasthan' : 'Jaipur',

 'Bihar' : 'Patna'

 }

 

print('List Of given states:\n')

 

# Iterating over keys

for state in statesAndCapitals:

 print(state)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    List Of given states:
    
    Rajasthan
    Bihar
    Maharashtra
    Gujarat
    

