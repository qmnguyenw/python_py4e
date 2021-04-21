Find length of a string in python (4 ways)



Strings in Python are **immutable** sequences of Unicode code points. Given a
string, we need to find its length.

Examples:

    
    
    Input : 'abc'
    Output : 3
    
    Input : 'hello world !'
    Output : 13
    
    Input : ' h e l   l  o '
    Output :14
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Methods:

  * Using the built-in function len. The built-in function len returns the number of items in a container.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate string length

# using len

 

str = "geeks"

print(len(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

  * Using for loop and in operator. A string can be iterated over, directly in a for loop. Maintaining a count of the number of iterations will result in the length of the string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate string length

# using for loop

 

# Returns length of string

def findLen(str):

 counter = 0

 for i in str:

 counter += 1

 return counter

 

 

str = "geeks"

print(findLen(str))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    5
    

