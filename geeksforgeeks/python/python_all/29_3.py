Python program to find Indices of Overlapping Substrings



To count the number of overlapping sub strings in Python we can use the Re
module. To get the indices we will use the re.finditer() method. But it
returns the count of non-overlapping indices only.

 **Examples:**

>  **Input:** String: “geeksforgeeksforgeeks” ; Pattern: “geeksforgeeks”  
>  **Output:** [0, 8]  
>  **Explanation:** The pattern is overlapping the string from 0th index to
> 12th index and again overlapping it from 8th index to 20th index. Hence, the
> output is the starting positions of overlapping i.e index 0 and index 8.
>
> **Input:** String: “barfoobarfoobarfoobarfoobarfoo” ; Pattern: “foobarfoo”  
>  **Output:** [3, 9,15, 21]  
>  **Explanation:** The pattern is overlapping the string from index 3, 9 , 15
> and 21.

This method returns the count of non-overlapping indices only from a string
having multiple occurrences overlapping pattern. Below is a program depicting
the use of _finditer()_ method.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required module

import re

 

 

# Function to depict use of finditer() method

def CntSubstr(pattern, string):

 

 # Array storing the indices

 a = [m.start() for m in re.finditer(pattern, string)]

 return a

 

 

# Driver Code

string = 'geeksforgeeksforgeeks'

pattern = 'geeksforgeeks'

 

# Printing index values of non-overlapping pattern

print(CntSubstr(pattern, string))  
  
---  
  
 __

 __

 **Output:**

    
    
    [0]
    

Therefore, to get the overlapping indices as well we need to do is escape out
of the regular expressions in the pattern. The definition in the explicit
function helps to select the characters in a partial way.

 **Approach:**

  1.  _re.finditer()_ helps in finding the indices where the match object occurs. As it returns an iterable object, the _start()_ method helps in return the indices or else it would show that a match object has been found at some location.
  2. The standard method in matching using re module is greedy which means the maximum number of characters are matched. Therefore, the _?={0}_ helps in minimum number of matches.
  3. To match it so that partial characters are matched, the re.escape() helps in escaping out the special characters which have been added before such as the _?={0}_.
  4. The result is that by adding som modifications, the _finditer()_ method returns a list of overlapping indices.

 **Below is the implementation of the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required module

import re

 

 

# Explicit function to Count

# Indices of Overlapping Substrings

def CntSubstr(pattern, string):

 a = [m.start() for m in re.finditer(

 '(?={0})'.format(re.escape(pattern)), string)]

 return a

 

 

# Driver Code

string1 = 'geeksforgeeksforgeeks'

pattern1 = 'geeksforgeeks'

 

string2 = 'barfoobarfoobarfoobarfoobarfoo'

pattern2 = 'foobarfoo'

 

 

# Calling the function

print(CntSubstr(pattern1, string1))

print(CntSubstr(pattern2, string2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 8]
    [3, 9, 15, 21]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

