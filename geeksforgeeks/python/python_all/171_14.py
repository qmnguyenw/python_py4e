Python | Remove spaces from dictionary keys



In Python, dictionary is a collection which is unordered, changeable and
indexed. Dictionaries are written with curly brackets, and they have keys and
values. It is used to hash a particular key.

Let’s see how to remove spaces from dictionary keys in Python.

 **Method #1:**  
Using translate() function here we visit each key one by one and remove
space with the none. Here translate function takes parameter 32, none where 32
is ASCII value of space ‘ ‘ and replaces it with none.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove space from keys

 

# creating a dictionary of type string

 

Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',

 'P 0 3 ': 'Soft Computing'}

 

# removing spaces from keys

# storing them in sam dictionary

Product_list = { x.translate({32:None}) : y 

 for x, y in Product_list.items()}

 

# printing new dictionary

print (" New dictionary : ", Product_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    New dictionary :  {'P01': 'DBMS', 'P03': 'Soft Computing', 'P02': 'OS'}
    

  
**Method #2:**  
Using replace() function. In this method, we visit each key in dictionary
one by one and replace all spaces in key with no space. This function takes as
argument space and second non-space.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove space from keys

 

# creating a dictionary of type string

 

Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',

 'P 0 3 ': 'Soft Computing'};

 

# removing spaces from keys

# storing them in sam dictionary

Product_list = {x.replace(' ', ''): v 

 for x, v in Product_list.items()}

 

# printing new dictionary

print (" New dictionary : ", Product_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    New dictionary :  {'P03': 'Soft Computing', 'P01': 'DBMS', 'P02': 'OS'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

