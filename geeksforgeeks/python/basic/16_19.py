Python dictionary (Avoiding Mistakes)



 **What is dict in python ?**  
Python dictionary is similar to hash table in languages like C++. Dictionary
are used to create a key value pair in python. In place of key there can be
used String Number and Tuple etc. In place of values there can be anything.
Python Dictionary is represented by curly braces. An empty dictionary is
represented by {}. In Python dictionary key and values are separated by ‘:’
and key values pair are separted by ‘, ‘ . Below example explains it clearly  
 **Example**

 __

 __  
 __

 __

 __  
 __  
 __

# program to understand dictionary in python

 

# creating an empty dictionary

mydictionary ={}

 

# inserting values in dictionary

mydictionary ={'name':'Ankit',

 'college':'MNNIT',

 'address':'Allahabad'};

 

# print the dictionary

print(mydictionary)  
  
---  
  
 __

 __

 **Output :**

    
    
      {'address': 'Allahabad', 'name': 'Ankit', 'college': 'MNNIT'}
    

**where is used ?**  
Dictionaries gives us power to model a variety of real world applications. We
can create a dictionary of person where we can store all information related
to that person as name age contact location etc. In dictionaries can be store
any type of information such as words and their meaning. Python dictionaries
are used very much in machine learning where machine talks with human in that
situation some predefined words are stored as keys and their meaning as values
and when user want anything that thing is searched in keys if it is found then
its value is returned otherwise it shows some error. In fact python dictionary
can be used anywhere where hashing is used in normal old language.  
 **Example to understand use of dict**

 __

 __  
 __

 __

 __  
 __  
 __

# program to understand dictionary in python

 

# creating an empty dictionary

mydictionary ={}

 

# inserting values in dictionary

mydictionary ={'greeting':'Hello',

 'status':'how are you',

 'thanks':'thanks visit again'};

 

# print values according to choice

print(mydictionary['greeting'])

print(mydictionary['status'])

print(mydictionary['thanks'])  
  
---  
  
 __

 __

 **Output :**

    
    
    Hello
    how are you
    thanks visit again
    
    

**Common mistakes while using dicts and overcomes**  
Following are some mistake while using dict in python.  
 **1 )** To access element of dictionary in python never direct access element
using key name always try to use .get method. If key is not present then .get
method would print none while [key] will terminate the whole program.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# program to understand dictionary in python

 

# creating an empty dictionary

mydictionary ={}

 

# inserting values in dictionary

mydictionary ={'greeting':'Hello',

 'status':'how are you',

 'thanks':'thanks visit again'};

 

# print values according to choice

print(mydictionary['greeting'])

print(mydictionary['status'])

print(mydictionary['thanks'])

 

# this will print none

print(mydictionary.get('college'))

 

# this will throw an error

print(mydictionary['college'])  
  
---  
  
 __

 __

 **Output :**

    
    
    Hello
    how are you
    thanks visit again
    None
    

**Runtime Error**

    
    
     Traceback (most recent call last):
      File "/home/ce65dd34285f0cb0781de2a068e658fa.py", line 14, in 
        print(mydictionary['college'])
    KeyError: 'college'
    

**2 )** When we want to copy a dictionary to another dictionary then there
should be proper knowledge of copying method

  * new_dictionary = old_dictionary : This line means that old_dictionary and new_dictionary will refer to same object means that change in one dictionary will reflect to other dictionary.
  * new_dictionary = dict(old_dictionary) and new_dictionary = old_dictionary.copy() : will copy old dictionary to new dictionary means that update in old will not reflect update in d but values in e will be copied by using references . This will perform shallow copy
  * new_dictionary = copy.deepcopy(old_dictionary) : This will generate an deep copy .

 __

 __  
 __

 __

 __  
 __  
 __

# program to understand dictionary in python

 

# creating an empty dictionary

mydictionary ={}

 

# inserting values in dictionary

mydictionary ={'greeting':'Hello',

 'status':'how are you',

 'thanks':'thanks visit again'};

 

# print values according to choice

print(mydictionary['greeting'])

print(mydictionary['status'])

print(mydictionary['thanks'])

 

# copying dictionary

m = mydictionary

print(m)  
  
---  
  
 __

 __

 **Output :**

    
    
    Hello
    how are you
    thanks visit again
    {'greeting': 'Hello', 'status': 'how are you', 'thanks': 'thanks visit again'}
    

**When not to use dicts ?**  
Python dict are useful in many situation but in some situation their use must
be avoided .In python never think that only dictionary are associative array.
In dict we should try to store values of same type.

  * If we want to search values whether values is present into dictionary or not always use in that situation python set because in python set is an associative array with bool values whether element is present or not.
  * For fixed number of attribute always use Class or named tuple in python .
  * When you want a predefined message when a particular key then use collections.defaultdict in python

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

