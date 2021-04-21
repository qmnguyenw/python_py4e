Python | re.search() vs re.match()



 **Prerequisite:** Regex in Python  
 **Use of re.search() and re.match() –**  
**re.search()** and **re.match()** both are functions of re module in python.
These functions are very efficient and fast for searching in strings. The
function searches for some substring in a string and returns a match object if
found, else it returns none.  
 **re.search() vs re.match() –**  
There is a difference between the use of both functions. Both return the first
match of a substring found in the string, but **re.match()** searches only
from the beginning of the string and return match object if found. But if a
match of substring is found somewhere in the middle of the string, it returns
none.  
While **re.search()** searches for the whole string even if the string
contains multi-lines and tries to find a match of the substring in all the
lines of string.  
 **Example :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import re module

import re

Substring ='string'

String1 ='''We are learning regex with geeksforgeeks

 regex is very useful for string matching.

 It is fast too.'''

String2 ='''string We are learning regex with geeksforgeeks

 regex is very useful for string matching.

 It is fast too.'''

# Use of re.search() Method

print(re.search(Substring, String1, re.IGNORECASE))

# Use of re.match() Method

print(re.match(Substring, String1, re.IGNORECASE))

# Use of re.search() Method

print(re.search(Substring, String2, re.IGNORECASE))

# Use of re.match() Method

print(re.match(Substring, String2, re.IGNORECASE))  
  
---  
  
 __

 __

 **Output :**  

    
    
    <_sre.SRE_Match object; span=(69, 75), match='string'>
    None
    

**Conclusion :**  

  1. **re.search()** is returning match object and implies that first match found at index 69.
  2.  **re.match()** is returning none because match exists in the second line of the string and re.match() only works if the match is found at the beginning of the string.   

  3. **re.IGNORECASE** is used to ignore the case sensitivity in the strings.   

  4. Both **re.search()** and **re.match()** returns only the first occurrence of a substring in the string and ignore others.   

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

