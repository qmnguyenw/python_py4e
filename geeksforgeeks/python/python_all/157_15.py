Python | Combine two dictionary adding values for common keys



Given two dictionary, the task is to combine the dictionaries such that we get
the added values for common keys in resultant dictionary.

 **Example:**

    
    
     **Input:** dict1 = {'a': 12, 'for': 25, 'c': 9}
           dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}
    
    **Output:** {'for': 325, 'Geeks': 100, 'geek': 200}
    

Let’s see some of the methods to do the task.

 **Method #1:** Naive method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to combine two dictionary

# adding values for common keys

# initializing two dictionaries

dict1 = {'a': 12, 'for': 25, 'c': 9}

dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}

 

 

# adding the values with common key

for key in dict2:

 if key in dict1:

 dict2[key] = dict2[key] + dict1[key]

 else:

 pass

 

print(dict2)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    {'for': 325, 'Geeks': 100, 'geek': 200}
    

