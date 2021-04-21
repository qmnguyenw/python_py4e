Python | Count unique sublists within list



Given a list of lists, the task is to find the count of unique sublists within
list.

 **Examples:**

    
    
    **Input:** [['Geek', 'for', 'geeks'], ['geeks', 'for'],
            ['for', 'Geeks', 'geek'], ['Geek', 'for', 'geeks']]
    
    **Output:**
    {('geeks', 'for'): 1, ('for', 'Geeks', 'geek'): 1, 
     ('Geek', 'for', 'geeks'): 2}
    

Below are some ways to achieve the task.

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count unique sublist within list

 

# Input list initialization

Input = [['Geek', 'for', 'geeks'], ['geeks', 'for'],

 ['for', 'Geeks', 'geek'], ['Geek', 'for',
'geeks']]

 

# Output list initialization

Output = {}

 

# Using Iteration

for lis in Input:

 Output.setdefault(tuple(lis), list()).append(1)

for a, b in Output.items():

 Output[a] = sum(b)

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

> {(‘Geek’, ‘for’, ‘geeks’): 2, (‘geeks’, ‘for’): 1, (‘for’, ‘Geeks’, ‘geek’):
> 1}

