Python String Methods | Set 2 (len, count, center, ljust, rjust, isalpha,
isalnum, isspace & join)



Some of the string methods are covered in the set 3 below  
String Methods Part- 1

More methods are discussed in this article

 **1\. len()** :- This function returns the **length** of the string.

 **2\. count(“string”, beg, end)** :- This function **counts** the occurrence
of mentioned **substring** in whole string. This function takes 3 arguments, s
**ubstring, beginning position( by default 0) and end position(by default
string length).**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# len() and count()

str = "geeksforgeeks is for geeks"

 

# Printing length of string using len()

print (" The length of string is : ", len(str));

 

# Printing occurrence of "geeks" in string

# Prints 2 as it only checks till 15th element

print (" Number of appearance of ""geeks"" is : ",end="")

print (str.count("geeks",0,15))  
  
---  
  
 __

 __

Output:

  

  

    
    
     The length of string is :  26
     Number of appearance of geeks is : 2
    

**3\. center()** :- This function is used to **surround the string with a
character** repeated both sides of string multiple times. By default the
character is a space. Takes 2 arguments, **length of string and the
character.**

 **4\. ljust()** :- This function returns the **original string shifted to
left** that has a **character at its right**. It left adjusts the string. By
default the character is space. It also takes two arguments, **length of
string and the character.  
**  
 **5\. rjust()** :- This function returns the **original string shifted to
right** that has a **character at its left**. It right adjusts the string. By
default the character is space. It also takes two arguments, **length of
string and the character.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# center(), ljust() and rjust()

str = "geeksforgeeks"

 

# Printing the string after centering with '-'

print ("The string after centering with '-' is : ",end="")

print ( str.center(20,'-'))

 

# Printing the string after ljust()

print ("The string after ljust is : ",end="")

print ( str.ljust(20,'-'))

 

# Printing the string after rjust()

print ("The string after rjust is : ",end="")

print ( str.rjust(20,'-'))  
  
---  
  
 __

 __

Output:

    
    
    The string after centering with '-' is : ---geeksforgeeks----
    The string after ljust is : geeksforgeeks-------
    The string after rjust is : -------geeksforgeeks
    

**6\. isalpha()** :- This function returns true when all the characters in the
string are **alphabets** else returns false.

 **7\. isalnum()** :- This function returns true when all the characters in
the string are **combination of numbers and/or alphabets** else returns false.

 **8\. isspace()** :- This function returns true when all the characters in
the string are **spaces** else returns false.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# isalpha(), isalnum(), isspace()

str = "geeksforgeeks"

str1 = "123"

 

# Checking if str has all alphabets 

if (str.isalpha()):

 print ("All characters are alphabets in str")

else : print ("All characters are not alphabets in str")

 

# Checking if str1 has all numbers

if (str1.isalnum()):

 print ("All characters are numbers in str1")

else : print ("All characters are not numbers in str1")

 

# Checking if str1 has all spaces

if (str1.isspace()):

 print ("All characters are spaces in str1")

else : print ("All characters are not spaces in str1")  
  
---  
  
 __

 __

Output:

    
    
    All characters are alphabets in str
    All characters are numbers in str1
    All characters are not spaces in str1
    

**9\. join()** :- This function is used to **join a sequence** of strings
mentioned in its arguments with the string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# join()

str = "_"

str1 = ( "geeks", "for", "geeks" )

 

# using join() to join sequence str1 with str

print ("The string after joining is : ", end="")

print ( str.join(str1))  
  
---  
  
 __

 __

Output:

    
    
    The string after joining is : geeks_for_geeks
    

This article is contributed by **Manjeet Singh** .If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

