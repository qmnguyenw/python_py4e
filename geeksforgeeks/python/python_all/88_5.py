Python – Swap elements in String list



Sometimes, while working with data records we can have a problem in which we
need to perform certain swap operation in which we need to change one element
with other over entire string list. This has application in both day-day and
data Science domain. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingreplace() \+ list comprehension**  
The combination of above functionalities can be used to perform this task. In
this, we iterate through list using list comprehension and task of swapping is
performed using replace().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Swap elements in String list

# using replace() + list comprehension

 

# Initializing list

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

 

# printing original lists

print("The original list is : " + str(test_list))

 

# Swap elements in String list

# using replace() + list comprehension

res = [sub.replace('G', '-').replace('e',
'G').replace('-', 'e') for sub in test_list]

 

# printing result 

print ("List after performing character swaps : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
    List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
    

**Method #2 : Usingjoin() + replace() + split()**  
The combination of above methods can also be used to perform this task. In
this, the task of replace is same, but we use join() and split() with same
parameter to perform task of list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Swap elements in String list

# using replace() + join() + split()

 

# Initializing list

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

 

# printing original lists

print("The original list is : " + str(test_list))

 

# Swap elements in String list

# using replace() + join() + split()

res = ", ".join(test_list)

res = res.replace("G", "_").replace("e",
"G").replace("_", "e").split(', ')

 

# printing result 

print ("List after performing character swaps : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
    List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

