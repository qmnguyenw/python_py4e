Python – Common items Dictionary Value List



The functionality of union has been discussed many times. But sometimes, we
can have a more complex container, in which we need to check for the
intersection of lists which are in form of keys of dictionary. Let’s discuss
certain ways to solve this type of problem.

 **Method #1 : Using Loops**  
Using loops is a naive brute force approach to perform this particular task.
In this method, we check for keys present in both list. We even check for the
keys completely not present in other to add its whole list value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Common elements Dictionary Value List

# using loops

 

# initializing dicts

test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4,
5] }

test_dict2 = { "Key1" : [1, 7, 3] }

 

# printing original dicts

print("The original dict 1 : " + str(test_dict1))

print("The original dict 2 : " + str(test_dict2))

 

# using loops

# Common elements Dictionary Value List

res = dict()

for key in test_dict1: 

 if key in test_dict2: 

 res[key] = []

 for val in test_dict1[key]:

 if val in test_dict2[key]:

 res[key].append(val)

 

# print result

print("The dicts after intersection is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict 1 : {'Key1': [1, 3, 4], 'key2': [4, 5]}
    The original dict 2 : {'Key1': [1, 7, 3]}
    The dicts after intersection is : {'Key1': [1, 3]}
    

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

# Common elements Dictionary Value List

# using dictionary comprehension + set operations

 

# initializing dicts

test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4,
5] }

test_dict2 = { "Key1" : [1, 7, 3] }

 

# printing original dicts

print("The original dict 1 : " + str(test_dict1))

print("The original dict 2 : " + str(test_dict2))

 

# using dictionary comprehension + set operations

# Common elements Dictionary Value List

res = {key : list(set(set(test_dict1.get(key, [])) &
set(test_dict2.get(key, [])))) 

 for key in set(test_dict2) & set(test_dict1)}

 

# print result

print("The dicts after intersection is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dict 1 : {'Key1': [1, 3, 4], 'key2': [4, 5]}
    The original dict 2 : {'Key1': [1, 7, 3]}
    The dicts after intersection is : {'Key1': [1, 3]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

