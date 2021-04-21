Python – Specific case change in String List



While working with String lists, the problem of cases is common, but
sometimes, we are concerned about changes cases in strings selectively. i.e on
basis of other list. This can have application in day-day programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +upper() + enumerate()**  
This is one of the ways in which this task can be performed. In this we run a
loop for each element and the compare strings, if found equal, then cases of
those lists don’t change and rest strings cases are changed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Specific case change in String List

# using loop + upper() + enumerate() 

 

# Initializing lists

test_list1 = ['GFG', 'IS', 'BEST', 'FOR', 'GEEKS']

test_list2 = ['Gfg', 'Best']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Specific case change in String List

# using loop + upper() + enumerate() 

for idx, ele in enumerate(test_list1):

 for ele2 in test_list2:

 if ele == ele2.upper():

 test_list1[idx] = ele2

 

# printing result 

print ("The string list after case change is : " +
str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['GFG', 'IS', 'BEST', 'FOR', 'GEEKS']
    The original list 2 is : ['Gfg', 'Best']
    The string list after case change is : ['Gfg', 'IS', 'Best', 'FOR', 'GEEKS']
    

**Method #2 : Using loop +capitalize()**  
This method performs similar to above one, the difference being that instead
of upper(), capitalize() is used to perform the task of changing cases.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Specific case change in String List

# using loop + capitalize()

 

# Initializing lists

test_list1 = ['GFG', 'IS', 'BEST', 'FOR', 'GEEKS']

test_list2 = ['Gfg', 'Best']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Specific case change in String List

# using loop + capitalize()

for idx, ele in enumerate(test_list1):

 if ele.capitalize() in test_list2:

 test_list1[idx] = ele.capitalize()

 

# printing result 

print ("The string list after case change is : " +
str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['GFG', 'IS', 'BEST', 'FOR', 'GEEKS']
    The original list 2 is : ['Gfg', 'Best']
    The string list after case change is : ['Gfg', 'IS', 'Best', 'FOR', 'GEEKS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

