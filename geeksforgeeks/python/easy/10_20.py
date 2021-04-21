Python | Convert mixed data types tuple list to string list



Sometimes, while working with records, we can have a problem in which we need
to perform type conversion of all records into a specific format to string.
This kind of problem can occur in many domains. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using list comprehension +tuple() + str() \+ generator
expression**  
The combination of above functions can be used to perform this task. In this,
we extract each tuple element using generation expression and perform the
conversion using str(). The iteration to each tuple is done by list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple mixed list to string list

# using list comprehension + tuple() + str() + generator expression

 

# initialize list 

test_list = [('gfg', 1, True), ('is', False),
('best', 2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert tuple mixed list to string list

# using list comprehension + tuple() + str() + generator expression

res = [tuple(str(ele) for ele in sub) for sub in
test_list]

 

# printing result

print("The tuple list after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('gfg', 1, True), ('is', False), ('best', 2)]
    The tuple list after conversion : [('gfg', '1', 'True'), ('is', 'False'), ('best', '2')]
    

**Method #2 : Usingmap() + tuple() + str() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we perform the task performed by generator expression above using map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple mixed list to string list

# using map() + tuple() + str() + list comprehension

 

# initialize list 

test_list = [('gfg', 1, True), ('is', False),
('best', 2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert tuple mixed list to string list

# using map() + tuple() + str() + list comprehension

res = [tuple(map(str, sub)) for sub in test_list]

 

# printing result

print("The tuple list after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('gfg', 1, True), ('is', False), ('best', 2)]
    The tuple list after conversion : [('gfg', '1', 'True'), ('is', 'False'), ('best', '2')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

