Different ways of sorting Dictionary by Keys and Reverse sorting by keys



 **Prerequisite:**Dictionaries in Python

A dictionary is a collection which is unordered, changeable and indexed. In
Python, dictionaries are written with curly brackets, and they have keys and
values. We can access the values of the dictionary using keys. In this
article, we will discuss 10 different ways of sorting the Python dictionary by
keys and also reverse sorting by keys.

###  **Using sorted() and keys():**

 **keys()** method returns a view object that displays a list of all the keys
in the dictionary. **sorted()** is used to sort the keys of the dictionary.

 **Examples:**

    
    
     **Input:**
    my_dict = {'c':3, 'a':1, 'd':4, 'b':2}
    
    **Output:**
    a: 1
    b: 2
    c: 3
    d: 4
    
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Initialising a dictionary

my_dict = {'c':3, 'a':1, 'd':4, 'b':2}

 

# Sorting dictionary

sorted_dict = my_dict.keys()

sorted_dict = sorted(sorted_dict)

 

# Printing sorted dictionary

print("Sorted dictionary using sorted() and keys() is : ")

for key in sorted_dict:

 print(key,':', my_dict[key])  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Sorted dictionary using sorted() and keys() is : 
    a : 1
    b : 2
    c : 3
    d : 4
    

