Python | Count tuples occurrence in list of tuples



Many a time while developing web and desktop product in Python, we use nested
lists and have several queries about how to find count of unique tuples. Let’s
see how to get count of unique tuples in given list of tuples.

Below are some ways to achieve the above task.

 **Method #1:** Using Iteration

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count unique

# tuples in list of list

 

import collections 

Output = collections.defaultdict(int)

 

# List initialization

Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],

 [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]

 

# Using iteration

for elem in Input:

 Output[elem[0]] += 1

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    defaultdict(<class 'int'>, {('Geeks', 'forGeeks'): 1, ('hi', 'bye'): 2, ('a', 'b'): 2})
    

  

  

**Method #2: Usingchain and Counter**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count unique

# tuples in list of list

 

# Importing

from collections import Counter

from itertools import chain

 

# List initialization

Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],

 [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]

 

# Using counter and chain

Output = Counter(chain(*Input))

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    Counter({('hi', 'bye'): 2, ('a', 'b'): 2, ('Geeks', 'forGeeks'): 1})
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

