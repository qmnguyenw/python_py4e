Python | Find frequency of given character at every position in list of lists



Given a list of lists, the task is to find the frequency of a character at
every position of sub-list in list of lists.

    
    
     **Input :** lst = [['X', 'Y', 'X'], ['Z', 'Y', 'X'],
                   ['Y', 'Y', 'Y'], ['Z', 'Z', 'X'],
                   ['Y', 'Z', 'X']], character = 'X'
    
    **Output:** [0.2, 0.0, 0.8]

 **Explanation:**  
We have 3 elements in each sublist, we have to find position of ‘X’ at
position 0, 1 and 2. For Position **0** in all sublist we have –  
‘x’ in first sub list at zero position,  
‘z’ in second sub list at zero position,  
‘y’ in third sub list at zero position,  
‘z’ in fourth sub list at zero position and  
‘y’ in fifth sub list at zero position.

So, we have 1 occurrence of ‘x’ at position 1 in all sub list so, Occurrence =
1/5 = .2  
For Position **1** we don’t have any occurrence of ‘x’ in sub list so,
Occurrence = 0/5 = 0.  
For Position **2** we have 4 occurrence of ‘x’ in sub list so, Occurrence =
4/5 = 0.8

  
Let’s discuss certain ways in which this can be performed.

 **Method #1 : Using Iteration**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find frequency of a character

# at every position of list in list of lists.

 

# Input list initialization

Input = [['X', 'Y', 'X'], ['Z', 'Y', 'X'],

 ['Y', 'Y', 'Y'], ['Z', 'Z', 'X'],

 ['Y', 'Z', 'X']]

Output = []

 

# Character Initialization

character = 'X'

 

# Output list initialization

for elem in range(len(Input[0])):

 Output.append(0)

 

# Using iteration

for elem in Input:

 for x, y in enumerate(elem):

 if y == character:

 Output[x]+= 1

for x, y in enumerate(Output):

 Output[x] = y / len(Input)

 

# Printing

print("Initial list of list is :", Input)

print("Occurrence of 'X' in list is", Output)  
  
---  
  
 __

 __

 **Output:**

> Initial list of list is : [[‘X’, ‘Y’, ‘X’], [‘Z’, ‘Y’, ‘X’], [‘Y’, ‘Y’,
> ‘Y’], [‘Z’, ‘Z’, ‘X’], [‘Y’, ‘Z’, ‘X’]]  
> Occurrence of ‘X’ in list is [0.2, 0.0, 0.8]

  
**Method #2 : Using zip**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find frequency of a character

# at every position of list in list of lists.

 

# Input list initialization

Input = [['X', 'Y', 'X'], ['Z', 'Y', 'X'],

 ['Y', 'Y', 'Y'], ['Z', 'Z', 'X'],

 ['Y', 'Z', 'X']]

 

Output = []

 

# Character initialization

character = 'X'

 

# Using zip

Output = [elem.count(character)/len(elem)

 for elem in zip(*Input)]

 

# Printing

print("Initial list of list is :", Input)

print("Occurrence of 'X' in list is", Output)  
  
---  
  
 __

 __

 **Output:**

> Initial list of list is : [[‘X’, ‘Y’, ‘X’], [‘Z’, ‘Y’, ‘X’], [‘Y’, ‘Y’,
> ‘Y’], [‘Z’, ‘Z’, ‘X’], [‘Y’, ‘Z’, ‘X’]]  
> Occurrence of ‘X’ in list is [0.2, 0.0, 0.8]

  
**Method #3: Using Pandas**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find frequency of a character

# at every position of list in list of lists.

 

import pandas as pd

 

# Input list initialization

Input = [['X', 'Y', 'X'],

 ['Z', 'Y', 'X'],

 ['Y', 'Y', 'Y'],

 ['Z', 'Z', 'X'],

 ['Y', 'Z', 'X']]

 

# Defining character

character = 'X'

 

# using pandas

Output = pd.DataFrame(Input)

Output = Output.where(Output == character, 0).where(Output
!= character, 1)

 

# Printing

print("Initial list of list is :", Input)

print("Occurrence of 'X' in list is\n", Output.mean())  
  
---  
  
 __

 __

 **Output:**

> Initial list of list is : [[‘X’, ‘Y’, ‘X’], [‘Z’, ‘Y’, ‘X’], [‘Y’, ‘Y’,
> ‘Y’], [‘Z’, ‘Z’, ‘X’], [‘Y’, ‘Z’, ‘X’]]  
> Occurrence of ‘X’ in list is  
> 0 0.2  
> 1 0.0  
> 2 0.8  
> dtype: float64

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

