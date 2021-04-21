Python | Split a list having single integer



Given a list containing single integer, the task is to split each value in the
list.

 **Examples:**

    
    
    **Input:** Input = [23]
    **Output:** Output  = [2, 3]
    
    **Input:** Input = [15478]
    **Output:** Output  = [1, 5, 4, 7, 8]
    

**Method #1 : Using Map**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split list containing single integer

 

# List initialization

input = [200]

 

# Using map

output = list(map(int, str(input[0])))

 

# Printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 0, 0]
    

  

  

**Method #2 : Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split list containing single integer

 

# List initialization

input = [231]

 

# Using list comprehension

output = [int(x) if x.isdigit() else x 

 for z in input for x in str(z)]

 

# Printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 3, 1]
    

  
**Method #3 : Using Loops**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split list containing single integer

 

# List initialization

input = [987]

 

# Converting to int

input = int(input[0])

 

# Output list initialization

output = []

 

while input>0:

 rem = input % 10

 input = int(input / 10)

 output.append(rem)

 

# Printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [7, 8, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

