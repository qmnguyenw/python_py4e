Python | Combining values from dictionary of list



Given a dictionary of list values, the task is to combine every key-value pair
in every combination.

>  **Input :**  
>  {“Name” : [“Paras”, “Chunky”],  
> “Site” : [“Geeksforgeeks”, “Cyware”, “Google”] }
>
>  **Output:**  
>  [{‘Site’: ‘Geeksforgeeks’, ‘Name’: ‘Paras’}, {‘Site’: ‘Cyware’, ‘Name’:
> ‘Paras’},  
> {‘Site’: ‘Google’, ‘Name’: ‘Paras’}, {‘Site’: ‘Geeksforgeeks’, ‘Name’:
> ‘Chunky’},  
> {‘Site’: ‘Cyware’, ‘Name’: ‘Chunky’}, {‘Site’: ‘Google’, ‘Name’: ‘Chunky’}]

 **Method #1: Using itertools and sorting**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to combine every key value

# pair in every combinations

 

# List initialization

Input = {

"Bool" : ["True", "False"],

"Data" : ["Int", "Float", "Long Long"],

}

 

# Importing

import itertools as it

 

# Sorting input

sorted_Input = sorted(Input)

 

# Using product after sorting

Output = [dict(zip(sorted_Input, prod)) 

 for prod in it.product(*(Input[sorted_Input]

 for sorted_Input in sorted_Input))]

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

> [{‘Bool’: ‘True’, ‘Data’: ‘Int’}, {‘Bool’: ‘True’, ‘Data’: ‘Float’},
> {‘Bool’: ‘True’, ‘Data’: ‘Long Long’}, {‘Bool’: ‘False’, ‘Data’: ‘Int’},
> {‘Bool’: ‘False’, ‘Data’: ‘Float’}, {‘Bool’: ‘False’, ‘Data’: ‘Long Long’}]

