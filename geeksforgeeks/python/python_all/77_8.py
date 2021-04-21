Python – Convert Lists of List to Dictionary



Sometimes, while working with Python records, we can have problem in which we
have data in form of Lists of list and we need to allocate certain elements as
keys and certain as values to form a dictionary. This type of application can
occur in data domains. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop**  
This is brute way in which we perform this task. In this, we iterate through
the lists forming key value pairs according to required slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Lists of List to Dictionary

# Using loop

 

# initializing list

test_list = [['a', 'b', 1, 2], ['c', 'd', 3,
4], ['e', 'f', 5, 6]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Lists of List to Dictionary

# Using loop

res = dict()

for sub in test_list:

 res[tuple(sub[:2])] = tuple(sub[2:])

 

# printing result 

print("The mapped Dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5,
> 6]]  
> The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’):
> (1, 2)}

  

  

**Method #2 : Using dictionary comprehension**  
This is yet another way in which this task can be performed. This is similar
to above method, just a one liner alternative.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Lists of List to Dictionary

# Using dictionary comprehension

 

# initializing list

test_list = [['a', 'b', 1, 2], ['c', 'd', 3,
4], ['e', 'f', 5, 6]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Lists of List to Dictionary

# Using dictionary comprehension

res = {tuple(sub[:2]): tuple(sub[2:]) for sub in
test_list}

 

# printing result 

print("The mapped Dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5,
> 6]]  
> The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’):
> (1, 2)}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

