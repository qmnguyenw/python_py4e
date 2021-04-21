Python – Capitalize repeated characters in a string



Given an input string with lowercase letters, the task is to write a python
program to identify the repeated characters in the string and capitalize them.

 **Examples:**

>  **Input:** programming language
>
>  **Output:** pRoGRAMMiNG lANGuAGe
>
>  **Explanation:** r,m,n,a,g are repeated elements
>
>  
>
>
>  
>
>
>  **Input:** geeks for geeks
>
>  **Output:** GEEKS for GEEKS
>
>  **Expalanation:** g,e,k,s are repeated elements

 **Approach:**

  * We have to keep the character of a string as a key and the frequency of each character of the string as a value in the dictionary.
  * Traverse the string and check the frequency of each character using a dictionary if the frequency of the character is greater than one then change the character to the uppercase using the upper() function.

 **Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function for changing the

# repated characters to uppercase

def RepeatedUpper(s):

 

 # declaring dictionary

 dic = {}

 

 # Traversing the string

 for i in s:

 

 # If the character is already

 # present in dictionary then increment

 # the frequency of the character

 if i in dic:

 dic[i] = dic[i]+1

 

 # If the character is not present in

 # the dictionary then inserting

 # the character in the dictionary

 else:

 dic[i] = 1

 ans = ''

 

 # traversing the string

 for i in s:

 

 # if the frequency of the character is 

 # greater than one

 if dic[i] > 1:

 

 # change into uppercase

 i = i.upper()

 

 # appending each character to the ans

 ans = ans+i

 return ans

 

 

# Driver code

s = 'geeks for geeks'

# fuction call

print(RepeatedUpper(s))  
  
---  
  
 __

 __

 **Output:**

    
    
    GEEKS for GEEKS

 **Time Complexity:** O(n)

 **Space Complexity:** O(n)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

