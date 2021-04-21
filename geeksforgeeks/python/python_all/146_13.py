Python | Dictionary to list of tuple conversion



Inter conversion between the datatypes is a problem that has many use cases
and is usual subproblem in the bigger problem to solve. The conversion of
tuple to dictionary has been discussed before. This article discusses a
converse case in which one converts the dictionary to list of tuples as the
way to represent the problem. Let’s discuss certain ways in which this problem
can be solved.

 **Method #1 : Using list comprehension + tuple +items()**  
This problem can be solved by using list comprehension for the construction of
list and the tuples are constructed by manually inserting the keys in the
tuples and items function is used to fetch the items key and values of
dictionary in form of tuples.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dictionary to list of tuple conversion

# using list comprehension + tuple + items()

 

# initializing Dictionary

test_dict = {"Nikhil" : (22, "JIIT"), "Akshat" : (21,
"JIIT")} 

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# using list comprehension + tuple + items()

# Dictionary to list of tuple conversion

res = [(key, i, j) for key, (i, j) in test_dict.items()]

 

# print result

print("The list after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'Nikhil': (22, 'JIIT'), 'Akshat': (21, 'JIIT')}
    The list after conversion : [('Nikhil', 22, 'JIIT'), ('Akshat', 21, 'JIIT')]
    

**Method #2 : Using list comprehension +items() \+ “+” operator**  
This method is similar to the above function with the modification of the
above method and allows the functionality to add as many possible keys rather
than restricted number that were allowed by the above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dictionary to list of tuple conversion

# using list comprehension + items() + "+" operator

 

# initializing Dictionary

test_dict = {"Nikhil" : (22, "JIIT"), "Akshat" : (21,
"JIIT")} 

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# using list comprehension + items() + "+" operator

# Dictionary to list of tuple conversion

res = [(key, ) + val for key, val in test_dict.items()]

 

# print result

print("The list after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'Nikhil': (22, 'JIIT'), 'Akshat': (21, 'JIIT')}
    The list after conversion : [('Nikhil', 22, 'JIIT'), ('Akshat', 21, 'JIIT')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

