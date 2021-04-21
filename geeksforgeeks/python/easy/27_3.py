max() and min() in Python



This article brings you a very interesting and lesser known function of
Python, namely max() and min(). Now when compared to their C++ counterpart,
which only allows two arguments, that too strictly being float, int or char,
these functions are **not only limited to 2 elements** , but **can hold many
elements as arguments and also support strings** in their arguments, hence
allowing to display lexicographically smallest or largest string as well.
Detailed functionality are explained below.  

**max()**

This function is used to compute the maximum of the values passed in its
argument and lexicographically largest value if strings are passed as
arguments.  

    
    
    **Syntax :**
    max(a,b,c,..,key,default)
    **Parameters :**
    **a,b,c,.. :**  similar type of data.
    **key :** key function where the iterables are passed and comparsion is performed
    **default :** default value is passed if the given iterable is empty
    **Return Value :**
    Returns the maximum of all the arguments.
    **Exceptions :**
    Returns TypeError when conflicting types are compared.
    
    
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# max()

# printing the maximum of 4,12,43.3,19,100

print("Maximum of 4,12,43.3,19 and 100 is : ",end="")

print (max( 4,12,43.3,19,100 ) )  
  
---  
  
 __

 __

Output :  

    
    
    Maximum of 4,12,43.3,19 and 100 is : 100
    
    
    

  

  

**min()**

This function is used to compute the minimum of the values passed in its
argument and lexicographically smallest value if strings are passed as
arguments.  

    
    
    **Syntax :**
    min(a,b,c,.., key,default)
    **Parameters :**
    **a,b,c,.. :**  similar type of data.
    **key** : key function where the iterables are passed and comparsion is performed
    **default** : default value is passed if the given iterable is empty
    **Return Value :**
    Returns the minimum of all the arguments.
    **Exceptions :**
    Returns TypeError when conflicting types are compared.
    
    
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# min()

# printing the minimum of 4,12,43.3,19,100

print("Minimum of 4,12,43.3,19 and 100 is : ",end="")

print (min( 4,12,43.3,19,100 ) )  
  
---  
  
 __

 __

Output :  

    
    
    Minimum of 4,12,43.3,19 and 100 is : 4
    
    
    

**Exception**

 **1\. TypeError :** These functions throw TypeError when **conflicting data
types are compared**.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the Exception of

# min() and max()

# printing the minimum of 4,12,43.3,19, "GeeksforGeeks"

# Throws Exception

print("Minimum of 4,12,43.3,19 and GeeksforGeeks is : ",end="")

print (min( 4,12,43.3,19,"GeeksforGeeks" ) )  
  
---  
  
 __

 __

Output :  

    
    
    Minimum of 4,12,43.3,19 and GeeksforGeeks is : 
    
    
    

Runtime Error :  

    
    
    Traceback (most recent call last):
      File "/home/b5da1d7f834a267f94fbbefe1b31a83c.py", line 7, in 
        print (min( 4,12,43.3,19,"GeeksforGeeks" ) )
    TypeError: unorderable types: str() < int()
    
    
    

**Practical Application**

One of the practical application among many are finding **lexicographically
largest and smallest** of Strings i.e String appearing first in dictionary or
last.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the Application of

# min() and max()

# printing the word occurring 1st among these in dict.

# "geeks", "manjeet", "algorithm", "programming"

print("The word occurring 1st in dict. among given is : ",end="")

print (min( "geeks", "manjeet", "algorithm",
"programming" ) )

# printing the word occurring last among these in dict.

# "geeks", "manjeet", "algorithm", "programming"

print("The word occurring last in dict. among given is : ",end="")

print (max( "geeks", "manjeet", "algorithm",
"programming" ) )  
  
---  
  
 __

 __

Output :  

    
    
    The word occurring 1st in dict. among given is : algorithm
    The word occurring last in dict. among given is : programming
    
    
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
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

