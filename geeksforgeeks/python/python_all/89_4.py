Python – Step Frequency of elements in List



Sometimes, while working with Python, we can have a problem in which we need
to compute frequency in list. This is quite common problem and can have
usecase in many domains. But we can atimes have problem in which we need
incremental count of elements in list. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using loop +defaultdict()**  
The combination of above functions can be used to perform this task. In this,
we just initialize list with a default value and increment its frequency using
a loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Step Frequency of elements in List

# using loop + defaultdict()

from collections import defaultdict

 

# Initializing loop 

test_list = ['gfg', 'is', 'best', 'gfg', 'is',
'life']

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Step Frequency of elements in List

# using loop + defaultdict()

res_d = defaultdict(int)

res = []

for ele in test_list:

 res_d[ele] += 1

 res.append(res_d[ele])

 

# printing result 

print ("Step frequency of elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'gfg', 'is', 'life']
    Step frequency of elements is : [1, 1, 1, 2, 2, 1]
    

**Method #2 : Usinglist comprehension + enumerate()**  
The combination of above functions can be used to solve this problem. In this
we just iterate and store the counter using enumerate().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Step Frequency of elements in List

# using list comprehension + enumerate()

from collections import defaultdict

 

# Initializing loop 

test_list = ['gfg', 'is', 'best', 'gfg', 'is',
'life']

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Step Frequency of elements in List

# using list comprehension + enumerate()

res = [test_list[ : idx + 1].count(ele) for (idx, ele) in
enumerate(test_list)]

 

# printing result 

print ("Step frequency of elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'gfg', 'is', 'life']
    Step frequency of elements is : [1, 1, 1, 2, 2, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

