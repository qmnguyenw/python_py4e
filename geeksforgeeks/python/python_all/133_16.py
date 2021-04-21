Python | Grouping dictionary keys by value



While performing computations over dictionary, we can come across a problem in
which we might have to perform the task of grouping keys according to value,
i.e create a list of keys, it is value of. This can other in cases of
organising data in case of machine learning. Let’s discuss certain way in
which this task can be performed.  
 **Method : Using sorted() + items() + defaultdict()**  
This task can be performed by combining the tasks which can be done by above
functions. The defaultdict() is used to create a dictionary initialized with
lists, items() gets the key-value pair and grouping is helped by sorted().  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Grouping dictionary keys by value

# Using sorted() + items() + defaultdict()

from collections import defaultdict

# Initialize dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 1,
'for' : 3, 'CS' : 2}

# printing original dictionary

print("The original dictionary : " + str(test_dict))

# Using sorted() + items() + defaultdict()

# Grouping dictionary keys by value

res = defaultdict(list)

for key, val in sorted(test_dict.items()):

 res[val].append(key)

 

# printing result

print("Grouped dictionary is : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original dictionary : {'gfg': 1, 'is': 2, 'best': 1, 'for': 3, 'CS': 2}
    Grouped dictionary is : {2: ['CS', 'is'], 1: ['best', 'gfg'], 3: ['for']}

 **Method 2:**

Additionally, This task can also be performed without using any module.  
So the logic here is:  
We can check if the keys are present or not  
1\. No, then we can create key res[v] = [i]  
2\. Yes, we can append value on the key res[v] + [i]  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

d_input= {'Input.txt': 'Randy', 'Code.py': 'Stan',
'Output.txt': 'Randy'}

res = {}

for i, v in d_input.items():

 res[v] = [i] if v not in res.keys() else res[v] +
[i]

print(res)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

