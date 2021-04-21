Python | Sort all sublists in given list of strings



Given a list of lists, the task is to sort each sublist in the given list of
strings.

 **Example:**

    
    
    **Input:**
    lst = [['Machine', 'London', 'Canada', 'France'],
           ['Spain', 'Munich'],
           ['Australia', 'Mandi']]
    
    **Output:**
    flist = [['Canada', 'France', 'London', 'Machine'],
             ['Munich', 'Spain'],
             ['Australia', 'Mandi']]
    

There are multiple ways to sort each list in alphabetical order.

 **Method #1 : Using map**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort all sublists

# in given list of strings

 

# List initialization

Input = [['Machine', 'London', 'Canada', 'France',
'Lanka'],

 ['Spain', 'Munich'],

 ['Australia', 'Mandi']]

 

# Using map for sorting

Output = list(map(sorted, Input))

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

> [[‘Canada’, ‘France’, ‘Lanka’, ‘London’, ‘Machine’], [‘Munich’, ‘Spain’],
> [‘Australia’, ‘Mandi’]]

