Python | Add only numeric values present in a list



Given a list containing characters and numbers, the task is to add only
numbers from a list. Given below are a few methods to complete a given task.  
  
 **Method #1: Usingfilter() and lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to add only numbers present

# in a list of characters and numbers

 

# initialising lists

ini_list = [1, 2, 3, 4, 'a', 'b', 'x', 5,
'z']

 

# printing initial list

print ("initial list", str(ini_list))

 

# code to add numbers from list

res = sum(filter(lambda i: isinstance(i, int),
ini_list))

 

# printing result

print ("resultant sum", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 2, 3, 4, 'a', 'b', 'x', 5, 'z']
    resultant sum 15
    

  
**Method #2: Using try and except**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to add only numbers present

# in a list of characters and numbers

 

# initialising lists

ini_list = [1, 2, 3, 4, 'a', 'b', 'x', 5,
'z']

 

# printing initial list

print ("initial list", str(ini_list))

 

# code to add numbers from list

res = 0

for item in ini_list:

 try:

 res+= int(item)

 except ValueError:

 pass

 

# printing result

print ("resultant sum", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 2, 3, 4, 'a', 'b', 'x', 5, 'z']
    resultant sum 15
    

  
**Method #3: Using isinstance and conditional statements**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to add only numbers present

# in a list of characters and numbers

 

# initialising lists

ini_list = [1, 2, 3, 4, 'a', 'b', 'x', 5,
'z']

 

# printing initial list

print ("initial list", str(ini_list))

 

# code to add numbers from list

res = sum([x for x in ini_list if isinstance(x,
int)])

 

# printing result

print ("resultant sum", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 2, 3, 4, 'a', 'b', 'x', 5, 'z']
    resultant sum 15
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

