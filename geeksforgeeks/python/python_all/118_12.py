Python | Alternate Sort in String list



Sometimes, while working with Python list, we can have a problem in which we
need to perform sorting only of alternatively in list. This kind of
application can come many times. Let’s discuss certain way in which this task
can be performed.

 **Method : Usingjoin() + enumerate() \+ generator expression + sorted()**  
This task can be achieved by using combination of functionalities above. In
this, we perform the sort using just %2 elements in String list. The extension
of this operation to entire list is performed by generator expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate Sort String list 

# using join() + enumerate() + generator expression + sorted()

 

# initialize list 

test_list = ['cdab', 'gfeh', 'kjil']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Alternate Sort String list 

# using join() + enumerate() + generator expression + sorted()

res = ["".join(sorted(j, reverse = i % 2)) for i, j
in enumerate(test_list)] 

 

# printing result

print("The String list after alternate sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['cdab', 'gfeh', 'kjil']
    The String list after alternate sorting : ['abcd', 'hgfe', 'ijkl']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

