Python | Program to convert a tuple to a string



Given a tuple of characters, Write a python program to convert the tuple into
a string.

 **Examples:**

    
    
    **Input :** ('a', 'b', 'c', 'd', 'e')
    **Output :** abcde
    
    **Input :** ('g', 'e', 'e', 'k', 's')
    **Output :** geeks
    

**Approach**  
There are various approaches to convert a tuple to a string.

  *  **Approach 1 : using str.join()**  
The join() method is a string method and returns a string in which the
elements of sequence have been joined by str separator.  
Using join() we add the characters of the tuple and convert it into string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to convert tuple

# into string

def convertTuple(tup):

 str = ''.join(tup)

 return str

 

# Driver code

tuple = ('g', 'e', 'e', 'k', 's')

str = convertTuple(tuple)

print(str)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    geeks
    

