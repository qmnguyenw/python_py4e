Python | Count number of items in a dictionary value that is a list



In Python, dictionary is a collection which is unordered, changeable and
indexed. Dictionaries are written with curly brackets, and they have keys and
values. It is used to hash a particular key.

A dictionary has multiple key:value pairs. There can be multiple pairs where
value corresponding to a key is a list. To check that the value is a list or
not we use the isinstance() method which is inbuilt in Python.

isinstance() method takes two parameters:

    
    
     **object -** object to be checked
    **classinfo -** class, type, or tuple of classes and types

It return a boolean whether the object is an instance of the given class or
not.

Let’s discuss different methods to count number of items in a dictionary value
that is a list.

  

  

 **Method #1** Using in operator

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count number of items

# in a dictionary value that is a list.

def main():

 

 # defining the dictionary

 d = {'A' : [1, 2, 3, 4, 5, 6, 7,
8, 9],

 'B' : 34,

 'C' : 12,

 'D' : [7, 8, 9, 6, 4] }

 

 # using the in operator

 count = 0

 for x in d:

 if isinstance(d[x], list):

 count += len(d[x])

 print(count)

 

# Calling Main 

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

  
**Method #2:** Using list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count number of items

# in a dictionary value that is a list.

def main():

 

 # defining the dictionary

 d = {'A' : [1, 2, 3, 4, 5, 6, 7,
8, 9],

 'B' : 34,

 'C' : 12,

 'D' : [7, 8, 9, 6, 4] }

 

 # using list comprehension

 print(sum([len(d[x]) for x in d if
isinstance(d[x], list)]))

 

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

  
**Method #3:** Using dict.items()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count number of items

# in a dictionary value that is a list.

def main():

 

 # defining the dictionary

 d = { 'A' : [1, 2, 3, 4, 5, 6, 7,
8, 9],

 'B' : 34,

 'C' : 12,

 'D' : [7, 8, 9, 6, 4] }

 

 # using dict.items()

 count = 0

 for key, value in d.items():

 if isinstance(value, list):

 count += len(value)

 print(count)

 

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

  
**Method #4:** Using enumerate()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count number of items

# in a dictionary value that is a list.

def main():

 

 # defining the dictionary

 d = {'A' : [1, 2, 3, 4, 5, 6, 7,
8, 9],

 'B' : 34,

 'C' : 12,

 'D' : [7, 8, 9, 6, 4] }

 

 # using enumerate()

 count = 0

 for x in enumerate(d.items()):

 

 # enumerate function returns a tuple in the form

 # (index, (key, value)) it is a nested tuple

 # for accessing the value we do indexing x[1][1]

 if isinstance(x[1][1], list):

 count += len(x[1][1])

 print(count)

 

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    14
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

