Python | Get dictionary keys as a list



Given a dictionary, write a Python program to get the dictionary keys as a
list.

 **Examples:**

    
    
    **Input :** {1:'a', 2:'b', 3:'c'}
    **Output :** [1, 2, 3]
    
    **Input :** {'A' : 'ant', 'B' : 'ball'}
    **Output :** ['A', 'B']
    

**Approach #1 :** Using **dict.keys()** [For Python 2.x]

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get

# dictionary keys as list

 

def getList(dict):

 return dict.keys()

 

# Driver program

dict = {1:'Geeks', 2:'for', 3:'geeks'}

print(getList(dict))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [1, 2, 3]
    

