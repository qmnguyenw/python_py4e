Python Regex – re.MatchObject.start() and re.MatchObject.end() functions



In this article, we are going to see **re.MatchObject.start()** and
**re.MatchObject.end()** regex methods.

## re.MatchObject.start()

This method returns the first index of the substring matched by _group._

>  **Syntax:** re.MatchObject.start([group])
>
>  **Parameter:**
>
>   *  **group: (optional)** _group_ defaults to zero (meaning the whole
> matched substring). Return -1 if _group_ exists but did not contribute to
> the match.
>

>
> **Return:** Index of start of the substring matched by _group._
>
>  **AttributeError:** If a matching pattern is not found then it raise
> AttributeError.

## re.MatchObject.end()

This method returns the last index of the substring matched by _group._

>  **Syntax:** re.MatchObject.end([group])
>
>  
>
>
>  
>
>
>  **Parameter:**
>
>   *  **group: (optional)** _group_ defaults to zero (meaning the whole
> matched substring). Return -1 if _group_ exists but did not contribute to
> the match.
>

>
> **Return:** Index of end of the substring matched by _group._
>
>  **AttributeError:** If a matching pattern is not found then it raise
> AttributeError.

Consider the below example:

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import re

 

# getting the match of the the string

search_pattern = re.search('\d+',

 '1234')

 

""" 

d: stands for integer

+: means a consecutive set of 

characters satisfying a condition. 

Hence d+ will match consecutive 

integer string 

"""

 

print(search_pattern.string)

 

print(search_pattern.start())

 

print(search_pattern.end())  
  
---  
  
 __

 __

 **Output:**

    
    
    1234
    0
    4

Let’s understand the code. In the third line of the code we use the
**re.search()** method to find a match in the given string(‘ **1234** ‘) the ‘
**d** ‘ **** indicates that we are searching for a numeric character and the ‘
**+** ‘ indicates that we are searching for continuous numeric characters in
the given string. The result we get is a **re.MatchObject** which is stored in
search_pattern. If you print **search_pattern.string** you will get ‘1234’ as
output.

In the above example, the **search_pattern.start()** returns value **0** as
the index of the first element of the matched string in the given string is 0
and the **search_pattern.end()** returns **4** that is the end index after the
end of the string.

**Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import re

 

# getting the match of the the string

search_pattern = re.search('\d+',

 'abcd')

""" 

d: stands for integer

+: means a consecutive set of characters 

satisfying a condition. 

Hence d+ will match consecutive 

integer string 

"""

 

print(search_pattern.start())

 

print(search_pattern.end())  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "/home/4f904f4b53a786e10faa03122533f96b.py", line 13, in 
        print(search_pattern.start())
    AttributeError: 'NoneType' object has no attribute 'start'
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

