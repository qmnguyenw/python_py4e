Python | Remove all duplicates and permutations in nested list



Given nested list, the task is to remove all duplicated and permutations in
that nested list.

    
    
     **Input:** [[-11, 0, 11], [-11, 11, 0], [-11, 0, 11], 
             [-11, 2, -11], [-11, 2, -11], [-11, -11, 2]]
    **Output:** {(-11, 0, 11), (-11, -11, 2)}
    
    **Input:** [[-1, 5, 3], [3, 5, 0], [-1, 5, 3], 
             [1, 3, 5], [-1, 3, 5], [5, -1, 3]]
    **Output:**  {(1, 3, 5), (0, 3, 5), (-1, 3, 5)}

  
**Code #1 :** Using Map

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all duplicates

# and permutations in nested list

 

#Initialisation

listOfPermut = [[-11, 0, 11], [-11, 11, 0],
[-11, 0, 11], 

 [-11, 2, -11], [-11, -11, 2], [2,
-11, -11]]

 

# Sorting tuple then removing

output = set(map(lambda x:
tuple(sorted(x)),listOfPermut))

 

# printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    {(-11, 0, 11), (-11, -11, 2)}
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all duplicates

# and permutations in nested list

 

#Initialisation

input = [[-11, 0, 11], [-11, 11, 0],
[-11, 2, -11],

 [-11, -11, 2], [2, -11, -11]]

 

# Sorting tuple then removing

output = set(tuple(sorted(x)) for x in input)

 

# printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    {(-11, 0, 11), (-11, -11, 2)}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

