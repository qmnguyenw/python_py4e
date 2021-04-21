Python | Convert a list to dictionary



Given a list, write a Python program to convert the given list to dictionary
such that all the odd elements have the key, and even number elements have the
value. Since python dictionary is unordered, the output can be in any order.  
 **Examples:**  

    
    
    **Input :** ['a', 1, 'b', 2, 'c', 3]
    **Output :** {'a': 1, 'b': 2, 'c': 3}
    
    **Input :** ['Delhi', 71, 'Mumbai', 42]
    **Output :** {'Delhi': 71, 'Mumbai': 42}
    
    
    

  
**Method #1 :** dict comprehension  
To convert a list to dictionary, we can use list comprehension and make a
key:value pair of consecutive elements. Finally, typecase the list to _dict_
type.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert a

# list to dictionary

def Convert(lst):

 res_dct = {lst[i]: lst[i + 1] for i in range(0,
len(lst), 2)}

 return res_dct

 

# Driver code

lst = ['a', 1, 'b', 2, 'c', 3]

print(Convert(lst))  
  
---  
  
 __

 __

 **Output**

    
    
    {'a': 1, 'b': 2, 'c': 3}
    
    

  
**Method #2 :** Using _zip()_ method  
First create an iterator, and initialize it to variable ‘it’. Then use _zip_
method, to zip keys and values together. Finally typecast it to _dict_ type.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert a

# list to dictionary

def Convert(a):

 it = iter(a)

 res_dct = dict(zip(it, it))

 return res_dct

 

# Driver code

lst = ['a', 1, 'b', 2, 'c', 3]

print(Convert(lst))  
  
---  
  
 __

 __

 **Output**

    
    
    {'a': 1, 'b': 2, 'c': 3}
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

