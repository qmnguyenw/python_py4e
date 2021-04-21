Python | Select dictionary with condition given key greater than k



In Python, sometimes we require to get only some of the dictionary required to
solve the problem. This problem is quite common in web development that we
require to get only the selective dictionary satisfying some given criteria.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# filtering of a list of dictionary

# on basis of condition

 

# initialising list of dictionary

ini_list = [{'a':1, 'b':3, 'c':7},
{'a':3, 'b':8, 'c':17},

 {'a':78, 'b':12, 'c':13}, {'a':2,
'b':2, 'c':2}]

 

# printing initial list of dictionary

print ("initial_list", str(ini_list))

 

# code to filter list

# where c is greater than 10

res = [d for d in ini_list if d['c'] > 10]

 

# printing result

print ("resultant_list", str(res))  
  
---  
  
 __

 __

 **Output:**

> initial_list [{‘c’: 7, ‘b’: 3, ‘a’: 1}, {‘c’: 17, ‘b’: 8, ‘a’: 3}, {‘c’: 13,
> ‘b’: 12, ‘a’: 78}, {‘c’: 2, ‘b’: 2, ‘a’: 2}]  
> resultant_list [{‘c’: 17, ‘b’: 8, ‘a’: 3}, {‘c’: 13, ‘b’: 12, ‘a’: 78}]

  
**Method #2: Using lambda and filter**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# filtering of list of dictionary

# on basis of condition

 

# initialising list of dictionary

ini_list = [{'a':1, 'b':3, 'c':7},
{'a':3, 'b':8, 'c':17},

 {'a':78, 'b':12, 'c':13}, {'a':2,
'b':2, 'c':2}]

 

# printing initial list of dictionary

print ("initial_list", str(ini_list))

 

# code to filter list

# where c is less than 10

res = list(filter(lambda x:x["c"] > 10, ini_list ))

 

# printing result

print ("resultant_list", str(res))  
  
---  
  
 __

 __

 **Output:**

> initial_list [{‘b’: 3, ‘c’: 7, ‘a’: 1}, {‘b’: 8, ‘c’: 17, ‘a’: 3}, {‘b’: 12,
> ‘c’: 13, ‘a’: 78}, {‘b’: 2, ‘c’: 2, ‘a’: 2}]  
> resultant_list [{‘c’: 17, ‘b’: 8, ‘a’: 3}, {‘c’: 13, ‘b’: 12, ‘a’: 78}]

  
**Method #3: Using dict comprehension and list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# filtering of list of dictionary

# on basis of condition

 

# initialising list of dictionary

ini_list = [{'a':1, 'b':3, 'c':7},
{'a':3, 'b':8, 'c':17},

 {'a':78, 'b':12, 'c':13}, {'a':2,
'b':2, 'c':10}]

 

# printing initial list of dictionary

print ("initial_list", str(ini_list))

 

# code to filter list

# where c is more than 10

 

res = [{ k:v for (k, v) in i.items()} 

 for i in ini_list if i.get('c') > 10]

 

# printing result

print ("resultant_list", str(res))  
  
---  
  
 __

 __

 **Output:**

> initial_list [{‘a’: 1, ‘c’: 7, ‘b’: 3}, {‘a’: 3, ‘c’: 17, ‘b’: 8}, {‘a’: 78,
> ‘c’: 13, ‘b’: 12}, {‘a’: 2, ‘c’: 10, ‘b’: 2}]  
> resultant_list [{‘a’: 3, ‘c’: 17, ‘b’: 8}, {‘a’: 78, ‘c’: 13, ‘b’: 12}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

