Python – Convert Strings to Character Matrix



Sometimes, while dealing with String lists, we can have a problem in which we
need to convert the Strings in list to separate character list. Overall
converting into Matrix. This can have multiple applications in data science
domain in which we deal with lots of data. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using List comprehension**  
This is one way in which this task can be performed. In this, we convert the
string to list of characters using list() and convert the result to desired
matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Convert Strings to Character Matrix

# using List comprehension

 

# Initializing list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Strings to Character Matrix

# using List comprehension

res = [list(sub) for sub in test_list]

 

# printing result 

print ("List String after conversion to Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘gfg’, ‘is’, ‘best’]  
> List String after conversion to Matrix : [[‘g’, ‘f’, ‘g’], [‘i’, ‘s’], [‘b’,
> ‘e’, ‘s’, ‘t’]]

  

  

**Method #2 : Usingloop + list()**  
This is brute force way to perform this task. In this, we run loop and and
convert each string to character list using list().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Convert Strings to Character Matrix

# using loop + list()

 

# Initializing list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Strings to Character Matrix

# using loop + list()

res = []

for sub in test_list:

 res.append(list(sub))

 

# printing result 

print ("List String after conversion to Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘gfg’, ‘is’, ‘best’]  
> List String after conversion to Matrix : [[‘g’, ‘f’, ‘g’], [‘i’, ‘s’], [‘b’,
> ‘e’, ‘s’, ‘t’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

