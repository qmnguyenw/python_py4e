Python – Substring concatenation by Separator



Sometimes, while working with Python Lists, we can have problem in which we
need to perform the concatenation of strings in a list till the separator.
This can have application in domains in which we need chunked data. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
perform the task of joining in loop conditional statements and re initialize
string to empty on separator occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring concatenation by Separator

# Using loop

 

# initializing list

test_list = ['gfg', 'is', '*', 'best', '*',
'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = '*'

 

# Substring concatenation by Separator

# Using loop

res = []

temp = ''

for sub in test_list:

 if sub != '*':

 temp += sub

 else:

 res.append(temp)

 temp = ''

if temp:

 res.append(temp)

 

# printing result 

print("The list after String concatenation : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', '*', 'best', '*', 'for', 'geeks']
    The list after String concatenation : ['gfgis', 'best', 'forgeeks']
    

**Method #2 : Usingjoin() + split() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we perform the task of concatenation using join(). The list construction is
done using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring concatenation by Separator

# Using join() + split() + list comprehension

 

# initializing list

test_list = ['gfg', 'is', '*', 'best', '*',
'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = '*'

 

# Substring concatenation by Separator

# Using join() + split() + list comprehension

res = [ele for ele in ''.join(test_list).split(K) if ele]

 

# printing result 

print("The list after String concatenation : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['gfg', 'is', '*', 'best', '*', 'for', 'geeks']
    The list after String concatenation : ['gfgis', 'best', 'forgeeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

