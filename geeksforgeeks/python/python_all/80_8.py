Python | Remove List elements containing given String character



Sometimes, while working with Python lists, we can have problem in which we
need to perform the task of removing all the elements of list which contain at
least one character of String. This can have application in day-day
programming. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate for all list elements and check for occurrence of any character using
loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove List elements containing String character

# Using loop

 

# initializing list

test_list = ['567', '840', '649', '7342']

 

# initializing string 

test_str = '1237'

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove List elements containing String character

# Using loop

res = []

for sub in test_list:

 flag = 0

 for ele in sub:

 if ele in test_str:

 flag = 1

 if not flag:

 res.append(sub)

 

# printing result 

print("The list after removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['567', '840', '649', '7342']
    The list after removal : ['840', '649']
    

**Method #2 : Using list comprehension**  
This is another way to perform this task. This is similar to above method. In
this we perform the task in similar way as above just as one liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove List elements containing String character

# Using list comprehension

 

def check_pres(sub, test_str):

 for ele in sub:

 if ele in test_str:

 return 0

 return 1

 

# initializing list

test_list = ['567', '840', '649', '7342']

 

# initializing string 

test_str = '1237'

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove List elements containing String character

# Using list comprehension

res = [ele for ele in test_list if check_pres(ele,
test_str)]

 

# printing result 

print("The list after removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['567', '840', '649', '7342']
    The list after removal : ['840', '649']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

