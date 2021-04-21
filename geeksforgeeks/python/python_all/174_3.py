Python program to check if a string contains all unique characters



To implement an algorithm to determine if a string contains all unique
characters.  
Examples:

> **Input :** s = “abcd”  
> **Output:** True  
> “abcd” doesn’t contain any duplicates. Hence the output is True.
>
>  **Input :** s = “abbd”  
> **Output:** False  
> “abbd” contains duplicates. Hence the output is False.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

One solution is to create an array of boolean values, where the flag at the
index i indicates whether character i in the alphabet is contained in the
string. The second time you see this character you can immediately return
false.  
You can also return false if the string length exceeds the number of unique
characters in the alphabet.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

def isUniqueChars(st):

 # String length cannot be more than

 # 256.

 if len(st) > 256:

 return False

 # Initialize occurrences of all characters

 char_set = [False] * 128

 # For every character, check if it exists

 # in char_set

 for i in range(0, len(st)):

 # Find ASCII value and check if it

 # exists in set.

 val = ord(st[i])

 if char_set[val]:

 return False

 char_set[val] = True

 return True

# driver code

st = "abcd"

print(isUniqueChars(st))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True

