Python | Ways to split a string in different ways



The most common problem we have encountered in Python is splitting a string by
a delimeter, But in some cases we have to split in different ways to get the
answer. In this article, we will get substrings obtained by splitting string
in different ways.

 **Examples:**

>  **Input :** Paras_Jain_Moengage_best  
>  **Output :** [‘Paras’, ‘Paras_Jain’, ‘Paras_Jain_Moengage’,
> ‘Paras_Jain_Moengage_best’]
>
>  **Input :** chunky_2808_GFG_Codechef  
>  **Output :** [‘chunky’, ‘chunky_2808’, ‘chunky_2808_GFG’,
> ‘chunky_2808_GFG_Codechef’]

Below are some ways to do the task.

  

  

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split string in substring manner

 

# Input initialisation

Input = "Geeks_for_geeks_is_best"

 

# Split initialise

split_string = Input.split('_')

 

# Output list initialise

Output = []

 

# Iteration

for a in range(len(split_string)):

 temp = split_string[:a + 1]

 temp = "_".join(temp)

 Output.append(temp)

 

# print output

print(Output)  
  
---  
  
 __

 __

 **Output:**

> [‘Geeks’, ‘Geeks_for’, ‘Geeks_for_geeks’, ‘Geeks_for_geeks_is’,
> ‘Geeks_for_geeks_is_best’]

 **Method 2: Using Itertools**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split string in substring manner

 

# Importing 

from itertools import accumulate

 

# Input initialisation

Input = "Geeks_for_geeks_is_best"

 

# Using accumulate

Output = [*accumulate(Input.split('_'), lambda temp1,
temp2 :

 '_'.join([temp1, temp2])), ]

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

> [‘Geeks’, ‘Geeks_for’, ‘Geeks_for_geeks’, ‘Geeks_for_geeks_is’,
> ‘Geeks_for_geeks_is_best’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

