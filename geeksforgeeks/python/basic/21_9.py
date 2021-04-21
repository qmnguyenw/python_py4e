Python string | strip()



 **strip()** is an inbuilt function in Python programming language that
returns a copy of the string with both leading and trailing characters removed
(based on the string argument passed).  
 **Syntax:**

    
    
    string.strip([chars])
    **Parameter:**
    There is only one optional parameter in it:
    1) **chars** - a string specifying 
    the set of characters to be removed. 
    
    If the optional chars parameter is not given, all leading 
    and trailing whitespaces are removed from the string.
    **Return Value:**
    Returns a copy of the string with both leading and trailing characters removed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the use of

# strip() method 

 

string = """ geeks for geeks """

 

# prints the string without stripping

print(string) 

 

# prints the string by removing leading and trailing whitespaces

print(string.strip()) 

 

# prints the string by removing geeks

print(string.strip(' geeks'))  
  
---  
  
 __

 __

 **Output:**

    
    
        geeks for geeks     
    geeks for geeks
    for
    

__

__  
__

__

__  
__  
__

# Python Program to demonstrate use of strip() method

 

str1 = 'geeks for geeks'

# Print the string without striping.

print(str1)

 

# String whose set of characters are to be

# remove from original string at both its ends.

str2 = 'ekgs'

 

# Print string after striping str2 from str1 at both its end.

print(str1.strip(str2))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeks for geeks
     for
    

Working of above code :  
We first construct a string str1 = ‘geeks for geeks’  
Now we call strip method over str1 and pass str2 = ‘ekgs’ as arguement.  
Now python interpreter trace str1 from left.It remove the character of str1 if
it is present in str2.  
Otherwise it stops tracing.  
Now python interpreter trace str1 from right. It remove the character of str1
if it is present in str2.  
Otherwise it stop tracing.  
Now at last it returns the resultant string.

When we call strip() without argument, it removes leading and trailing spaces.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to demonstrate use of strip() method without any arguement

str1 = """ geeks for geeks """

 

# Print the string without striping.

print(str1)

 

# Print string after removing all leading 

# and trailing whitespaces.

print(str1.strip())  
  
---  
  
 __

 __

 **Input:**

    
    
        geeks for geeks     
    

**Output:**

    
    
    geeks for geeks
    

**Practical application:**  
Given a string remove occurrence of word “the” from the beginning and the end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the practical application

# strip() 

 

 

string = " the King has the largest army in the entire world the"

 

# prints the string after removing the from beginning and end

print(string.strip(" the"))  
  
---  
  
 __

 __

 **Input:**

    
    
    the King has the largest army in the entire world the
    

Output:

    
    
    King has the largest army in the entire world
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

