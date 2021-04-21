Python | Sum list of dictionaries with same key



You have given a list of dictionaries, the task is to return a single
dictionary with sum values with the same key.

Let’s discuss different methods to do the task.

 **Method #1: Usingreduce() + operator**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the sum of values of dictionary

# with same keys in list of dictionary

 

import collections, functools, operator

 

# Initialising list of dictionary

ini_dict = [{'a':5, 'b':10, 'c':90},

 {'a':45, 'b':78}, 

 {'a':90, 'c':10}]

 

 

# printing initial dictionary

print ("initial dictionary", str(ini_dict))

 

# sum the values with same keys

result = dict(functools.reduce(operator.add,

 map(collections.Counter, ini_dict)))

 

print("resultant dictionary : ", str(result))  
  
---  
  
 __

 __

 **Output:**

> initial dictionary [{‘b’: 10, ‘a’: 5, ‘c’: 90}, {‘b’: 78, ‘a’: 45}, {‘a’:
> 90, ‘c’: 10}]  
> resultant dictionary : {‘b’: 88, ‘a’: 140, ‘c’: 100}
>
>  
>
>
>  
>

  
**Method #2: Using counter**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the sum of values of dictionary

# with same keys in list of dictionary

 

import collections

 

# Initialising list of dictionary

ini_dict = [{'a':5, 'b':10, 'c':90}, 

 {'a':45, 'b':78},

 {'a':90, 'c':10}]

 

# printing initial dictionary

print ("initial dictionary", str(ini_dict))

 

# sum the values with same keys

counter = collections.Counter()

for d in ini_dict: 

 counter.update(d)

 

result = dict(counter)

 

 

print("resultant dictionary : ", str(counter))  
  
---  
  
 __

 __

 **Output:**

> initial dictionary [{‘c’: 90, ‘a’: 5, ‘b’: 10}, {‘a’: 45, ‘b’: 78}, {‘a’:
> 90, ‘c’: 10}]  
> resultant dictionary : Counter({‘a’: 140, ‘c’: 100, ‘b’: 88})

  
**Method #3: Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the sum of values of dictionary

# with same keys in list of dictionary

 

from operator import itemgetter

 

# Initialising list of dictionary

ini_dict = [{'a':5, 'b':10, 'c':90},

 {'a':45, 'b':78}, 

 {'a':90, 'c':10}]

 

# printing initial dictionary

print ("initial dictionary", str(ini_dict))

 

# sum the values with same keys

result = {}

for d in ini_dict:

 for k in d.keys():

 result[k] = result.get(k, 0) + d[k]

 

 

print("resultant dictionary : ", str(result))  
  
---  
  
 __

 __

 **Output:**

> initial dictionary [{‘b’: 10, ‘c’: 90, ‘a’: 5}, {‘b’: 78, ‘a’: 45}, {‘c’:
> 10, ‘a’: 90}]  
> resultant dictionary : {‘b’: 88, ‘c’: 100, ‘a’: 140}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

