Python | Sort a list of percentage



Given a list of percentage, write a Python program to sort the given list in
ascending order.

Let’s see different ways to do the task.

 **Code #1:** Chops ‘%’ in string and convert it into float.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort list of percentage

 

# List initialization

Input =['2.5 %', '6.4 %', '91.6 %', '11.5 %']

 

# removing % and converting to float

# then apply sort function

Input.sort(key = lambda x: float(x[:-1]))

 

# printing output

print(Input)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['2.5 %', '6.4 %', '11.5 %', '91.6 %']
    

  
**Code #2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort list of percentage

 

# List initialization

Input =['2.5 %', '6.4 %', '91.6 %', '11.5 %']

 

# Temporary list initialization

temp = []

 

# removing % sign

for key in Input:

 temp.append((key[:-1]))

 

# sorting list of float

temp = sorted(temp, key = float)

 

# Output list initialization

output = []

 

# Adding percentage sign

for key in temp:

 output.append(key + '%')

 

# printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['2.5 %', '6.4 %', '11.5 %', '91.6 %']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

