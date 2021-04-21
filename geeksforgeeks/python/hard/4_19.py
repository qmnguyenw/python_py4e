Merging and Updating Dictionary Operators in Python 3.9



Python 3.9 is still in development and scheduled to be released in October
this year. On Feb 26, alpha 4 versions have been released by the development
team. One of the latest features in Python 3.9 is the merge and update
operators.

There are various ways in which Dictionaries can be merged by the use of
various functions and constructors in Python. In this article, we will look
upon all the old ways of doing these operations as well as about the latest
operator released by the Python development team, which will surely be
relevant for all the Python programmers.

  *  **Using method update():**

Update() method is used to merge the second dictionary into the first
dictionary without creating any new dictionary and updating the value of the
first dictionary, whereas, the value of the second dictionary remains
unaltered. Also, the function doesn’t return any value.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge dict

# using update() method 

 

 

dict1 = {'a': 10, 'b': 5, 'c': 3} 

dict2 = {'d': 6, 'c': 4, 'b': 8}

 

# This return None 

print("value returned by update function :", 

 dict1.update(dict2)) 

 

# changes made in dict1 

print("dict1 :", dict1)

print("dict2 :", dict2)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    value returned by update function : None
    dict1 : {'a': 10, 'b': 8, 'c': 4, 'd': 6}
    dict2 : {'d': 6, 'c': 4, 'b': 8}
    

