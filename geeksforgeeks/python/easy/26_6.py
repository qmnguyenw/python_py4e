Using Counter() in Python to find minimum character removal to make two
strings anagram



Given two strings in lowercase, the task is to make them Anagram. The only
allowed operation is to remove a character from any string. Find minimum
number of characters to be deleted to make both the strings anagram?  
If two strings contains same data set in any order then strings are called
**Anagrams**.

Examples:

    
    
    Input : str1 = "bcadeh" str2 = "hea"
    Output: 3
    We need to remove b, c and d from str1.
    
    Input : str1 = "cddgk" str2 = "gcd"
    Output: 2
    
    Input : str1 = "bca" str2 = "acb"
    Output: 0
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Remove minimum number of
characters so that two strings become anagram link. We will solve this problem
in python quickly using Counter() and Dictionary Data Structure and
**intersection** property of Set data structure. Approach is very simple,

  1. Convert each string into a dictionary data structure using **Counter(iterable)** method.
  2. Count number of keys in both dictionaries ( count1, count2) and count number of keys common in both dictionaries.
  3. If no common keys found that means we need to remove **count1 + count2** characters from both the strings.
  4. Else **(max(count1, count2) – countCommon)** will be the number of characters to be removed

 __

 __  
 __

 __

 __  
 __  
 __

# Function remove minimum number of characters so that

# two strings become anagram 

from collections import Counter 

def removeChars(str1, str2): 

 

 # make dictionaries from both strings 

 dict1 = Counter(str1) 

 dict2 = Counter(str2) 

 

 # extract keys from dict1 and dict2 

 keys1 = dict1.keys() 

 keys2 = dict2.keys() 

 

 # count number of keys in both lists of keys 

 count1 = len(keys1) 

 count2 = len(keys2) 

 

 # convert list of keys in set to find common keys 

 set1 = set(keys1) 

 commonKeys = len(set1.intersection(keys2)) 

 

 if (commonKeys == 0): 

 return count1 + count2 

 else: 

 return (max(count1, count2)-commonKeys) 

 

# Driver program 

if __name__ == "__main__": 

 str1 ='bcadeh'

 str2 ='hea'

 print (removeChars(str1, str2))   
  
---  
  
__

__

Output:

  

  

        
        
        3
        

**  
Alternate Solution :**

      1. Convert each string into a dictionary data structure using **Counter(iterable)** method.
      2. Find the common elements from both dictonary
      3. Add up the values from common dictionary in order to get the total number of common elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Function remove minimum number of characters so that

# two strings become anagram 

from collections import Counter 

def removeChars(a, b): 

 

 # make dictionaries from both strings 

 c1 = Counter(a) 

 c2 = Counter(b) 

 

 # finding the common elements from both dictonary 

 common = c1&c2; 

 value = 0

 

 # adding up the key from common dictionary in order 

 # to get the total number of common elements 

 for key in common: 

 value = value + common[key] 

 

 # returning the number of elements to be 

 # removed to form an anagram 

 return (len(a)-2*value+ len(b)) 

 

# Driver program 

if __name__ == "__main__": 

 str1 ='bcadeh'

 str2 ='hea'

 print (removeChars(str1, str2))   
  
---  
  
__

__

Output:

                
                
                3
                

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

