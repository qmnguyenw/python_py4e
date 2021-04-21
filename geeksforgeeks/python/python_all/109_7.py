Python – Test if a list is completely True



Sometimes, we need to check if a list is completely True, these occurrences
come more often in testing purposes after the development phase. Hence, having
a knowledge of all this is necessary and useful. Lets discuss certain ways in
which this can be performed.

 **Method #1 : Naive Method**  
In the naive method, we just run a loop from beg to end of list and check
manually for each value. This is the most basic way to perform this particular
task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pure List Test

# using naive method

 

# initializing list 

test_list = [True, True, True, True]

 

# printing original list

print ("The original list is : " + str(test_list))

 

flag = 0

 

# using naive method 

# Pure List Test

for i in test_list :

 if not i :

 flag = 1

 break

 

# printing result

print ("Is List completely True ? : " + str(bool(not
flag)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [True, True, True, True]
    Is List completely True ? : True
    

**Method #2 : Usingall()**  
This function tests each value to be True and if yes, returns boolean True,
else returns false. The list iteration is done using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pure List Test

# using all()

 

# initializing list 

test_list = [True, True, True, True]

 

# printing original list

print ("The original list is : " + str(test_list))

 

flag = 0

 

# using all()

# Pure List Test 

res = all(i for i in test_list)

 

# printing result

print ("Is List completely True ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [True, True, True, True]
    Is List completely True ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

