Python | Ways to convert list of ASCII value to string



Given a list of ASCII values, write a Python program to convert those values
to their character and make a string. Given below are a few methods to solve
the problem.

 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of list of ascii values

# to string

 

# Initialising list

ini_list = [71, 101, 101, 107, 115, 102, 

 111, 114, 71, 101, 101, 107, 115] 

 

# Printing initial list

print ("Initial list", ini_list)

 

# Using Naive Method

res = ""

for val in ini_list:

 res = res + chr(val)

 

# Printing resultant string

print ("Resultant string", str(res))  
  
---  
  
 __

 __

 **Output:**

> Initial list [71, 101, 101, 107, 115, 102, 111, 114, 71, 101, 101, 107, 115]  
> Resultant string GeeksforGeeks

 **Method #2: Using map()**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of list of ascii values

# to string

 

# Initialising list

ini_list = [71, 101, 101, 107, 115, 102,

 111, 114, 71, 101, 101, 107, 115] 

 

# Printing initial list

print ("Initial list", ini_list)

 

# Using map and join

res = ''.join(map(chr, ini_list))

 

# Print the resultant string

print ("Resultant string", str(res))  
  
---  
  
 __

 __

 **Output:**

> Initial list [71, 101, 101, 107, 115, 102, 111, 114, 71, 101, 101, 107, 115]  
> Resultant string GeeksforGeeks

 **Method #3: Using join and list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# conversion of a list of ascii values

# to string

 

# Initialising list

ini_list = [71, 101, 101, 107, 115, 102,

 111, 114, 71, 101, 101, 107, 115] 

 

# Printing initial list

print ("Initial list", ini_list)

 

# Using list comprehension and join

res = ''.join(chr(val) for val in ini_list)

 

# Print the resultant string

print ("Resultant string", str(res))  
  
---  
  
 __

 __

 **Output:**

> Initial list [71, 101, 101, 107, 115, 102, 111, 114, 71, 101, 101, 107, 115]  
> Resultant string GeeksforGeeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

