Python | Convert string enclosed list to list



Given a list enclosed within string (or quotes), write a Python program to
convert the given string to list type.

 **Examples:**

    
    
    **Input :** "[0, 2, 9, 4, 8]"
    **Output :** [0, 2, 9, 4, 8]
    
    **Input :** "['x', 'y', 'z']"
    **Output :** ['x', 'y', 'z']
    

  
**Approach #1 :** Python eval()

The eval() method parses the expression passed to this method and runs
python expression (code) within the program. Here it takes the list enclosed
within quotes as expression and runs it, and finally returns the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to ways to convert

# list enclosed within string to list

 

def convert(lst):

 return eval(lst)

 

# Driver code

lst = "[0, 2, 9, 4, 8]"

print(convert(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [0, 2, 9, 4, 8]
    

