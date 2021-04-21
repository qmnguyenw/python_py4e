Python – Ways to remove multiple empty spaces from string List



Sometimes, while working with Python strings, we have a problem in which we
need to perform the removal of empty spaces in Strings. The problem of
filtering a single space is easier. But sometimes we are unaware of number of
spaces. This has application in many domains. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop +strip()**  
This is a way in which we can perform this task. In this, we strip the strings
using strip(), it reduces to single space and then it can be tested for NULL
value. Returns True if string is single space and hence helps in filtering.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove multiple empty spaces from string List

# Using loop + strip()

 

# initializing list

test_list = ['gfg', ' ', ' ', 'is', ' ', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove multiple empty spaces from string List

# Using loop + strip()

res = []

for ele in test_list:

 if ele.strip():

 res.append(ele)

 

# printing result 

print("List after filtering non-empty strings : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
    List after filtering non-empty strings : ['gfg', 'is', 'best']
    

**Method #2 : Using list comprehension +strip()**  
The combination of above functions can also be used to perform this task. In
this, we employ one-liner approach to perform this task instead of using loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove multiple empty spaces from string List

# Using list comprehension + strip()

 

# initializing list

test_list = ['gfg', ' ', ' ', 'is', ' ', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove multiple empty spaces from string List

# Using list comprehension + strip()

res = [ele for ele in test_list if ele.strip()]

 

# printing result 

print("List after filtering non-empty strings : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
    List after filtering non-empty strings : ['gfg', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

