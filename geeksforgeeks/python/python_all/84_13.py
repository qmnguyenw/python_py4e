Python – Prefix frequency in string List



Sometimes, while working with Python lists, we can have a problem in which we
need to get the count of strings that start with particular substring. This
can have an application in web development and general programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +startswith()**  
The combination of above functions can be used to perform this task. In this,
we run a loop for each string in list and employ startswith() to get the
strings that start with particular prefix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix frequency in List

# using loop + startswith()

 

# Initializing list

test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS',
'Gcourses']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing substring

test_sub = 'gfg'

 

# Prefix frequency in List

# using loop + startswith()

res = 0

for ele in test_list:

 if ele.startswith(test_sub):

 res = res + 1

 

# printing result 

print ("Strings count with matching frequency : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘gfgisbest’, ‘geeks’, ‘gfgfreak’, ‘gfgCS’,
> ‘Gcourses’]  
> Strings count with matching frequency : 3

  

  

**Method #2 : Usingsum() + startswith()**  
The combination of above functions can be used to perform this task. In this,
we perform the task of counting using sum() and startswith(), is used to
perform task of checking of prefix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix frequency in List

# using sum() + startswith()

 

# Initializing list

test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS',
'Gcourses']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing substring

test_sub = 'gfg'

 

# Prefix frequency in List

# using sum() + startswith()

res = sum(sub.startswith(test_sub) for sub in test_list)

 

# printing result 

print ("Strings count with matching frequency : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘gfgisbest’, ‘geeks’, ‘gfgfreak’, ‘gfgCS’,
> ‘Gcourses’]  
> Strings count with matching frequency : 3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

