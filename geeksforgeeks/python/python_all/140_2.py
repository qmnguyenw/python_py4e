Python | All occurrences of substring in string



Many times while working with strings, we have problems dealing with
substrings. This may include the problem of finding all positions of a
particular substrings in a string. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using list comprehension +startswith()**  
This task can be performed using the two functionalities. The startswith
function primarily performs the task of getting the starting indices of
substring and list comprehension is used to iterate through the whole target
string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All occurrences of substring in string

# Using list comprehension + startswith()

 

# initializing string 

test_str = "GeeksforGeeks is best for Geeks"

 

# initializing substring

test_sub = "Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# printing substring 

print("The substring to find : " + test_sub)

 

# using list comprehension + startswith()

# All occurrences of substring in string 

res = [i for i in range(len(test_str)) if
test_str.startswith(test_sub, i)]

 

# printing result 

print("The start indices of the substrings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks is best for Geeks
    The substring to find : Geeks
    The start indices of the substrings are : [0, 8, 26]
    

**Method #2 : Using **re.finditer()****  
The finditer function of the regex library can help us perform the task of
finding the occurrences of the substring in the target string and the start
function can return the resultant index of each of them.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All occurrences of substring in string

# Using re.finditer()

import re

 

# initializing string 

test_str = "GeeksforGeeks is best for Geeks"

 

# initializing substring

test_sub = "Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# printing substring 

print("The substring to find : " + test_sub)

 

# using re.finditer()

# All occurrences of substring in string 

res = [i.start() for i in re.finditer(test_sub, test_str)]

 

# printing result 

print("The start indices of the substrings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks is best for Geeks
    The substring to find : Geeks
    The start indices of the substrings are : [0, 8, 26]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

