Python | Convert list of tuples into list



Given a list of tuples, write a Python program to convert it into list.

 **Examples:**

    
    
    **Input:** [(11, 20), (13, 40), (55, 16)]
    **Output:** [11, 20, 13, 40, 55, 16]
    
    **Input:** [('Geeks', 2), ('For', 4), ('geek', '6')]
    **Output:** ['Geeks', 2, 'For', 4, 'geek', '6']
    

Below are methods to convert list of tuples into list.

 **Method #1 :** Using list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert list of tuples into list

 

# List of tuple initialization

lt = [('Geeks', 2), ('For', 4), ('geek', '6')]

 

# using list comprehension

out = [item for t in lt for item in t]

 

# printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['Geeks', 2, 'For', 4, 'geek', '6']
    

