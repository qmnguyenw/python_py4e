Python – Tuple key detection from value list



Sometimes, while working with record data, we can have a problem in which we
need to extract the key which has matching value of K from its value list.
This kind of problem can occur in domains that are linked to data. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using List comprehension**  
This task can be performed using List comprehension. In this, we iterate
through each records and test it’s value list for K. If found we return that
key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tuple key detection from value list

# using List comprehension

 

# Initializing list

test_list = [('Gfg', [1, 3, 4]), ('is', [5,
8, 10]), ('best', [11, 9, 2])]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 4

 

# Tuple key detection from value list

# using List comprehension

res = [sub[0] for sub in test_list if K in
sub[1]]

 

# printing result 

print ("The required key of list values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Gfg', [1, 3, 4]), ('is', [5, 8, 10]), ('best', [11, 9, 2])]
    The required key of list values : ['Gfg']
    

**Method #2 : Usingfilter() \+ lambda**  
The combination of above functions can also be used to perform this task. In
this, filter() is used to check for existance in list and extract the required
key with help of lambda.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tuple key detection from value list

# using filter() + lambda

 

# Initializing list

test_list = [('Gfg', [1, 3, 4]), ('is', [5,
8, 10]), ('best', [11, 9, 2])]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 4

 

# Tuple key detection from value list

# using filter() + lambda

res = list(filter(lambda sub, ele = K : ele in
sub[1], test_list))

 

# printing result 

print ("The required key of list values : " +
str(res[0][0]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Gfg', [1, 3, 4]), ('is', [5, 8, 10]), ('best', [11, 9, 2])]
    The required key of list values : Gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

