Python | Ways to sort list of float values



Given a list of float values, write a Python program to sort the list.

 **Examples:**

    
    
    **Input:** list = ['1.2', '.8', '19.8', '2.7', '99.8', '80.7']
    **Output:** ['.8', '1.2', '2.7', '19.8', '80.7', '99.8']
    
    **Input:** list = [12.8, .178, 1.8, 782.7, 99.8, 8.7]
    **Output:** [0.178, 1.8, 8.7, 12.8, 99.8, 782.7]
    

Let’s discuss different ways to solve this problem.

 **Method #1 :Using lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort list of decimal values

 

# List initialization

Input = [12.8, .178, 1.8, 782.7, 99.8, 8.7]

 

# Using sorted and lambda

Output = sorted(Input, key = lambda x:float(x))

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [0.178, 1.8, 8.7, 12.8, 99.8, 782.7]
    

