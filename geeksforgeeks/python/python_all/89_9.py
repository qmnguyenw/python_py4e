Python – Remove words containing list characters



Sometimes, in the process of data filtering we have a problem in which we need
to remove words which are composite of certain letters. This kind of
application is common in data science domain. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usingall() \+ list comprehension**  
The combination of above methods can be used to perform this task. In this, we
just check for all list characters using all() in each list and filters out
string which has any one of characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove words containing list characters

# using list comprehension + all()

from itertools import groupby

 

# initializing list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# initializing char list 

char_list = ['g', 'o']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# printing character list

print ("The character list is : " + str(char_list))

 

# Remove words containing list characters

# using list comprehension + all()

res = [ele for ele in test_list if all(ch not in ele
for ch in char_list)]

 

# printing result 

print ("The filtered strings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    The character list is : ['g', 'o']
    The filtered strings are : ['is', 'best']
    

**Method #2 : Using loop**  
This is brute method in which this task can be performed. In this we use loop
and conditional statements to perform this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove words containing list characters

# using loop

from itertools import groupby

 

# initializing list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# initializing char list 

char_list = ['g', 'o']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# printing character list

print ("The character list is : " + str(char_list))

 

# Remove words containing list characters

# using loop

res = []

flag = 1

for ele in test_list:

 for idx in char_list:

 if idx not in ele:

 flag = 1

 else:

 flag = 0

 break

 if(flag == 1):

 res.append(ele) 

 

# printing result 

print ("The filtered strings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    The character list is : ['g', 'o']
    The filtered strings are : ['is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

