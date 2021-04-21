Python | Check if a Substring is Present in a Given String



Given two strings, check if s1 is there in s2.

 **Examples:**

    
    
    Input : s1 = geeks s2=geeks for geeks
    Output : yes
    
    Input : s1 = geek s2=geeks for geeks
    Output : yes
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We can iteratively check for every word, but Python provides us an inbuilt
function find() which checks if a substring is present in the string, which is
done in one line.  
find() function returns -1 if it is not found, else it returns the first
occurrence, so using this function this problem can be solved.  
 **Method 1: Using user defined function.**

 __

 __  
 __

 __

 __  
 __  
 __

# function to check if small string is

# there in big string

def check(string, sub_str):

 if (string.find(sub_str) == -1):

 print("NO")

 else:

 print("YES")

 

# driver code

string = "geeks for geeks"

sub_str ="geek"

check(string, sub_str)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    YES          
    

**Method 2: Using “count()” method:-**

 __

 __  
 __

 __

 __  
 __  
 __

def check(s2, s1): 

 if (s2.count(s1)>0): 

 print("YES") 

 else: 

 print("NO") 

 

s2 = "A geek in need is a geek indeed"

s1 ="geek"

check(s2, s1)   
  
---  
  
__

__

**Output:**

    
    
    YES          
    

**Method 3: Using regular expressions**  
RegEx can be used to check if a string contains the specified search pattern.
Python has a built-in package called **re** , which can be used to work with
Regular Expressions.

 __

 __  
 __

 __

 __  
 __  
 __

# When you have imported the re module, you can start using regular
expressions.

import re

 

# Take input from users

MyString1 = "A geek in need is a geek indeed"

MyString2 ="geek"

 

# re.search() returns a Match object if there is a match anywhere in the
string

if re.search( MyString2, MyString1 ):

 print("YES,string '{0}' is present in string '{1}' "
.format(MyString2,MyString1))

else:

 print("NO,string '{0}' is not present in string {1} "
.format(MyString2, MyString1) )  
  
---  
  
 __

 __

 **Output:**

    
    
    YES,string 'geek' is present in string 'A geek in need is a geek indeed' 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

