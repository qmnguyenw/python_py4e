Python | Reverse sign of each element in given list



Given a list of integers, write a Python program to reverse the sign of each
element in given list.

 **Examples:**

    
    
    **Input :** [-1, 2, 3, -4, 5, -6, -7]
    **Output :** [1, -2, -3, 4, -5, 6, 7]
    
    **Input :** [-5, 9, -23, -2, 7]
    **Output :** [5, -9, 23, 2, -7]
    

**Methods #1 :** List comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert positive

# list integers to negative and vice-versa

def Convert(lst):

 return [ -i for i in lst ]

 

# Driver code

lst = [-1, 2, 3, -4, 5, -6, -7]

print(Convert(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [1, -2, -3, 4, -5, 6, 7]
    

