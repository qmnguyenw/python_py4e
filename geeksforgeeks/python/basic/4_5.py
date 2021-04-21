re.MatchObject.group() function in Python Regex



 **re.MatchObject.group()** method returns the complete matched subgroup by
default or a tuple of matched subgroups depending on the number of arguments

>  **Syntax:** re.MatchObject.group([group])
>
>  **Parameter:**
>
>   *  **group: (optional)** _group_ defaults to zero (meaning that it it will
> return the complete matched string). Return -1 if _group_ exists but did not
> contribute to the match.
>

>
>  **Return:** Complete match by default else one or more matched subgroups
> depending on the arguments.
>
>  **IndexError:** If the group number passed as arguement is negative or
> greater than the number of groups defined in the match pattern then an
> IndexError exception will be raised
>
>  
>
>
>  
>
>
>  **AttributeError:** If a matching pattern is not found then it raise
> AttributeError.

Consider the below example:

 **Example 1:**

A program to print the username, comapany_name and domain from a emailID

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import re

 

"""We create a re.MatchObject and store it in 

 match_object variable

 the '()' parenthesis are used to define a 

 specific group"""

 

match_object = re.match(r'(\w+)@(\w+)\.(\w+)',
'username@geekforgeeks.org')

 

""" w in above pattern stands for alphabetical character

 + is used to match a consecutive set of characters 

 satisfying a given condition

 so w+ will match a consecutive set of alphabetical characters"""

 

# for entire match

print(match_object.group())

# also print(match_object.group(0)) can be used

 

# for the first parenthesized subgroup

print(match_object.group(1))

 

# for the second parenthesized subgroup

print(match_object.group(2))

 

# for the third parenthesized subgroup

print(match_object.group(3))

 

# for a tuple of all matched subgroups

print(match_object.group(1, 2, 3))  
  
---  
  
 __

 __

 **Output:**

    
    
    username@geekforgeeks.org
    username
    geekforgeeks
    org
    ('username', 'geekforgeeks', 'org')
    

It’s time to understand the above program. We use a **re.match()** method to
find a match in the given string(‘ **username@geekforgeeks.org** ‘) the ‘
**w** ‘ indicates that we are searching for an alphabetical character and the
‘ **+** ‘ indicates that we are searching for continuous alphabetical
characters in the given string. Note the use of ‘ **()** ‘ the parenthesis is
used to define different subgroups, in the above example, we have three
subgroups in the match pattern. The result we get is a **re.MatchObject**
which is stored in match_object.

 **Note:** To know more about regex patterns refer Python regex

  

  

Depending on the arguments passed the group method returns us different
strings and also it returns a tuple of matched strings.

 **Example 2:**

If we pass an invalid group number in the method argument then we will get an
IndexError exception.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import re

 

"""We create a re.MatchObject and store it in 

 match_object variable

 the '()' parenthesis are used to define a 

 specific group"""

 

match_object = re.match(r'(\w+)@(\w+)\.(\w+)',
'username@geekforgeeks.org')

 

""" w in above pattern stands for alphabetical character

 + is used to match a consecutive set of characters 

 satisfying a given condition

 so w+ will match a consecutive set of alphabetical characters"""

 

# Following line will raise IndexError exception

print(match_object.group(7))  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "/home/8da42759204c98da7baa88422a4a74e0.py", line 17, in 
        print(match_object.group(7))
    IndexError: no such group
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

