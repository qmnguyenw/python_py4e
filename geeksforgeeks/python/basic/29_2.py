Interesting facts about strings in Python | Set 2 (Slicing)



Interesting facts about strings in Python -Set 1

Like other programming languages, it’s possible to access individual
characters of a string by using array-like indexing syntax. In this we can
access each and every element of string through their index number and the
indexing starts from 0. Python does index out of bound checking.

So, we can obtain the required character using syntax,
**string_name[index_position]** :

  * The positive index_position denotes the element from the starting(0) and the negative index shows the index from the end(-1).

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# A python program to illustrate slicing in strings

 

x = "Geeks at work"

 

# Prints 3rd character beginning from 0 

print (x[2]) 

 

# Prints 7th character 

print (x[6]) 

 

# Prints 3rd character from the rear beginning from -1 

print (x[-3]) 

 

# Length of string is 10 so it is out of bound 

print (x[15])   
  
---  
  
__

__

**Output:**

  

  

    
    
    Traceback (most recent call last):
      File "8a33ebbf716678c881331d75e0b85fe6.py", line 15, in <module>
        print x[15] 
    **IndexError: string index out of range**
    
    
    e
    a
    o

**Slicing**

To extract substring from the whole string then we use the syntax like

    
    
     **string_name[beginning: end : step]**

  * beginning represents the starting index of string
  * end denotes the end index of string which is not inclusive 
  * steps denotes the distance between the two words.

Note: We can also slice the string using beginning and only and _**steps are
optional.**_

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# A python program to illustrate

# print substrings of a string 

x = "Welcome to GeeksforGeeks"

 

# Prints substring from 2nd to 5th character 

print (x[2:5]) 

 

# Prints substring stepping up 2nd character 

# from 4th to 10th character 

print (x[4:10:2]) 

 

# Prints 3rd character from rear from 3 to 5 

print (x[-5:-3])   
  
---  
  
__

__

Output:

    
    
    lco
    oet
    Ge

This article is contributed by **Arpit Agarwal.** If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

