Python Program to find minimum number of rotations to obtain actual string



Given two strings s1 and s2. The task is to find out the minimum number of
string rotations for the given string s1 to obtain the actual string s2.

 **Examples:**

    
    
    **Input :** eeksg, geeks
    **Output:** 1 
    **Explanation:** g is rotated left to obtain geeks.
    
    **Input :** eksge, geeks
    **Output:** 2
    **Explanation :** e and g are left rotated to obtain geeks.
    

**Approach:**

  * Use string slicing to rotate the string.
  * Perform right rotations str1=str1[1:len(str1)]+str1[0] on string to obtain the actual string.
  * Perform left rotations m=m[len(m)-1]+m[:len(m)-1] on string to obtain the actual string.
  * Print the minimum of left(x) and right(y) rotations.

 **TIME COMPLEXITY:** O(n)

Below is the implementation:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

def findRotations(str1, str2):

 

 # To count left rotations 

 # of string

 x = 0

 

 # To count right rotations

 # of string

 y = 0

 m = str1

 

 while True:

 

 # left rotating the string

 m = m[len(m)-1] + m[:len(m)-1] 

 

 # checking if rotated and 

 # actual string are equal.

 if(m == str2):

 x += 1

 break

 

 else:

 x += 1

 if x > len(str2) :

 break

 

 while True:

 

 # right rotating the string

 str1 = str1[1:len(str1)]+str1[0] 

 

 # checking if rotated and actual

 # string are equal.

 if(str1 == str2):

 y += 1

 break

 

 else:

 y += 1

 if y > len(str2):

 break

 

 if x < len(str2):

 

 # printing the minimum

 # number of rotations.

 print(min(x,y))

 

 else:

 print("given strings are not of same kind")

 

# Driver code

findRotations('sgeek', 'geeks')  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

