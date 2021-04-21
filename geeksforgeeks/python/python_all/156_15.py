Python | Check whether a string is valid json or not



Given a string, the task is to check whether a string is valid json object or
not. Let’s try to understand the problem using different examples.

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# checking whether string

# is valid json or not

 

import json

 

ini_string = "{'akshat' : 1, 'nikhil' : 2}"

 

# printing initial ini_string

print ("initial string", ini_string)

 

# checking for string

try:

 json_object = json.loads(ini_string)

 print ("Is valid json? true")

except ValueError as e:

 print ("Is valid json? false")  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string {'akshat' : 1, 'nikhil' : 2}
    Is valid json? false
    

  
**Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# checking whether string

# is valid json or not

 

import json

 

#ini_string = '{"Geek" : 1,"forGeeks" : 2}'

 

a = '{"name":"John", "age":31, "Salary":25000}'

b = '{ "Subjects": {"Maths":85, "Physics":90}}'

 

#printing initial ini_string

print ("initial strings given - \n", a, "\n", b)

 

#checking for string

try:

 json_object1 = json.loads(a)

 json_object2 = json.loads(b)

 print ("Is valid json? true")

 

except ValueError as e:

 print ("Is valid json? false")  
  
---  
  
 __

 __

 **Output:**

    
    
    initial strings given - 
     {"name":"John", "age":31, "Salary":25000} 
     { "Subjects": {"Maths":85, "Physics":90}}
    Is valid json? true
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

