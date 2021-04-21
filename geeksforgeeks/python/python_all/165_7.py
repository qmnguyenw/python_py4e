Python | Remove all strings from a list of tuples



Given a list of tuples, containing both integer and strings, the task is to
remove all strings from list of tuples.

 **Examples:**

    
    
    **Input :** [(1, 'Paras'), (2, 'Jain'), (3, 'GFG'), (4, 'Cyware')]
    **Output :**  [(1), (2), (3), (4)]
    
    **Input :** [('string', 'Geeks'), (2, 225), (3, '111')]
    **Output :** [(), (2, 225), (3,)]
    

  
**Method #1:** Using filter() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all strings from a list of tuples

 

# Check function to check isinstance

def check(x):

 return not isinstance(x, str)

 

# creating list of tuples

listOfTuples = [('string', 'Paras'), (2, 'Jain'), (3,
'GFG'),

 (4, 'Cyware'), (5, 'Noida')] 

 

# using filter 

output = ([tuple(filter(check, x)) for x in
listOfTuples])

 

# printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [(), (2,), (3,), (4,), (5,)]
    

  
**Method #2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all strings from a list of tuples

 

# Creating list of tuples

listOfTuples = [('string', 'Geeks'), (2, 225), (3,
'111'),

 (4, 'Cyware'), (5, 'Noida')] 

 

 

output = [tuple(j for j in i if not isinstance(j,
str))

 for i in listOfTuples]

 

# printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    [(), (2, 225), (3,), (4,), (5,)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

