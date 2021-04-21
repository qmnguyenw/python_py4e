Python | Replace multiple occurrence of character by single



Given a string and a character, write a Python program to replace multiple
occurrences of the given character by a single character.

 **Examples:**

    
    
    **Input :** Geeksforgeeks, ch = 'e'
    **Output :** Geksforgeks
    
    **Input :** Wiiiin, ch = 'i'
    **Output :** Win
    

**Approach #1 :** Naive Approach  
This method is a brute force approach in which we take another list ‘new_str’.
Use a for loop to check if the given character is repeated or not. If repeated
multiple times, append the character single time to the list. Other
characters(Not the given character) are simply appended to the list without
any alteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to replace multiple

# occurrences of a character by a single character

 

def replace(s, ch):

 new_str = []

 l = len(s)

 

 for i in range(len(s)):

 if (s[i] == ch and i != (l-1) and

 i != 0 and s[i + 1] != ch and s[i-1] !=
ch):

 new_str.append(s[i])

 

 elif s[i] == ch:

 if ((i != (l-1) and s[i + 1] == ch) and

 (i != 0 and s[i-1] != ch)):

 new_str.append(s[i])

 

 else:

 new_str.append(s[i])

 

 return ("".join(i for i in new_str))

 

 

# Driver code 

s = 'Geeksforgeeks'

char = 'e'

print(replace(s, char))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Geksforgeks
    

