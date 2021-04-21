Python – Split String of list on K character



Sometimes while working with data, we can have a problem in which we need to
perform split operation on Strings, and sometimes, we might also require to
perform them into nested strings overall. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using loop +split()**  
The combination of above functionalities can be used to perform this task. In
this, we iterate through each list string and perform a manual split and then
add the new elements to that list using extend() using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split String of list on K character

# using loop + split()

 

# Initializing list 

test_list = ['Gfg is best', 'for Geeks', 'Preparing']

 

# printing original list

print("The original list is : " + str(test_list))

 

K = ' '

 

# Split String of list on K character

# using loop + split()

res = []

for ele in test_list:

 sub = ele.split(K)

 res.extend(sub)

 

# printing result 

print ("The extended list after split strings : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg is best', 'for Geeks', 'Preparing']
    The extended list after split strings : ['Gfg', 'is', 'best', 'for', 'Geeks', 'Preparing']
    

**Method #2 : Usingjoin() + split()**  
The combination of above functions can be used to perform this task. In this,
we join split all the elements of list and then join each of them to make it
split by K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split String of list on K character

# using join() + split()

 

# Initializing list 

test_list = ['Gfg is best', 'for Geeks', 'Preparing']

 

# printing original list

print("The original list is : " + str(test_list))

 

K = ' '

 

# Split String of list on K character

# using join() + split()

res = K.join(test_list).split(K)

 

# printing result 

print ("The extended list after split strings : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg is best', 'for Geeks', 'Preparing']
    The extended list after split strings : ['Gfg', 'is', 'best', 'for', 'Geeks', 'Preparing']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

