Python | Ways to join pair of elements in list



Given a list, the task is to join a pair of elements of the list. Given below
are a few methods to solve the given task.

 **Method #1: Usingzip() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to join pair of elements of list

 

# Initialising list

ini_list = ['a', 'b', 'c', 'd', 'e', 'f']

 

# Printing initial list 

print ("Initial list", str(ini_list))

 

# Pairing the elements of lists

res = [i + j for i, j in zip(ini_list[::2],
ini_list[1::2])]

 

# Printing final result

print ("Result", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial list ['a', 'b', 'c', 'd', 'e', 'f']
    Result ['ab', 'cd', 'ef']
    

  
**Method #2: Using list comprehension and next and iters**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to join pair of elements of list

 

# Initialising list

ini_list = iter(['a', 'b', 'c', 'd', 'e',
'f'])

 

# Pairing the elements of lists

res = [h + next(ini_list, '') for h in ini_list]

 

# Printing final result

print ("Result", str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Result ['ab', 'cd', 'ef']
    

