Python | Convert String list to Joined Single element



Sometimes, while working with Python, we can have a problem in which we need
to perform the task of joining each element of String list to a single element
in List by combining using delim. This kind of application can come in web
development domain. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop**  
This is one of way to perform this task. In this, we iterate for the String
list for strings using loop and perform the join operation according to the
delim.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String list to Joined Single element

# Using loop

 

# initializing list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim 

delim = "-"

 

# Convert String list to Joined Single element

# Using loop

res = '' 

for idx in range(len(test_list)-1):

 res = res + test_list[idx] + delim

if len(test_list) > 0:

 res = res + test_list[-1]

res = [res]

 

# printing result 

print("String after performing join : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    String after performing join : ['gfg-is-best']
    

**Method #2 : Using join() \+ list comprehension**  
This task can also be performed using the combination of above functions. In
this, we perform the task of combining using join(). The logic is compiled
using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String list to Joined Single element

# Using join() + list comprehension

 

# initializing list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim 

delim = "-"

 

# Convert String list to Joined Single element

# Using join() + list comprehension

res = [delim.join(test_list)]

 

# printing result 

print("String after performing join : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    String after performing join : ['gfg-is-best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

