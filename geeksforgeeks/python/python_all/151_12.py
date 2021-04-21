Python | Segregating Key’s Values



Many times when we have the requirement to separate the values of a dictionary
key in case we have a list of dictionary and need to separate it’s different
key’s values. This is quite useful utility used in web development. Let’s
discuss certain ways in which this can be done.

 **Method #1 : Using list comprehension +tuple()**  
The list comprehension can be coupled with tuple function and can be used to
perform this particular task. List comprehension does the task of segregation
and tuple function is used put them into separate tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# segragation of keys and values

# using list comprehension + tuple()

 

# initializing list of dictionaries

test_list = [{'Nikhil' : 1, 'Akash' : 2},

 {'Nikhil' : 3, 'Akash' : 4}]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + tuple()

# to segregate keys and values

res = [tuple(i["Nikhil"] for i in test_list),
tuple(i["Akash"]

 for i in test_list)]

 

# printing result 

print("The segregated keys and values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [{'Akash': 2, 'Nikhil': 1}, {'Akash': 4, 'Nikhil': 3}]
    The segregated keys and values : [(1, 3), (2, 4)]
    

**Method #2 : Usingmap() + zip() + list()**  
These functions can also be coupled to achieve this particular functionality.
The map function is used to extract the values, zip function is used to do the
segregation. And list function is used at end to bind the result into a
dictionary.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# segragation of keys and values

# using map() + list() + zip()

 

# initializing list of dictionaries

test_list = [{'Nikhil' : 1, 'Akash' : 2},

 {'Nikhil' : 3, 'Akash' : 4}]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using map() + list() + zip()

# to segregate keys and values

res = list(zip(*map(dict.values, test_list)))

 

# printing result 

print("The segregated keys and values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [{'Akash': 2, 'Nikhil': 1}, {'Akash': 4, 'Nikhil': 3}]
    The segregated keys and values : [(2, 4), (1, 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

