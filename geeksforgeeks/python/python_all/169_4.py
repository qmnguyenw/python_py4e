Python | Test for False list



Sometimes, we need to check if a list is completely True of False, these
occurrences come more often in testing purposes after the development phase.
Hence, having a knowledge of all this is necessary and useful. Lets discuss
certain ways in which this can be performed.

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

# to check for False list 

# using naive method

 

# initializing list 

test_list = [False, False, False, False]

 

# printing original list

print ("The original list is : " + str(test_list))

 

flag = 0

 

# using naive method 

# to check for False list 

for i in test_list :

 if i == True :

 flag = 1

 break

 

# printing result

print ("Is List completely false ? : " + str(bool(not
flag)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [False, False, False, False]
    Is List completely false ? : True
    

  
**Method #2 : Usingall()**  
This function tests each value to be False and if yes, returns boolean True,
else returns false. The list iteration is done using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to check for False list 

# using all()

 

# initializing list 

test_list = [False, False, False, False]

 

# printing original list

print ("The original list is : " + str(test_list))

 

flag = 0

 

# using all()

# to check for False list 

res = all(not i for i in test_list)

 

# printing result

print ("Is List completely false ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [False, False, False, False]
    Is List completely false ? : True
    

