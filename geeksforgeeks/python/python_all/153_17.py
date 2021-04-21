Python | Remove tuples having duplicate first value from given list of tuples



Given a list of tuples, the task is to remove all tuples having duplicate
first values from the given list of tuples.

 **Examples:**

    
    
     **Input:** [(12.121, 'Tuple1'), (12.121, 'Tuple2'), 
             (12.121, 'Tuple3'), (923232.2323, 'Tuple4')]
    **Output:** [(12.121, 'Tuple1'), (923232.2323, 'Tuple4')]
    
    **Input:** [('Tuple1', 121), ('Tuple2', 125), 
             ('Tuple1', 135), ('Tuple4', 478)]
    **Output:** [('Tuple1', 121), ('Tuple2', 125), ('Tuple4', 478)]

Below are some ways to achieve the above task.

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove tuples having

# duplicate first value from given

# list of tuples

 

# Input list initialization

Input = [(12.121, 'Geeksforgeeks is best'), 

 (19212.22, 'India is best'), 

 (12.121, 'Cyware is best.'),

 (923232.2323, 'Jiit is best')]

 

# using set

visited = set()

 

# Output list initialization

Output = []

 

# Iteration

for a, b in Input:

 if not a in visited:

 visited.add(a)

 Output.append((a, b))

 

# Printing

print("Initial list of tuple is \n", Input)

print("List of tuple after removing duplicates:\n ", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

> Initial list of tuple is  
> [(12.121, ‘Geeksforgeeks is best’), (19212.22, ‘India is best’), (12.121,
> ‘Cyware is best.’), (923232.2323, ‘Jiit is best’)]
>
> List of tuple after removing duplicates:  
> [(12.121, ‘Geeksforgeeks is best’), (19212.22, ‘India is best’),
> (923232.2323, ‘Jiit is best’)]

