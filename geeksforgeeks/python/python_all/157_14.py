Python | Check if suffix matches with any string in given list



Given a list of strings, the task is to check whether suffix matches with any
string in the given list.

 **Examples:**

    
    
     **Input:** lst = ["Paras", "Geeksforgeeks", "Game"], str = 'Geeks'
    **Output:** True
    
    **Input:** lst = ["Geeks", "for", "forgeeks"], str = 'John'
    **Output:** False

Let’s discuss a few methods to do the task.  

**Method #1 : Usingany()**  
The most concise and readable way to check whether suffix exists in list of
strings is to use any().

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to check whether

# suffix exists in list of strings.

 

# Input list initialization

lst = ["Paras", "Geeksforgeeks", "Game"]

 

# using any to find suffix

Output = any('Geek' in x for x in lst)

 

# Printing output

print("Initial List is :", lst)

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial List is : ['Paras', 'Geeksforgeeks', 'Game']
    True
    

