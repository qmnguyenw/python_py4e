Python | Filter list of strings based on the substring list



Given two lists of strings _string_ and _substr_ , write a Python program to
filter out all the strings in _string_ that contains string in _substr_.

 **Examples:**

    
    
    **Input :** string = ['city1', 'class5', 'room2', 'city2']
            substr = ['class', 'city']
    **Output :** ['city1', 'class5', 'city2']
    
    **Input :** string = ['coordinates', 'xyCoord', '123abc']
            substr = ['abc', 'xy']
    **Output :** ['xyCoord', '123abc']
    

  
**Method #1 :** Using List comprehension

We can Use list comprehension along with _in_ operator to check if the string
in ‘substr’ is contained in ‘string’ or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Filter list of

# strings based on another list

import re

 

def Filter(string, substr):

 return [str for str in string if

 any(sub in str for sub in substr)]

 

# Driver code

string = ['city1', 'class5', 'room2', 'city2']

substr = ['class', 'city']

print(Filter(string, substr))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['city1', 'class5', 'city2']
    

