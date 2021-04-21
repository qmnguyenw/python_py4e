Python | Ways to format elements of given list



Given a List of float values, the task is to truncate all float values to
2-decimal digit. Let’s see the different methods to do the task.

 **Method #1 : Using List comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to truncate float

# values to 2-decimal digits.

 

# List initialization

Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

 

# Using list comprehension

Output = ["%.2f" % elem for elem in Input]

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['100.77', '17.23', '60.99', '300.84']
    

  
**Method #2 : Using Map**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to truncate float

# values to 2 decimal digits.

 

# List initialization

Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

 

# Using map

Output = map(lambda n: "%.2f" % n, Input)

 

# Converting to list

Output = list(Output)

 

# Print output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['100.77', '17.23', '60.99', '300.84']
    

