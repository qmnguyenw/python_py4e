Python counter and dictionary intersection example (Make a string using
deletion and rearrangement)



Given two strings, find if we can make first string from second by deleting
some characters from second and rearranging remaining characters.

Examples:

    
    
    Input : s1 = ABHISHEKsinGH
          : s2 = gfhfBHkooIHnfndSHEKsiAnG
    Output : Possible
    
    Input : s1 = Hello
          : s2 = dnaKfhelddf
    Output : Not Possible
    
    Input : s1 = GeeksforGeeks
          : s2 = rteksfoGrdsskGeggehes
    Output : Possible
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Make a string from
another by deletion and rearrangement of characters link. We will this problem
quickly in python. Approach is very simple,

  1. Convert both string into dictionary using Counter(iterable) method, each dictionary contains characters within string as Key and their frequencies as Value.
  2. Now take intersection of two dictionaries and compare resultant output with dictionary of first string, if both are equal that means it is **possible** to convert string otherwise not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find if we can make first string

# from second by deleting some characters from 

# second and rearranging remaining characters.

from collections import Counter

 

def makeString(str1,str2):

 

 # convert both strings into dictionaries

 # output will be like str1="aabbcc", 

 # dict1={'a':2,'b':2,'c':2}

 # str2 = 'abbbcc', dict2={'a':1,'b':3,'c':2}

 dict1 = Counter(str1)

 dict2 = Counter(str2)

 

 # take intersection of two dictionries

 # output will be result = {'a':1,'b':2,'c':2}

 result = dict1 & dict2

 

 # compare resultant dictionary with first

 # dictionary comparison first compares keys

 # and then compares their corresponding values 

 return result == dict1

 

# Driver program

if __name__ == "__main__":

 str1 = 'ABHISHEKsinGH'

 str2 = 'gfhfBHkooIHnfndSHEKsiAnG'

 if (makeString(str1,str2)==True):

 print("Possible")

 else:

 print("Not Possible")  
  
---  
  
 __

 __

Output:

    
    
    Possible
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

