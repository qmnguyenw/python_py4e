Python – Remove duplicate words from Strings in List



Sometimes, while working with Python list we can have a problem in which we
need to perform removal of duplicated words from string list. This can have
application when we are in data domain. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingset() + split() \+ loop**  
The combination of above methods can be used to perform this task. In this, we
first split each list into combined words and then employ set() to perform the
task of duplicate removal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove duplicate words from Strings in List

# using loop + set() + split()

 

# Initializing list

test_list = ['gfg, best, gfg', 'I, am, I', 'two, two, three'
]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove duplicate words from Strings<code></code> in List

# using loop + set() + split()

res = []

for strs in test_list:

 res.append(set(strs.split(", ")))

 

# printing result 

print ("The list after duplicate words removal is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg, best, gfg', 'I, am, I', 'two, two, three']
    The list after duplicate words removal is : [{'best', 'gfg'}, {'I', 'am'}, {'three', 'two'}]
    

**Method #2 : Using list comprehension +set() + split()**  
This is similar method to above. The difference is that we employ list
comprehension instead of loops to perform the iteration part.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove duplicate words from Strings in List

# using list comprehension + set() + split()

 

# Initializing list

test_list = ['gfg, best, gfg', 'I, am, I', 'two, two, three'
]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove duplicate words from Strings in List

# using list comprehension + set() + split()

res = [set(strs.split(", ")) for strs in test_list]

 

# printing result 

print ("The list after duplicate words removal is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg, best, gfg', 'I, am, I', 'two, two, three']
    The list after duplicate words removal is : [{'best', 'gfg'}, {'I', 'am'}, {'three', 'two'}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

