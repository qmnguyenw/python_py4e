Python | List of tuples to dictionary conversion



Interconversions are always required while coding in Python, also because of
the expansion of Python as a prime language in the field of Data Science. This
article discusses yet another problem that converts to dictionary and assigns
keys as 1st element of tuple and rest as it’s value.

Let’s discuss certain ways in which this can be performed.

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

# List of tuple to dictionary conversion

# using list comprehension

 

# initializing list

test_list = [('Nikhil', 21, 'JIIT'), ('Akash', 22,
'JIIT'), ('Akshat', 22, 'JIIT')]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension

# List of tuple to dictionary conversion

res = {sub[0]: sub[1:] for sub in test_list}

 

# print result

print("The dictionary after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

> The original list : [(‘Nikhil’, 21, ‘JIIT’), (‘Akash’, 22, ‘JIIT’),
> (‘Akshat’, 22, ‘JIIT’)]  
> The dictionary after conversion : {‘Nikhil’: (21, ‘JIIT’), ‘Akshat’: (22,
> ‘JIIT’), ‘Akash’: (22, ‘JIIT’)}

