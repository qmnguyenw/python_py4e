Second largest value in a Python Dictionary



In this problem we will find the second largest value in the given Dictionary.  
 **Examples:**

    
    
    **Input :** {'one':5, 'two':1, 'three':6, 'four':10}
    **Output :** Second largest value of the dictionary is 6
    
    **Input :**  {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
    **Output :**  Second largest value of the dictionary is Geeks
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

dictionary= {1: 'Geeks', 'name': 'For', 3:
'Geeks'}

val = list(dictionary.values())

val.sort()

res = val[-2]

print(res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Geeks
    

Time Complexity : O(n Log n)

Please refer below post for more methods :

Python program to find second maximum value in Dictionary

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

