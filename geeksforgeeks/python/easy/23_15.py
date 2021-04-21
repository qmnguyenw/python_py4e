Python program for removing i-th character from a string



Given the string, we have to remove the ith indexed character from the string.

In any string, indexing always start from 0. Suppose we have a string geeks
then its indexing will be as –

    
    
    g e e k s
    0 1 2 3 4
    

**Examples :**

    
    
    Input : Geek
            i = 1
    Output : Gek 
    
    Input : Peter 
            i = 4
    Output : Pete
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach 1 :** From the given string, i-th indexed element has to be
removed. So, Split the string into two halves, before indexed character and
after indexed character. Return the merged string.

  

  

Below is the implementation of above approach :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for removing i-th

# indexed character from a string

 

# Removes character at index i

def remove(string, i): 

 

 # Characters before the i-th indexed

 # is stored in a variable a

 a = string[ : i] 

 

 # Characters after the nth indexed

 # is stored in a variable b

 b = string[i + 1: ]

 

 # Returning string after removing

 # nth indexed character.

 return a + b

 

# Driver Code

if __name__ == '__main__':

 

 string = "geeksFORgeeks"

 

 # Remove nth index element

 i = 5

 

 # Print the new string

 print(remove(string, i))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksORgeeks
    

**Approach 2 :** The idea is to use string replace in Python  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for removing i-th

# indexed character from a string

 

# Removes character at index i

def remove(string, i): 

 

 for j in range(len(string)):

 if j == i:

 string = string.replace(string[i], "", 1)

 return string

 

# Driver Code

if __name__ == '__main__':

 

 string = "geeksFORgeeks"

 

 # Remove nth index element

 i = 5

 

 # Print the new string

 print(remove(string, i))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksORgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

