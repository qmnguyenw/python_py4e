Python | Find keys with duplicate values in dictionary



Given a dictionary, the task is to find keys with duplicate values. Let’s
discuss a few methods for the same.

 **Method #1: Using Naive approach**  
In this method first, we convert dictionary values to keys with the inverse
mapping and then find the duplicate keys

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# finding duplicate values from a dictionary

 

# initialising dictionary

ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}

 

# printing initial_dictionary

print("initial_dictionary", str(ini_dict))

 

# finding duplicate values

# from dictionary

# using a naive approach

rev_dict = {}

 

for key, value in ini_dict.items():

 rev_dict.setdefault(value, set()).add(key)

 

result = [key for key, values in rev_dict.items()

 if len(values) > 1]

 

# printing result

print("duplicate values", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_dictionary {'c': 3, 'b': 2, 'd': 2, 'a': 1}
    duplicate values [2]
    

  
**Method #2: Using flipping dictionary**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# finding duplicate values from dictionary

 

# initialising dictionary

ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}

 

# printing initial_dictionary

print("initial_dictionary", str(ini_dict))

 

# finding duplicate values

# from dictionary using flip

flipped = {}

 

for key, value in ini_dict.items():

 if value not in flipped:

 flipped[value] = [key]

 else:

 flipped[value].append(key)

 

# printing result

print("final_dictionary", str(flipped))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial_dictionary {'a': 1, 'c': 3, 'd': 2, 'b': 2}
    final_dictionary {1: ['a'], 2: ['d', 'b'], 3: ['c']}
    

