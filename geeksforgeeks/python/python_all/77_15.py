Python – Test Record existence in Dictionary



Sometimes while working with pool of records, we can have problem in which we
need to check the presence of particular value of a key for existence. This
can have application in many domains such as day-day programming or web
development. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using any() + generator expression**  
The combination of above functions can be used to perform this task. In this,
we simply test for all elements using any(), iterated using generator
expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Record existance in Dictionary

# Using any() + generator expression

 

# initializing list

test_list = [{ 'name' : 'Nikhil', 'age' : 22},

 { 'name' : 'Akshat', 'age' : 23},

 { 'name' : 'Akash', 'age' : 23}]

 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key and value 

test_key = 'name'

test_val = 'Nikhil'

 

# Test Record existance in Dictionary

# Using any() + generator expression

res = any(sub[test_key] == test_val for sub in
test_list)

 

# printing result 

print("Does key value contain in dictionary list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘name’: ‘Nikhil’, ‘age’: 22}, {‘name’: ‘Akshat’,
> ‘age’: 23}, {‘name’: ‘Akash’, ‘age’: 23}]  
> Does key value contain in dictionary list : True

  

  

**Method #2 : Usingfilter() \+ lambda**  
The combination of above functions can be used to perform this task. In this,
we check for all values using filter and iteration using lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Record existance in Dictionary

# Using filter() + lambda

 

# initializing list

test_list = [{ 'name' : 'Nikhil', 'age' : 22},

 { 'name' : 'Akshat', 'age' : 23},

 { 'name' : 'Akash', 'age' : 23}]

 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key and value 

test_key = 'name'

test_val = 'Nikhil'

 

# Test Record existance in Dictionary

# Using filter() + lambda

res = filter(lambda sub: test_val in sub.values(), test_list)

if len(list(res)):

 res = True

else :

 res = False

 

# printing result 

print("Does key value contain in dictionary list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘name’: ‘Nikhil’, ‘age’: 22}, {‘name’: ‘Akshat’,
> ‘age’: 23}, {‘name’: ‘Akash’, ‘age’: 23}]  
> Does key value contain in dictionary list : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

