Generate a list using given frequency list



Given a list, the task is to generate another list containing numbers from _0
to n_ , from given list whose each element is frequency of numbers in the
generated list.

    
    
     **Input:** freq = [1, 4, 3, 5]
    **Output:** [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
    
    **Explanation:**
    Number = 0
    Input[0] = 1 Output = [0]
    
    Number =1
    Input[1] = 4 Output = [0, 1, 1, 1, 1] (repeats 1 four times)
    
    Number =2
    Input[2] = 3  Output = [0, 1, 1, 1, 1, 2, 2, 2] (repeats 2 three times)
    
    Number =3
    Input[3] = 5  Output = [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3] (repeats 3 five times)
    

Below are some ways to achieve above task.

 **Method #1 : Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to generate list containing numbers from 0 to 'n'

# having frequency of no from another list

 

# List initialisation

Input = [1, 4, 3, 5]

Output = []

 

# Number initialisation

no = 0

 

# using iteration

for rep in Input:

 for elem in range(rep):

 Output.append(no)

 no += 1

 

# printing output

print(Output)   
  
---  
  
__

__

**Output:**

    
    
    [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
    

  
**Method #2 : Using enumerate and list comprehension**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to generate list containing numbers from 0 to 'n'

# having frequency of no from another list

 

# List initialisation

Input = [1, 4, 3, 5]

 

# Using enumerate and list comprehension

Output = [no for no, rep in enumerate(Input)

 for elem in range(rep)]

 

# Printing output

print(Output)   
  
---  
  
__

__

**Output:**

    
    
    [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
    

  
**Method #3 : Using enumerate and chain**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to generate list containing numbers from 0 to 'n'

# having frequency of no from another list

 

# List initialisation

Input = [1, 4, 3, 5]

 

# Importing

from itertools import repeat, chain

 

# Using chain and enumerate

Output = list(chain.from_iterable((repeat(x, y))

 for x, y in enumerate(Input)))

 

# Printing output

print(Output)   
  
---  
  
__

__

**Output:**

    
    
    [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

