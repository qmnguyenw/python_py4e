Python | Tuple key dictionary conversion



Interconversions are always required while coding in Python, also because of
expansion of Python as a prime language in the field of Data Science. This
article discusses yet another problem that converts to dictionary and assigns
keys as first pair elements as tuple and rest as it’s value. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Using dictionary comprehension**  
This problem can be solved using a shorthand made using dictionary
comprehension which performs the classic Naive method of loops in single line
inside a dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tuple key dictionary conversion

# using list comprehension

 

# initializing list

test_list = [('Nikhil', 21, 'JIIT'), ('Akash', 22,
'JIIT'), ('Akshat', 22, 'JIIT')]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension

# Tuple key dictionary conversion

res = {(sub[0], sub[1]): sub[2:] for sub in
test_list}

 

# print result

print("The dictionary after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('Nikhil', 21, 'JIIT'), ('Akash', 22, 'JIIT'), ('Akshat', 22, 'JIIT')]
    The dictionary after conversion : {('Akash', 22): ('JIIT', ), ('Akshat', 22): ('JIIT', ), ('Nikhil', 21): ('JIIT', )}
    

**Method #2 : Usingdict() \+ dictionary comprehension**  
Performs task similar to the above method, just the difference comes in the
way of creation of dictionary. In the above method, dictionary is created
using comprehension, here dict function is used for creation of a dictionary.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tuple key dictionary conversion

# using dict() + dictionary comprehension

 

# initializing list

test_list = [('Nikhil', 21, 'JIIT'), ('Akash', 22,
'JIIT'), ('Akshat', 22, 'JIIT')]

 

# printing original list

print("The original list : " + str(test_list))

 

# using dict() + dictionary comprehension

# Tuple key dictionary conversion

res = dict(((idx[0], idx[1]), idx[2:]) for idx in
test_list) 

 

# print result

print("The dictionary after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('Nikhil', 21, 'JIIT'), ('Akash', 22, 'JIIT'), ('Akshat', 22, 'JIIT')]
    The dictionary after conversion : {('Akash', 22): ('JIIT', ), ('Akshat', 22): ('JIIT', ), ('Nikhil', 21): ('JIIT', )}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

