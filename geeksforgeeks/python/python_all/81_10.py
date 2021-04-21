Python – Cumulative List Split



Sometimes, while working with String lists, we can have a problem in which we
need to perform the task of split and return all the split instances of list
in cummulative way. This kind of problem can occur in many domains in which
data is involved. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop**  
This is brute force way in which this task is performed. In this, we test for
the list and append the list when ever we encounter the split character.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative List Split

# Using loop

 

# initializing list

test_list = ['gfg-is-all-best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Split char

spl_char = "-"

 

# Cummulative List Split

# Using loop

res = []

for sub in test_list:

 for idx in range(len(sub)):

 if sub[idx] == spl_char:

 res.append([ sub[:idx] ])

 res.append([ sub ])

 

# printing result 

print("The Cummulative List Splits : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg-is-all-best']
    The Cummulative List Splits : [['gfg'], ['gfg-is'], ['gfg-is-all'], ['gfg-is-all-best']]
    

**Method #2 : Usingaccumulate() + join()**  
This is one-liner approach to this problem. In this, we perform the task of
cutting into cummulative using accumulate and join() is used to construct the
resultant List of lists.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative List Split

# Using accumulate() + join()

from itertools import accumulate

 

# initializing list

test_list = ['gfg-is-all-best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Split char

spl_char = "-"

 

# Cummulative List Split

# Using accumulate() + join()

temp = test_list[0].split(spl_char)

res = list(accumulate(temp, lambda x, y: spl_char.join([x, y])))

 

# printing result 

print("The Cummulative List Splits : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg-is-all-best']
    The Cummulative List Splits : ['gfg', 'gfg-is', 'gfg-is-all', 'gfg-is-all-best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

