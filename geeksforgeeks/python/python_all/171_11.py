Iterate over characters of a string in Python



In Python, while operating with String, one can do multiple operations on it.
Let’s see how to iterate over characters of a string in Python.

 **Example #1:** Using simple iteration and range()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to iterate over characters of a string

 

# Code #1

string_name = "geeksforgeeks"

 

# Iterate over the string

for element in string_name:

 print(element, end=' ')

print("\n")

 

 

# Code #2

string_name = "GEEKS"

 

# Iterate over index

for element in range(0, len(string_name)):

 print(string_name[element])  
  
---  
  
 __

 __

 **Output:**

    
    
    g e e k s f o r g e e k s 
    
    G
    E
    E
    K
    S
    

  
**Example #2:** Using enumerate() function

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to iterate over characters of a string

 

string_name = "Geeks"

 

# Iterate over the string

for i, v in enumerate(string_name):

 print(v)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    G
    e
    e
    k
    s
    

