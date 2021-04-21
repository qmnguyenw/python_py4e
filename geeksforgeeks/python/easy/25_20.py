Python code to print common characters of two Strings in alphabetical order



Given two strings, print all the common characters in lexicographical order.
If there are no common letters, print -1. All letters are lower case.

Examples:

    
    
    Input : 
    string1 : geeks
    string2 : forgeeks
    Output : eegks
    Explanation: The letters that are common between 
    the two strings are e(2 times), k(1 time) and 
    s(1 time).
    Hence the lexicographical output is "eegks"
    
    Input : 
    string1 : hhhhhello
    string2 : gfghhmh
    Output : hhh
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Print common characters of two
Strings in alphabetical order link. We will solve this problem in python using
intersection property and collections.Counter() module. Approach is simple,

  1. Convert both strings into dictionary data type using **Counter(str)** method, which contains characters of string as key and their frequencies as value.
  2. Now find common elements between two strings using **intersection ( a &b; )** property.
  3. Resultant will also be an counter dictionary having common elements as keys and their common frequencies as value.
  4. Use **elements()** method of counter dictionary to expand list of keys by their frequency number of times.
  5. Sort the list and concatenate each character of output list without space to print resultant string.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to print common characters of two Strings

# in alphabetical order 

from collections import Counter 

 

def common(str1,str2): 

 

 # convert both strings into counter dictionary 

 dict1 = Counter(str1) 

 dict2 = Counter(str2) 

 

 # take intersection of these dictionaries 

 commonDict = dict1 & dict2 

 

 if len(commonDict) == 0: 

 print (-1)

 return

 

 # get a list of common elements 

 commonChars = list(commonDict.elements()) 

 

 # sort list in ascending order to print resultant 

 # string on alphabetical order 

 commonChars = sorted(commonChars) 

 

 # join characters without space to produce 

 # resultant string 

 print (''.join(commonChars)) 

 

# Driver program 

if __name__ == "__main__": 

 str1 = 'geeks'

 str2 = 'forgeeks'

 common(str1, str2)   
  
---  
  
__

__

Output:

    
    
    eegks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

