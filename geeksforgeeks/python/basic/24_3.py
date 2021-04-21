Second most repeated word in a sequence in Python



Given a sequence of strings, the task is to find out the second most repeated
(or frequent) string in the given sequence. (Considering no two words are the
second most repeated, there will be always a single word).

Examples:

    
    
    Input : {"aaa", "bbb", "ccc", "bbb", 
             "aaa", "aaa"}
    Output : bbb
    
    Input : {"geeks", "for", "geeks", "for", 
              "geeks", "aaa"}
    Output : for
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Second most repeated word in a
sequence link. We can solve this problem quickly in Python using
Counter(iterator) method.

Approach is very simple –

  

  

  1. Create a dictionary using **Counter(iterator)** method which contains words as keys and it’s frequency as value.
  2. Now get a list of all values in dictionary and sort it in descending order. Choose second element from the sorted list because it will be the second largest.
  3. Now traverse dictionary again and print key whose value is equal to second largest element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to print Second most repeated

# word in a sequence in Python 

from collections import Counter 

 

def secondFrequent(input): 

 

 # Convert given list into dictionary 

 # it's output will be like {'ccc':1,'aaa':3,'bbb':2} 

 dict = Counter(input) 

 

 # Get the list of all values and sort it in ascending order 

 value = sorted(dict.values(), reverse=True) 

 

 # Pick second largest element 

 secondLarge = value[1] 

 

 # Traverse dictionary and print key whose 

 # value is equal to second large element 

 for (key, val) in dict.items(): 

 if val == secondLarge: 

 print (key) 

 return

 

# Driver program 

if __name__ == "__main__": 

 input = ['aaa','bbb','ccc','bbb','aaa','aaa']


 secondFrequent(input)  
  
---  
  
 __

 __

 **Output:**

    
    
    bbb
    

**  
Alternate Implementation :**

 __

 __  
 __

 __

 __  
 __  
 __

# Second most repeated word in a sequence in Python

 

def secondFrequent(input):

 from collections import Counter

 

 # this sorts from most common to least common to least common

 c = Counter(input) 

 

 # c.most_common()[1] prints ('bbb',2) 

 # c.most_common()[1][0] prints output: bbb

 print(c.most_common()[1][0])

 

# Driver code

input = ['aaa','bbb','ccc','bbb','aaa','aaa']

secondFrequent(input)  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

