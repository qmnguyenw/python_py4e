Python | Initialize tuples with parameters



This article deals with initializing the tuples with parameters. Namely,
default value, size, and specific value at specific index. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingtuple() \+ * operator**  
This task can be performed using combination of above functionalities. In
this, we extend the default values using * operator and perform the formation
of tuple using tuple()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize tuples with parameters

# Using tuple() + * operator

 

# Initializing size 

N = 6

 

# Initializing default value 

def_val = 2

 

# Initializing index to add value 

idx = 3

 

# Initializing value to be added 

val = 9

 

# Initialize tuples with parameters

# Using tuple() + * operator

res = [def_val] * N

res[idx] = val 

res = tuple(res)

 

# printing result

print("The formulated tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The formulated tuple is : (2, 2, 2, 9, 2, 2)
    

**Method #2 : Using generator expression +tuple()**  
This task can be performed using generator expression along with tuple() as
well. The elements are created one by one on this and specific element is
initialized at specific position using comparison.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize tuples with parameters

# Using tuple() + generator expression

 

# Initializing size 

N = 6

 

# Initializing default value 

def_val = 2

 

# Initializing index to add value 

idx = 3

 

# Initializing value to be added 

val = 9

 

# Initialize tuples with parameters

# Using tuple() + generator expression

res = tuple(val if i == idx else def_val for i in
range(N))

 

# printing result

print("The formulated tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The formulated tuple is : (2, 2, 2, 9, 2, 2)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

