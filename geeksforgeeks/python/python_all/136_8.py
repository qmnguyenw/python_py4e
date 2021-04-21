Python | Sort dictionary keys to list



Sometimes, we wish to flatten the dictionary into list, the simple flattening
is relatively easier, but when we wish to align keys and values in sorted way,
i.e sorted by value, then it becomes quite a complex problem. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingsum() + sorted() + items() \+ lambda**  
The combination of above functions can be used to perform this particular
task. In this, firstly we sort the dictionary by keys for desired order using
sorted(), then keys and values are extracted by items() functions that are
returned as pair by lambda function. The sum function does the task of
populating the tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionary keys to list 

# Using sum() + sorted() + items() + lambda

 

# initializing dictionary

test_dict = {'Geeks' : 2, 'for' : 1, 'CS' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using sum() + sorted() + items() + lambda

# Sort dictionary keys to list 

res = list(sum(sorted(test_dict.items(), key = lambda
x:x[1]), ()))

 

# printing result 

print("List after conversion from dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Geeks': 2, 'for': 1, 'CS': 3}
    List after conversion from dictionary : ['for', 1, 'Geeks', 2, 'CS', 3]
    

**Method #2 : Usingchain() + sorted() + items() \+ lambda**  
This method is also similar to above method, the only difference is that the
construction of the final list is done by the chain method which reduces the
intermediate step of conversion to tuple and does the whole task in linear
time.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionary keys to list 

# Using chain() + sorted() + items() + lambda

from itertools import chain

 

# initializing dictionary

test_dict = {'Geeks' : 2, 'for' : 1, 'CS' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using chain() + sorted() + items() + lambda

# Sort dictionary keys to list 

res = list(chain(*sorted(test_dict.items(), key = lambda x:
x[1])))

 

# printing result 

print("List after conversion from dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Geeks': 2, 'for': 1, 'CS': 3}
    List after conversion from dictionary : ['for', 1, 'Geeks', 2, 'CS', 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

