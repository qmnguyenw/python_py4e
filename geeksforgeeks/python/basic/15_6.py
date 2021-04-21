Python | Convert a list into a tuple



Given a list, write a Python program to convert the given list into a tuple.

 **Examples:**

    
    
    **Input :** [1, 2, 3, 4]
    **Output :** (1, 2, 3, 4)
    
    **Input :** ['a', 'b', 'c']
    **Output :** ('a', 'b', 'c')
    

  
**Approach #1 :** Using tuple(list_name).

Typecasting to tuple can be done by simply using tuple(list_name).

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to convert a

# list into a tuple

def convert(list):

 return tuple(list)

 

# Driver function

list = [1, 2, 3, 4]

print(convert(list))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    (1, 2, 3, 4)
    

