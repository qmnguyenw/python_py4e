Python – Remove characters till K element



Sometimes, while working with Python, we can have problem in which we need to
get all elements in list occurring after particular character in list. This
kind of problem can have application in data domains and web development. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force method in which this task can be performed. In this, we
iterate the loop till we find K and then start appending characters, seeming
like removing the elements before K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove characters till K element

# using loop

 

# Initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 'best'

 

# Remove characters till K element

# using loop

res = []

flag = 0

for ele in test_list:

 if ele == K:

 flag = 1

 continue

 if flag:

 res.append(ele)

 

# printing result 

print ("List elements after removing all before K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    List elements after removing all before K : ['for', 'geeks']
    

**Method #2 : Usingindex() \+ list comprehension**  
This is yet another way in which this task can be performed. In this, we first
find the index of element and then use list comprehension + enumerate() to
append only elements after that K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove characters till K element

# using list comprehension + enumerate() + index()

 

# Initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 'best'

 

# Remove characters till K element

# using list comprehension + enumerate() + index()

temp = test_list.index(K)

res = [ele for idx, ele in enumerate(test_list) if idx >
temp]

 

# printing result 

print ("List elements after removing all before K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    List elements after removing all before K : ['for', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

