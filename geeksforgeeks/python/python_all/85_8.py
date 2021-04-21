Python – List Strings frequency in Matrix



Sometimes, while working with Matrix, we can have a problem in which we need
to check frequency of argument Strings from List in each row of Matrix. This
is very peculiar problem and can have usefulness in many domains. Lets discuss
certain ways in which this task can be solved.

 **Method #1 : Usingcount() \+ loop**  
The combination of above functionalities can be used to perform this task. In
this we count the frequency using count() and task of iteration is performed
inside the loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# List Strings frequency in Matrix

# using count() + loop

 

# Initializing lists

test_list1 = [['Gfg', 'is', 'best'], ['Gfg', 'is',
'for', 'CS'], ['Gfg', 'is', 'for', 'Geeks']]

test_list2 = ['Gfg', 'is', 'best']

 

# printing original list1

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# List Strings frequency in Matrix

# using count() + loop

res = []

for val in test_list1:

 res.append([val.count(ele) for ele in test_list2])

 

# printing result 

print ("Frequency of strings in Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [['Gfg', 'is', 'best'], ['Gfg', 'is', 'for', 'CS'], ['Gfg', 'is', 'for', 'Geeks']]
    The original list 2 is : ['Gfg', 'is', 'best']
    Frequency of strings in Matrix : [[1, 1, 1], [1, 1, 0], [1, 1, 0]]
    

**Method #2 : Using list comprehension**  
This is yet another way in which this task can be performed. This is shortened
version of above method in one liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# List Strings frequency in Matrix

# using list comprehension

 

# Initializing lists

test_list1 = [['Gfg', 'is', 'best'], ['Gfg', 'is',
'for', 'CS'], ['Gfg', 'is', 'for', 'Geeks']]

test_list2 = ['Gfg', 'is', 'best']

 

# printing original list1

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# List Strings frequency in Matrix

# using list comprehension

res = [[sub.count(ele) for ele in test_list2] for sub in
test_list1]

 

# printing result 

print ("Frequency of strings in Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [['Gfg', 'is', 'best'], ['Gfg', 'is', 'for', 'CS'], ['Gfg', 'is', 'for', 'Geeks']]
    The original list 2 is : ['Gfg', 'is', 'best']
    Frequency of strings in Matrix : [[1, 1, 1], [1, 1, 0], [1, 1, 0]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

