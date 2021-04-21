Python | Convert 1D list to 2D list of variable length



Given a 1D list ‘lst’ and list of variable lengths ‘var_lst’, write a Python
program to convert the given 1D list to 2D list of given variable lengths.

 **Examples:**

    
    
    **Input :** lst = [1, 2, 3, 4, 5, 6]
            var_lst = [1, 2, 3]
    **Output :** [[1], [2, 3], [4, 5, 6]]
    
    **Input :** lst = ['a', 'b', 'c', 'd', 'e']
            var_lst = [3, 2]
    **Output :** [['a', 'b', 'c'], ['d', 'e']]
    

  
**Method #1 :** List slicing

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert 1D

# list to 2D list

from itertools import islice

 

def convert(lst, var_lst):

 idx = 0

 for var_len in var_lst:

 yield lst[idx : idx + var_len]

 idx += var_len

 

# Driver code

lst = [1, 2, 3, 4, 5, 6]

var_lst = [1, 2, 3]

print(list(convert(lst, var_lst)))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1], [2, 3], [4, 5, 6]]
    

  
**Method #2 :** Using _itertools.islice()_

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert 1D

# list to 2D list

from itertools import islice

 

def convert(lst, var_lst):

 it = iter(lst)

 return [list(islice(it, i)) for i in var_lst]

 

# Driver code

lst = [1, 2, 3, 4, 5, 6]

var_lst = [1, 2, 3]

print(convert(lst, var_lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1], [2, 3], [4, 5, 6]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

