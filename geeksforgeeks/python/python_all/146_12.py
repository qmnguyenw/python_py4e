Python | Union of Value Lists



The functionality of union has been discussed many times. But sometimes, we
can have a more complex container, in which we need to check for the union of
lists which are in form of keys of dictionary. Let’s discuss certain ways to
solve this type of problem.

 **Method #1 : Using Loops**  
Using loops is a naive brute force approach to perform this particular task.
In this method, we check for keys present in both list and check for non-
repeating values to add to result. We even check for the keys completely not
present in other to add its whole list value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Union of Value Lists

# using loops

 

# initializing dicts

test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4,
5] }

test_dict2 = { "Key1" : [1, 7, 8] }

 

# printing original dicts

print("The original dict 1 : " + str(test_dict1))

print("The original dict 2 : " + str(test_dict2))

 

# using loops

# Union of Value Lists

for key in test_dict1: 

 if key in test_dict2: 

 for val in test_dict1[key]:

 if val not in test_dict2[key]: 

 test_dict2[key].append(val)

 else: 

 test_dict2[key] = test_dict1[key][:]

 

# print result

print("The dicts after union is : " + str(test_dict2))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict 1 : {'Key1': [1, 3, 4], 'key2': [4, 5]}
    The original dict 2 : {'Key1': [1, 7, 8]}
    The dicts after union is : {'Key1': [1, 7, 8, 3, 4], 'key2': [4, 5]}
    

**Method #2 : Using dictionary comprehension + set operations**  
This is the one line approach to solve the similar problem and offers a
compact alternative to above method. This solution processes by using the set
comprehension to get the necessary elements bound together into lists using
dictionary comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Union of Value Lists

# using dictionary comprehension + set operations

 

# initializing dicts

test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4,
5] }

test_dict2 = { "Key1" : [1, 7, 8] }

 

# printing original dicts

print("The original dict 1 : " + str(test_dict1))

print("The original dict 2 : " + str(test_dict2))

 

# using dictionary comprehension + set operations

# Union of Value Lists

res = {key : list(set(test_dict1.get(key, []) +
test_dict2.get(key, []))) 

 for key in set(test_dict2) | set(test_dict1)}

 

# print result

print("The dicts after union is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict 1 : {'Key1': [1, 3, 4], 'key2': [4, 5]}
    The original dict 2 : {'Key1': [1, 7, 8]}
    The dicts after union is : {'Key1': [1, 7, 8, 3, 4], 'key2': [4, 5]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

