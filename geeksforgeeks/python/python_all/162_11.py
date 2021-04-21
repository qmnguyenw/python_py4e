Python Group by matching second tuple value in list of tuples



Given a list of tuples, the task is to group the tuples by matching the second
element in the tuples. We can achieve this using dictionary by checking the
second element in each tuple.

 **Examples:**

    
    
    **Input :** [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]
    **Output:** {80: [(20, 80), (31, 80)],
             11: [(88, 11), (27, 11)],
             22: [(1, 22)]}
    
    **Input :** [(20, 'Geek'), (31, 'Geek'), (88, 'NotGeek'), (27, 'NotGeek')]
    **Output:** {'NotGeek': [(88, 'NotGeek'), (27, 'NotGeek')],
             'Geek': [(20, 'Geek'), (31, 'Geek')]}
    
    

**Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to group tuples by matching

# second tuple value in list of tuples

 

# Initialisation 

Input = [(20, 80), (31, 80), (1, 22), (88,
11), (27, 11)]

 

Output = {}

for x, y in Input:

 if y in Output:

 Output[y].append((x, y))

 else:

 Output[y] = [(x, y)]

 

# Printing Output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    {80: [(20, 80), (31, 80)], 11: [(88, 11), (27, 11)], 22: [(1, 22)]}
    

