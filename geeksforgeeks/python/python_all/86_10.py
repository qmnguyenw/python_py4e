Python – Remove Record if Nth Column is K



Sometimes while working with list of records, we can have a problem in which
we need to perform removal of records on the basis of presence of certain
element at Nth position of record. Lets discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop**  
This is brute force method in which this task can be performed. In this, we
iterate for each element in list and exclude it if its Nth column is equal to
K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove Record if Nth Column is K

# using loop

 

# Initializing list

test_list = [(5, 7), (6, 7, 8), (7, 8,
10), (7, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 7

 

# Initializing N 

N = 1

 

# Remove Record if Nth Column is K

# using loop

res = []

for sub in test_list:

 if (sub[N] != K):

 res.append(sub)

 

# printing result 

print ("List after removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 7), (6, 7, 8), (7, 8, 10), (7, 1)]
    List after removal : [(7, 8, 10), (7, 1)]
    

**Method #2 : Using list comprehension**  
This is yet another way in which this task can be performed. In this, we
perform this task in similar way as above but in one liner form.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove Record if Nth Column is K

# using list comprehension

 

# Initializing list

test_list = [(5, 7), (6, 7, 8), (7, 8,
10), (7, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 7

 

# Initializing N 

N = 1

 

# Remove Record if Nth Column is K

# using list comprehension

res = [sub for sub in test_list if sub[N] != K]

 

# printing result 

print ("List after removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 7), (6, 7, 8), (7, 8, 10), (7, 1)]
    List after removal : [(7, 8, 10), (7, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

