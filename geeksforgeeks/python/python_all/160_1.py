Python | Remove tuples from list of tuples if greater than n



Given a list of a tuple, the task is to remove all the tuples from list, if
it’s greater than _n_ (say 100). Let’s discuss a few methods for the same.

 **Method #1: Using lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove the tuples

# if certain criteria met

 

# initialising _list

ini_tuple = [('b', 100), ('c', 200), ('c', 45),

 ('d', 876), ('e', 75)]

 

# printing iniial_tuplelist

print("intial_list", str(ini_tuple))

 

# removing tuples for condition met

result = [i for i in ini_tuple if i[1] <= 100]

 

# printing resultant tuple list

print ("Resultant tuple list: ", str(result))

   
  
---  
  
__

__

**Output:**

> intial_list [(‘b’, 100), (‘c’, 200), (‘c’, 45), (‘d’, 876), (‘e’, 75)]  
> Resultant tuple list: [(‘b’, 100), (‘c’, 45), (‘e’, 75)]

  
**Method #2: Using filter + lambda**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove the tuples

# if certain criteria met

 

# initialising _list

ini_tuple = [('b', 100), ('c', 200), ('c', 45),

 ('d', 876), ('e', 75)]

 

# printing iniial_tuplelist

print("intial_list", str(ini_tuple))

 

# removing tuples for condition met

result = list(filter(lambda x: x[1] <= 100,
ini_tuple))

 

# printing resultant tuple list

print ("Resultant tuple list: ", str(result))  
  
---  
  
 __

 __

 **Output:**

> intial_list [(‘b’, 100), (‘c’, 200), (‘c’, 45), (‘d’, 876), (‘e’, 75)]  
> Resultant tuple list: [(‘b’, 100), (‘c’, 45), (‘e’, 75)]

  
**Method #3: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to remove the tuples

# if certain criteria met

 

# initialising _list

ini_tuple = [('b', 100), ('c', 200), ('c', 45), 

 ('d', 876), ('e', 75)]

 

# printing iniial_tuplelist

print("intial_list", str(ini_tuple))

 

# removing tuples for condition met

result = []

for i in ini_tuple:

 if i[1] <= 100:

 result.append(i)

 

# printing resultant tuple list

print ("Resultant tuple list: ", str(result))

   
  
---  
  
__

__

**Output:**

> intial_list [(‘b’, 100), (‘c’, 200), (‘c’, 45), (‘d’, 876), (‘e’, 75)]  
> Resultant tuple list: [(‘b’, 100), (‘c’, 45), (‘e’, 75)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

