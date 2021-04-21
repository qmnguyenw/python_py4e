Python | Convert list into list of lists



Given a list of strings, write a Python program to convert each element of the
given list into a sublist. Thus, converting the whole list into a list of
lists.

 **Examples:**

    
    
    **Input :** ['alice', 'bob', 'cara']
    **Output :** [['alice'], ['bob'], ['cara']]
    
    **Input :** [101, 202, 303, 404, 505] 
    **Output :** [[101], [202], [303], [404], [505]]
    

  
**Approach #1 :** Naive Approach

Use another list ‘res’ and a for a loop. Using _split()_ method of Python we
extract each element from the list in the form of the list itself and append
it to ‘res’. Finally, return ‘res’. One drawback of this method is that it
does not work with integer list as ‘int’ object has no attribute ‘split’.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to convert

# list into a list of lists

 

def extractDigits(lst):

 res = []

 for el in lst:

 sub = el.split(', ')

 res.append(sub)

 

 return(res)

 

# Driver code

lst = ['alice', 'bob', 'cara']

print(extractDigits(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [['alice'], ['bob'], ['cara']]
    

