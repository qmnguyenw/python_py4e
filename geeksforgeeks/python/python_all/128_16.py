Python | Splitting string list by strings



Sometimes, while working with Python strings, we might have a problem in which
we need to perform a split on a string. But we can have a more complex problem
of having a front and rear string and need to perform a split on them. This
can be multiple pairs for split. Let’s discuss certain way to solve this
particular problem.

 **Method : Using loop +index() \+ list slicing**  
This task can be performed by using the above functionalities together. In
this, we just loop along the pairs and get the desired indices using
index(). Then list slicing is done to construct a new list of the desired
slice and appended to form a new resultant list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Splitting string list by strings

# using loop + index() + list slicing

 

# initialize list

test_list = ['gfg', 'is', 'best', "for", 'CS',
'and', 'Maths' ]

 

# initialize split list

split_list = [('gfg', 'best'), ('CS', 'Maths')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# printing split list 

print("The split list is : " + str(split_list))

 

# Splitting string list by strings

# using loop + index() + list slicing

for start, end in split_list:

 temp1 = test_list.index(start)

 temp2 = test_list.index(end) + 1

 test_list[temp1 : temp2] = [test_list[temp1 : temp2]]

 

# printing result

print("The resultant split list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'CS', 'and', 'Maths']
    The split list is : [('gfg', 'best'), ('CS', 'Maths')]
    The resultant split list is : [['gfg', 'is', 'best'], 'for', ['CS', 'and', 'Maths']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

