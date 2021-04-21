Python | Consecutive prefix overlap concatenation



Sometimes, while working with Python Strings, we can have application in which
we need to perform the concatenation of all elements in String list. This can
be tricky in cases we need to overlap suffix of current element with prefix of
next in case of a match. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop +endswith() + join() + list comprehension +
zip()**  
The combination of above functions can be used to perform this task. In this,
we use loop for the logic of join/no join using endswith(). If a join, that is
performed using join(). Whole logic is compiled in list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive prefix overlap concatenation

# Using endswith() + join() + list comprehension + zip() + loop

 

def help_fnc(i, j):

 for ele in range(len(j), -1, -1):

 if i.endswith(j[:ele]):

 return j[ele:]

 

# initializing list

test_list = ["gfgo", "gone", "new", "best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Consecutive prefix overlap concatenation

# Using endswith() + join() + list comprehension + zip() + loop

res = ''.join(help_fnc(i, j) for i, j in zip([''] +

 test_list, test_list))

 

# printing result 

print("The resultant joined string : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfgo', 'gone', 'new', 'best']
    The resultant joined string : gfgonewbest
    

**Method #2 : Usingreduce() + lambda + next()**  
The combination of above methods can also be employed to solve this problem.
In this, we perform the task of performing overlap using next() and endswith,
and rest of task is performed using reduce() and lambda.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive prefix overlap concatenation

# Using reduce() + lambda + next()

 

# initializing list

test_list = ["gfgo", "gone", "new", "best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Consecutive prefix overlap concatenation

# Using reduce() + lambda + next()

res = reduce(lambda i, j: i + j[next(idx 

 for idx in reversed(range(len(j) + 1)) 

 if i.endswith(j[:idx])):], test_list, '', )

 

# printing result 

print("The resultant joined string : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfgo', 'gone', 'new', 'best']
    The resultant joined string : gfgonewbest
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

