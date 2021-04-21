Python | Convert a string representation of list into list



Many times, we come over the dumped data that is found in the string format
and we require it to be represented into the actual list format in which it
was actually found. This kind of problem of converting a list represented in
string format back to list to perform tasks are quite common in web
development. Let’s discuss certain ways in which this can be performed.

 **Method #1:** Using split() and strip()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate converting

# string representation of list to list

# using strip and split

 

# initializing string representation of a list

ini_list = "[1, 2, 3, 4, 5]"

 

# printing initialized string of list and its type

print ("initial string", ini_list)

print (type(ini_list))

 

# Converting string to list

res = ini_list.strip('][').split(', ')

 

# printing final result and its type

print ("final list", res)

print (type(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string [1, 2, 3, 4, 5]
    <class 'str'>
    final list ['1', '2', '3', '4', '5']
    <class 'list'>
    

  
**Method #2:** Using ast.literal_eval()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate converting

# string representation of list to list

# using ast.literal_eval()

import ast

 

# initializing string representation of a list

ini_list = "[1, 2, 3, 4, 5]"

 

# printing initialized string of list and its type

print ("initial string", ini_list)

print (type(ini_list))

 

# Converting string to list

res = ast.literal_eval(ini_list)

 

# printing final result and its type

print ("final list", res)

print (type(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial string [1, 2, 3, 4, 5]
    <class 'str'>
    final list [1, 2, 3, 4, 5]
    <class 'list'>
    

