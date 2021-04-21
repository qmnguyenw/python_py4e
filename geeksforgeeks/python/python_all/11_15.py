Python program to check a string for specific characters



Given a string ‘s’ and char array ‘arr’, the task is to write a python program
to check string s for characters in char array arr.

 **Examples:**

    
    
     **Input:** s = @geeksforgeeks%
           arr[] = {'o','e','%'}
    **Output:** [true,true,true]
    
    **Input:** s = $geek
           arr[] = {'@','e','a','$'} 
    **Output:** [false,true,false,true]

 **Method #1:** using in keyword \+ loop

Traverse through the char array and for each character in arr check if that
character is present in string s using in operator which returns a boolean
value (either True or false).

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation to check string

# for specific characters

 

# function to check string

def check(s, arr):

 result = []

 for i in arr:

 

 # for every character in char array

 # if it is present in string return true else false

 if i in s:

 result.append("True")

 else:

 result.append("False")

 return result

 

 

# Driver Code

s = "@geeksforgeeks123"

arr = ['e', 'r', '1', '7']

print(check(s, arr))  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    ['True', 'True', 'True', 'False']

