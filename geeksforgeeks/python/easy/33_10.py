Logical Operators on String in Python



For strings in python, boolean operators (and, or, not) work. Let us consider
the two strings namely str1 and str2 and try boolean operators on them:  

 __

 __  
 __

 __

 __  
 __  
 __

str1= ''

str2 = 'geeks'

 

# repr is used to print the string along with the quotes

 

# Returns str1

print(repr(str1 and str2)) 

 

# Returns str1 

print(repr(str2 and str1)) 

 

# Returns str2 

print(repr(str1 or str2)) 

 

# Returns str2 

print(repr(str2 or str1)) 

 

str1 = 'for'

 

# Returns str2 

print(repr(str1 and str2)) 

 

# Returns str1 

print(repr(str2 and str1)) 

 

# Returns str1 

print(repr(str1 or str2)) 

 

# Returns str2 

print(repr(str2 or str1)) 

 

str1='geeks'

 

# Returns False

print(repr(not str1)) 

 

str1 = '' 

 

# Returns True 

print(repr(not str1)) 

 

 

# Coded by Nikhil Kumar Singh(nickzuck_007)  
  
---  
  
 __

 __

 **Output:**

    
    
    ''
    ''
    'geeks'
    'geeks'
    'geeks'
    'for'
    'for'
    'geeks'
    False
    True
    

The output of the boolean operations between the strings depends on following
things:

  1. Python considers empty strings as having boolean value of ‘false’ and non-empty string as having boolean value of ‘true’.
  2. For ‘and’ operator if left value is true, then right value is checked and returned. If left value is false, then it is returned
  3. For ‘or’ operator if left value is true, then it is returned, otherwise if left value is false, then right value is returned.

Note that the bitwise operators (| , &) don’t work for strings.

This article is contributed by **Nikhil Kumar Singh**.

  

  

If you like GeeksforGeeks and would like to contribute, you can also write an
article and mail your article to contribute@geeksforgeeks.org. See your
article appearing on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

