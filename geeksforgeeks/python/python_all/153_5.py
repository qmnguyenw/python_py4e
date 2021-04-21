Python | Sort given list of strings by part of string



Given a list of string, the task is to sort the list by part of the string
which is separated by some character. In this scenario, we are considering the
string to be separated by space, which means it has to be sorted by second
part of each string.

Given below are a few methods to solve the given task.

 **Method #1: Using _sort_**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate to sort list

# containing string by part of string

 

# Initialising list

ini_list = ["GeeksForGeeks abc", "manjeet xab", "akshat
bac"]

 

# printing initial list

print ("initial list", str(ini_list))

 

# code to sort list

ini_list.sort(key = lambda x: x.split()[1])

 

# printing result

print ("result", str(ini_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list ['GeeksForGeeks abc', 'manjeet xab', 'akshat bac']
    result ['GeeksForGeeks abc', 'akshat bac', 'manjeet xab']
    

  
**Method #2: Using _sorted_**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate to sort list

# containing string by part of string

 

# Initialising list

ini_list = ["GeeksForGeeks abc", "manjeet xab", "akshat
bac"]

 

# printing initial list

print ("initial list", str(ini_list))

 

# code to sort list

res = sorted(ini_list, key = lambda x: x.split()[1])

 

# printing result

print ("result", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list ['GeeksForGeeks abc', 'manjeet xab', 'akshat bac']
    result ['GeeksForGeeks abc', 'akshat bac', 'manjeet xab']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

