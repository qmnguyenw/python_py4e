Python | Find all possible substrings after deleting k characters



Given a string and an Integer k, write a Python program to find all possible
substrings of the given string after deleting k characters.

 **Examples:**

    
    
    **Input :** geeks, k = 1
    **Output :** {'gees', 'eeks', 'geks', 'geek'}
    
    **Input :** dog, k = 1
    **Output :** {'do', 'dg', 'og'}
    

  
**Approach #1 :** Naive Approach  
This is the recursive naive approach to find all possible substrings after
deleting k characters. First, we initialize _start, end_ and index variable
with 0, length of string and 0 respectively. We create a temporary list, say ‘
_temp_ ‘ which stores all outputs one by one. We start from first index in
temp[], one by one fix elements at this index and recur for remaining
indexes.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find all combinations

# of string after deleting k characters

list = []

 

def findCombinations(str, temp, start, end, index, k): 

 

 if (index == k): 

 item = ''

 

 for j in range(k): 

 item += temp[j]

 list.append(item)

 return; 

 

 i = start; 

 while(i <= end and end - i + 1 >= k - index):


 temp[index] = str[i]

 findCombinations(str, temp, i + 1, 

 end, index + 1, k); 

 i += 1; 

 

# Driver Code

str = 'geeks'

k = 1

temp = [0]*(len(str)-k)

s, e = 0, len(str)-1

 

findCombinations(str, temp, s, e, 0, len(str)-k)

print(set(list))  
  
---  
  
 __

 __

 **Output:**

    
    
    {'eeks', 'gees', 'geks', 'geek'}
    

  
**Approach #2 :** Using Itertools  
The Python module Itertools gives a function combination(), which takes the
string and length to give all possible combinations of a string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find all combinations

# of string after deleting k characters

from itertools import combinations

 

def findCombinations(str, k):

 l = len(str)

 return set([''.join(i) for i in combinations(str, l -
k)])

 

# Driver Code

str = 'geeks'

k = 1

print(findCombinations(str, k))  
  
---  
  
 __

 __

 **Output:**

    
    
    {'geek', 'eeks', 'geks', 'gees'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

