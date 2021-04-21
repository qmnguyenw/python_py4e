Python end parameter in print()



By default python’s print() function ends with a newline. A programmer with
C/C++ background may wonder how to print without newline.

Python’s print() function comes with a parameter called ‘end’. By default, the
value of this parameter is ‘\n’, i.e. the new line character. You can end a
print statement with any character/string using this parameter.

 __

 __  
 __

 __

 __  
 __  
 __

# This Python program must be run with

# Python 3 as it won't work with 2.7.

 

# ends the output with a <space> 

print("Welcome to" , end = ' ') 

print("GeeksforGeeks", end = ' ')  
  
---  
  
 __

 __

Output :

    
    
    Welcome to GeeksforGeeks

One more program to demonstrate working of end parameter.

 __

 __  
 __

 __

 __  
 __  
 __

# This Python program must be run with

# Python 3 as it won't work with 2.7.

 

# ends the output with '@'

print("Python" , end = '@') 

print("GeeksforGeeks")  
  
---  
  
 __

 __

Output :

  

  

    
    
    Python@GeeksforGeeks

This article is contributed by **Ankit Bindal**. If you like GeeksforGeeks and
would like to contribute, you can also write an article and mail your article
to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

