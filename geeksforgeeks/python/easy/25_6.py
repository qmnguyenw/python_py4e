Python | Merging two Dictionaries



There are various ways in which Dictionaries can be merged by the use of
various functions and constructors in Python. In this article, we will discuss
a few ways of merging dictionaries.

### **Using the method update()**

By using the method update() in Python, one list can be merged into another.
But in this, the second list is merged into the first list and no new list is
created. It returns _None_.  

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge dict using update() method

def Merge(dict1, dict2):

 return(dict2.update(dict1))

 

# Driver code

dict1 = {'a': 10, 'b': 8}

dict2 = {'d': 6, 'c': 4}

# This return None

print(Merge(dict1, dict2))

# changes made in dict2

print(dict2)  
  
---  
  
 __

 __

 **Output:**

    
    
    None
    {'c': 4, 'a': 10, 'b': 8, 'd': 6}
    
    

### **Using** **** in Python**  

This is generally considered a trick in Python where a single expression is
used to merge two dictionaries and stored in a third dictionary. The single
expression is **. This does not affect the other two dictionaries. ** implies
that an argument is a dictionary. Using ** [double star] is a shortcut that
allows you to pass multiple arguments to a function directly using a
dictionary. For more information refer **kwargs in Python. Using this we first
pass all the elements of the first dictionary into the third one and then pass
the second dictionary into the third. This will replace the duplicate keys of
the first dictionary.  

  

  

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge dict using a single

# expression

def Merge(dict1, dict2):

 res = {**dict1, **dict2}

 return res

 

# Driver code

dict1 = {'a': 10, 'b': 8}

dict2 = {'d': 6, 'c': 4}

dict3 = Merge(dict1, dict2)

print(dict3)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'b': 8, 'a': 10, 'c': 4, 'd': 6}
    
    

### Using | in Python 3.9

In the latest update of python now we can use “|” operator to merge two
dictionaries. It is a very convenient method to merge dictionaries.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

# Python code to merge dict using a single 

# expression

def Merge(dict1, dict2):

 res = dict1 | dict2

 return res

 

# Driver code

dict1 = {'x': 10, 'y': 8}

dict2 = {'a': 6, 'b': 4}

dict3 = Merge(dict1, dict2)

print(dict3)

# This code is contributed by virentanti16  
  
---  
  
 __

 __

 **Output:**

    
    
    {'x': 10, 'a': 6,  'b': 4, 'y': 8}
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

