Python | Get the smallest window in a string containing all characters of
given pattern



Given two strings _str_ and _pattern_ , find the smallest substring in _str_
containing all characters of pattern efficiently.

 **Examples:**

    
    
    **Input :** str = 'geeksforgeeks' pattern = 'gks' 
    **Output :** geeks
    
    **Input :** str = 'new string' pattern = 'rg' 
    **Output :** ring
    

**Approach #1 :** Using Python _enumerate()_  
This method uses Python enumerate(). _need[k]_ store how many times we need
character _k_ and missing tells how many characters are still missing. In the
loop, first add the new character to the window. Then, if nothing is missing,
remove as much as possible from the window start and then update the result.

 __

 __  
 __

 __

 __  
 __  
 __

string= 'new string'

pattern = 'rg'

 

# let's find the index of r and g in String and the

# stor them in index list (index[]) 

index=[]

for x in range(len(pattern)):

 if pattern[x] in string:

 index.append(string.index(pattern[x]))

 

# sorting the r and g index's

index.sort()

 

# save first index in l

l = len(index)

low = int(index[0])

 

# save last index in h

high = int(index[l-1])

h = high +1

for i in range(low,h):

 print(string[i],end=" ")  
  
---  
  
 __

 __

 **Output:**

    
    
    ksf
    

  
**Approach #2 :** Using collections.defaultdict()  
This method make use of two defaultdicts ‘src’ and ‘dest’. A _defaultdict_
works exactly like a normal dict, but it is initialized with a function
(“default factory”) that takes no arguments. _source_ is empty while _target_
consist of pattern elements as keys and the count of occurrence as value. In
every iteration ‘i’, we check if the _i th_ element of _str_ is present in
_target_ dictionary or not and update _source_ dictionary accordingly.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Find the smallest

# window in a string containing all 

# characters of another string

from collections import defaultdict

import sys

def min_window(str, pattern):

 

 # Function to check validity of source and 

 # destination

 def isValid(i, j):

 for item in j:

 if item not in i or i[item] < j[item]:

 return False

 return True

 

 source = defaultdict(int)

 target = defaultdict(int)

 

 # Target consist pattern elements and 1 

 # as key:value pair

 for e in pattern:

 target[e] += 1

 

 # Minimum length for window 

 minLen = sys.maxsize

 n = len(str)

 ans, j = '', 0

 for i in range(n):

 

 # Update source for valid source - target pair

 while j < n and (isValid(source, target) == False):

 source[str[j]] += 1

 j += 1

 

 # Checking validity of source-target pair

 if isValid(source, target):

 if minLen > j-i + 1:

 minLen = j-i + 1

 ans = str[i:j]

 source[str[i]] -= 1

 return ans

 

# Driver Code

string = "geekforgeeks"

pattern = "gks"

print(min_window(string, pattern))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeks
    

  
**Approach #3 :** Dynamic approach  
In this method, we use a for loop and in every iteration, say i, we find the
shortest interval that ends in i and includes all letters in the pattern. This
can be done by taking two data structures in account i.e. ‘rpos’ and ‘rdict’.
rpos is a sorted list of positions where rightmost positions of characters of
pattern in str are kept and rdict is a dictionary mapping from a character to
the position. values of rdict is same as rpos.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Find the smallest

# window in a string containing all 

# characters of another string

from collections import Counter, defaultdict

 

def min_window(str, pattern):

 

 rdict, count = defaultdict(list), Counter(pattern)

 rpos, res = [], "" 

 

 # Loop only over c exist in pattern

 for i, c in filter(lambda x: x[1] in pattern,
enumerate(str)): 

 if len(rdict) == count: 

 

 # If reached limit, remove

 rpos.remove(rdict.pop(0))

 

 # Add to dict

 rdict[i].append(i)

 

 # Add to list

 rpos.append(i) 

 

 if (len(rpos) == len(pattern) and

 (res =="" or rpos[-1]-rpos[0]<len(res))):

 res = str[rpos[0]:rpos[-1]+1] 

 

 return res

 

# Driver Code

string = "geeksforgeeks"

pattern = "gks"

print(min_window(string, pattern))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

