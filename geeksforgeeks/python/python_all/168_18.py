Python program to check if given string is vowel Palindrome



Given a string (may contain both vowel and consonant letters), remove all
consonants, then check if the resulting string is palindrome or not.

 **Examples:**

    
    
    **Input :**  abcuhuvmnba
    **Output :** YES
    **Explanation :**
    The consonants in the string "a **bc** u **h** u **vmnb** a"
    are removed. Now the string becomes " **auua** ".
    
    **Input :** xayzuezyax
    **Output :** NO
    
    **Input :** bkldhgcj
    **Output :** -1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
Remove all the consonants in the string. Check if the vowel string is a
palindrome. If it is a palindrome print YES, else print NO. If string contains
no vowels, then print -1.

Below is the Python implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if given

# string is vowel Palindrome

 

# Function to check if a given string is a vowel

def vowel(c):

 

 # creating a list of vowels

 v = list("aeiou")

 

 # if the character is a vowel return True

 if c in v: return True

 return False

 

# Function to check if a vowel

# string is palindrome

def palindrome(s):

 

 # create a empty list

 v = []

 

 # append all vowels into the list

 for i in s:

 if vowel(i):v.append(i)

 

 # if the length of the vowel

 # string is 0 then print -1

 if len(v)== 0: print("-1")

 

 # else check if it is a palindrome

 else:

 # create a reversed string

 x = v[::-1]

 

 # initialize a flag

 f = 1

 for i in range(len(x)):

 

 # if the characters are not the same 

 if x[i]!= v[i]:

 

 # set the flag to 0

 f = 0

 break

 

 if f == 1: print("YES")

 else: print("NO")

 

# Driver Code

s = 'abcuhuvmnba'

 

# calling the main function

palindrome(s.strip())  
  
---  
  
 __

 __

 **Output:**

    
    
    YES
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

