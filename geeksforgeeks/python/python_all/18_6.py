Python Program to swap the First and the Last Character of a string



Given a String. The task is to swap the first and the last character of the
string.

 **Examples:**

    
    
     **Input:** GeeksForGeeks
    **Output:** seeksForGeekG
     
    **Input:** Python
    **Output:** nythoP

Python string is immutable which means we cannot modify it directly. But
Python has string slicing which makes it very easier to perform string
operations and make modifications. Follow the below steps to swap characters –

  1. We initialize a variable **start,** which stores the first character of the string ( **string[0]** )
  2. We initialize another variable **end** that stores the last character ( **string[-1]** )
  3. Then we will use string slicing, **string[1:-1]** , this will access all the characters from the 2nd position excluding the last character.
  4. Then we add these three as required forming a new string that has the first and last characters of the original string swapped. And then we will print it.

Below is the implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def swap(string):

 

 # storing the first character

 start = string[0]

 

 # storing the last character

 end = string[-1]

 

 swapped_string = end + string[1:-1] + start

 print(swapped_string)

 

# Driver Code

swap("GeeksforGeeks")

swap("Python")  
  
---  
  
 __

 __

 **Output:**

    
    
    seeksforGeekG
    nythoP

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

