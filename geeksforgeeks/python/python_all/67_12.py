Python – Prefix tuple records



Sometimes, while working with Python lists, we can have problem in which we
need to find all the tuples which begin with a paricular tuple record. This
kind of problem can find application in data domains. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using list comprehension +zip() + all()**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of checking using all(), which checks for all prefix
elements equality with elements zipped with prefixes using zip(). The list
comprehension is used to perform for all the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Prefix tuple records

# Using list comprehension + zip() + all()

 

# initializing list

test_list = [('Gfg', 'best', 'geeks'), ('Gfg',
'good'), 

 ('Gfg', 'best', 'CS'), ('Gfg', 'love')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing prefix tuple

pref_tup = ('Gfg', 'best')

 

# Prefix tuple records

# Using list comprehension + zip() + all()

res = [tup for tup in test_list if all(x == y for
x, y in

 zip(tup, pref_tup))]

 

# printing result 

print("The filtered tuples : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [(‘Gfg’, ‘best’, ‘geeks’), (‘Gfg’, ‘good’), (‘Gfg’,
> ‘best’, ‘CS’), (‘Gfg’, ‘love’)]  
> The filtered tuples : [(‘Gfg’, ‘best’, ‘geeks’), (‘Gfg’, ‘best’, ‘CS’)]

  

  

**Method #2 : Usingfilter() + lambda + generator expression + all()**  
The combination of above functions can be used to solve this particular
problem. In this, we perform the task of filtering using filter() and logic
compilation using lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Prefix tuple records

# Using filter() + lambda + generator expression + all()

 

# initializing list

test_list = [('Gfg', 'best', 'geeks'), ('Gfg',
'good'), 

 ('Gfg', 'best', 'CS'), ('Gfg', 'love')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing prefix tuple

pref_tup = ('Gfg', 'best')

 

# Prefix tuple records

# Using filter() + lambda + generator expression + all()

res = list(filter(lambda sub: all([sub[idx] == ele

 for idx, ele in enumerate(pref_tup)]), test_list))

 

# printing result 

print("The filtered tuples : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [(‘Gfg’, ‘best’, ‘geeks’), (‘Gfg’, ‘good’), (‘Gfg’,
> ‘best’, ‘CS’), (‘Gfg’, ‘love’)]  
> The filtered tuples : [(‘Gfg’, ‘best’, ‘geeks’), (‘Gfg’, ‘best’, ‘CS’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

