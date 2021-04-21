Python | Convert List of Dictionary to Tuple list



Given a list of dictionaries, write a python code to convert list of
dictionary into list if tuples.

 **Examples:**

    
    
    **Input:**
    [{'a':[1, 2, 3], 'b':[4, 5, 6]}, 
     {'c':[7, 8, 9], 'd':[10, 11, 12]}]
    
    **Output:**
    [('b', 4, 5, 6), ('a', 1, 2, 3), ('d', 10, 11, 12), ('c', 7, 8, 9)]
    
    **Input:**
    [{'a':['America', 'Australia'], 'b':['Bhutan', 'Bhopal']},
     {'c':['Canada', 'California'], 'd':['Denmark', 'Delhi']}]
    
    **Output:**
    [('a', 'America', 'Australia'), ('b', 'Bhutan', 'Bhopal'),
     ('c', 'Canada', 'California'), ('d', 'Denmark', 'Delhi')]
    

Below are various methods to convert list of dictionaries to list of tuples.

 **Method #1: Using Naive Approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting list of dictionary to list of tuples

 

# initialising list of dictionary

ini_list = [{'a':[1, 2, 3], 'b':[4, 5,
6]},

 {'c':[7, 8, 9], 'd':[10, 11, 12]}]

 

# converting to list of tuples

temp_dict = {}

result = []

for ini_dict in ini_list:

 for key in ini_dict.keys():

 if key in temp_dict:

 temp_dict[key] += ini_dict[key]

 else:

 temp_dict[key] = ini_dict[key]

 

for key in temp_dict.keys():

 result.append(tuple([key] + temp_dict[key]))

 

# printing result

print ("Resultant list of tuples: {}".format(result))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Resultant list of tuples: [('a', 1, 2, 3), ('d', 10, 11, 12), ('b', 4, 5, 6), ('c', 7, 8, 9)]
    

  
**Method #2: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting list of dictionary to list of tuples

 

# initialising list of dictionary

ini_list = [{'a':[1, 2, 3], 'b':[4, 5,
6]},

 {'c':[7, 8, 9], 'd':[10, 11, 12]}]

 

# converting to list of tuples

dict_list = [(key, )+tuple(val) for dic in ini_list 

 for key, val in dic.items()]

 

# printing result

print ("Resultant list of tuples: {}".format(dict_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Resultant list of tuples: [('b', 4, 5, 6), ('a', 1, 2, 3), ('d', 10, 11, 12), ('c', 7, 8, 9)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

