Python | Convert dictionary to list of tuples



Given a dictionary, write a Python program to convert the given dictionary
into list of tuples.

 **Examples:**

    
    
     **Input:** { 'Geeks': 10, 'for': 12, 'Geek': 31 }
    **Output :** [ ('Geeks', 10), ('for', 12), ('Geek', 31) ]
    
    **Input:** { 'dict': 11, 'to': 22, 'list_of_tup': 33}
    **Output :** [ ('dict', 11), ('to', 22), ('list_of_tup', 33) ]
    

Below are various methods to convert dictionary to list of tuples.

 **Method #1 :** Using list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert dictionary into list of tuples

 

# Initialization of dictionary

dict = { 'Geeks': 10, 'for': 12, 'Geek': 31 }

 

# Converting into list of tuple

list = [(k, v) for k, v in dict.items()]

 

# Printing list of tuple

print(list)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [('Geek', 31), ('for', 12), ('Geeks', 10)]
    

