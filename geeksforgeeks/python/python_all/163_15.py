Python | Convert list of string into sorted list of integer



Given a list of string, write a Python program to convert it into sorted list
of integer.

 **Examples:**

    
    
     **Input:** ['21', '1', '131', '12', '15']
    **Output:** [1, 12, 15, 21, 131]
    
    **Input:** ['11', '1', '58', '15', '0']
    **Output:** [0, 1, 11, 15, 58]
    

  
Let’s discuss different methods we can achieve this task.

 **Method #1:** Using map and sorted()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert list of

# string into sorted list of integer

 

# List initialization

list_string = ['21', '1', '131', '12', '15']

 

# mapping

list_map = map(int, list_string)

 

# sorting list

list_sorted = sorted(list_map)

 

# Printing sorted list of integers

print(list_sorted)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [1, 12, 15, 21, 131]
    

