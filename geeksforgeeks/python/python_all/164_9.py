Python | Convert a list into tuple of lists



We are given a list, the task is to convert the list into tuple of lists.

    
    
     **Input:** ['Geeks', 'For', 'geeks']
    **Output:** (['Geeks'], ['For'], ['geeks'])
    
    **Input:** ['first', 'second', 'third']
    **Output:** (['first'], ['second'], ['third'])
    

  
**Method #1 :** Using Comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert a list into tuple of lists

 

# Initialisation of list

Input = ['Geeks', 'for', 'geeks']

 

# Using list Comprehension

Output = tuple([name] for name in Input)

 

# printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    (['Geeks'], ['for'], ['geeks'])
    

  
**Method #2 :** Using Map + Lambda

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert a list into tuple of lists

 

# Initialisation of list

Input = ['first', 'second', 'third']

 

# Using map + lambda

Output = tuple(map(lambda x: [x], Input))

 

# printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    (['first'], ['second'], ['third'])
    

