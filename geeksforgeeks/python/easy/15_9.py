Python program to check if given string is pangram



Given a string, write a Python program to check if that string is Pangram or
not. A pangram is a sentence containing every letter in the English Alphabet.

 **Examples:**

    
    
    **Input :** The quick brown fox jumps over the lazy dog
    **Output :** Yes
    
    **Input :** abcdefgxyz
    **Output :** No
    

We have already discussed the naive approach of pangram checking in this
article. Now, let’s discuss the Pythonic approaches to do the same.

 **Approach #1 :** Pythonic Naive  
This method uses a loop to check if each character of the string belongs to
the alphabet set or not.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# Check if the string is pangram

import string

 

def ispangram(str):

 alphabet = "abcdefghijklmnopqrstuvwxyz"

 for char in alphabet:

 if char not in str.lower():

 return False

 

 return True

 

# Driver code

string = 'the quick brown fox jumps over the lazy dog'

if(ispangram(string) == True):

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

  
**Approach #2 :** Using Python Set  
Convert the given string into set and then check if the alphabet set is
greater than or equal to it or not. If the string set is greater or equal,
print ‘Yes’ otherwise ‘No’.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# Check if the string is pangram

import string

 

alphabet = set(string.ascii_lowercase)

 

def ispangram(string):

 return set(string.lower()) >= alphabet

 

# Driver code

string = "The quick brown fox jumps over the lazy dog"

if(ispangram(string) == True):

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

  
**Approach #3 :** Alternative to set method  
This is another method that uses Python set to find if the string is Pangram
or not. We make set of lowercase alphabets and the given string. If set of
given string is subtracted from the set of alphabets, we get to know whether
the string is pangram or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# Check if the string is pangram

import string

 

alphabet = set(string.ascii_lowercase)

 

def ispangram(str):

 return not set(alphabet) - set(str)

 

# Driver code

string = 'the quick brown fox jumps over the lazy dog'

if(ispangram(string) == True):

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

  
**Approach #4 :** ASCII method  
Check if each character of the string lies between the ASCII range of
lowercase alphabets i.e. 96 to 122.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# Check if the string is pangram

import itertools

import string

 

alphabet = set(string.ascii_lowercase)

 

def ispangram(str):

 return sum(1 for i in set(str) if 96 <
ord(i) <= 122) == 26

 

# Driver code

string = 'the quick brown fox jumps over the lazy dog'

if(ispangram(string) == True):

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

