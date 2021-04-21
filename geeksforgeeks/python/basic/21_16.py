Python reversed() function



 **reversed()** method returns an iterator that accesses the given sequence in
the reverse order.

 **Syntax :**

> reversed(sequ)

 **Parameters :**

>  **sequ :** Sequence to be reversed.
>
>  
>
>
>  
>

 **Returns :**

> returns an iterator that accesses the given sequence in the reverse order.

  
**CODE 1**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# reversed()

 

# For string

seqString = 'geeks'

print(list(reversed(seqString)))

 

# For tuple

seqTuple = ('g', 'e', 'e', 'k', 's')

print(list(reversed(seqTuple)))

 

# For range

seqRange = range(1, 5)

print(list(reversed(seqRange)))

 

# For list

seqList = [1, 2, 4, 3, 5]

print(list(reversed(seqList)))  
  
---  
  
 __

 __

Output :

    
    
    ['s', 'k', 'e', 'e', 'g']
    ['s', 'k', 'e', 'e', 'g']
    [4, 3, 2, 1]
    [5, 3, 4, 2, 1]
    

  
**CODE 2**

 __

 __  
 __

 __

 __  
 __  
 __

vowels= ['a', 'e', 'i', 'o', 'u']

 

# Function to reverse the list

def __reversed__(self):

 return reversed(self.vowels)

 

# Main Function 

if __name__ == '__main__':

 print(list(reversed(vowels)))  
  
---  
  
 __

 __

Output :

    
    
    ['u', 'o', 'i', 'e', 'a']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

