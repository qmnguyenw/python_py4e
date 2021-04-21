Python | Convert a list of Tuples into Dictionary



Sometimes you might need to convert a tuple to dict object to make it more
readable.  
In this article, we will try to learn how to convert a list of tuples into a
dictionary. Here we will find two methods of doing this.  
 **Examples:**

    
    
    Input : [("akash", 10), ("gaurav", 12), ("anand", 14), 
             ("suraj", 20), ("akhil", 25), ("ashish", 30)]
    Output : {'akash': [10], 'gaurav': [12], 'anand': [14], 
              'ashish': [30], 'akhil': [25], 'suraj': [20]}
    
    Input : [('A', 1), ('B', 2), ('C', 3)]
    Output : {'B': [2], 'A': [1], 'C': [3]}
    
    Input : [("Nakul",93), ("Shivansh",45), ("Samved",65),
                 ("Yash",88), ("Vidit",70), ("Pradeep",52)]
    Output : {'Nakul': [93], 'Shivansh': [45], 'Samved': [65], 
                'Yash': [88], 'Vidit': [70], 'Pradeep': [52]}
    
    Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
    Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1 : Use ofsetdefault()**

Here we have used the dictionary method _setdefault()_ to convert the first
parameter to key and the second to the value of the dictionary.
_setdefault(key, def_value)_ function searches for a key and displays its
value and creates a new key with def_value if the key is not present. Using
the append function we just added the values to the dictionary.

 **Example 1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert into dictionary

 

def Convert(tup, di):

 for a, b in tup:

 di.setdefault(a, []).append(b)

 return di

 

# Driver Code 

tups = [("akash", 10), ("gaurav", 12), ("anand",
14), 

 ("suraj", 20), ("akhil", 25), ("ashish", 30)]

dictionary = {}

print (Convert(tups, dictionary))  
  
---  
  
 __

 __

Output:

    
    
    {'akash': [10], 'gaurav': [12], 'anand': [14], 
     'ashish': [30], 'akhil': [25], 'suraj': [20]}
    

**Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert into dictionary

list_1=[("Nakul",93), ("Shivansh",45),
("Samved",65),

 ("Yash",88), ("Vidit",70), ("Pradeep",52)]

dict_1=dict()

 

for student,score in list_1:

 dict_1.setdefault(student, []).append(score)

print(dict_1)  
  
---  
  
 __

 __

Output:

    
    
    {'Nakul': [93], 'Shivansh': [45], 'Samved': [65], 'Yash': [88], 'Vidit': [70], 'Pradeep': [52]}
    

**Method 2 : Use of dict() method**

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert into dictionary

def Convert(tup, di):

 di = dict(tup)

 return di

 

# Driver Code 

tups = [("akash", 10), ("gaurav", 12), ("anand",
14), 

 ("suraj", 20), ("akhil", 25), ("ashish", 30)]

dictionary = {}

print (Convert(tups, dictionary))  
  
---  
  
 __

 __

Output:

    
    
    {'anand': 14, 'akash': 10, 'akhil': 25, 
     'suraj': 20, 'ashish': 30, 'gaurav': 12}

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert into dictionary

 

print (dict([('Sachin', 10), ('MSD', 7), ('Kohli',
18), ('Rohit', 45)]))  
  
---  
  
 __

 __

Output:

    
    
    {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
    

This is a simple method of conversion from a list or tuple to a dictionary.
Here we pass a tuple into the dict() method which converts the tuple into the
corresponding dictionary.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

