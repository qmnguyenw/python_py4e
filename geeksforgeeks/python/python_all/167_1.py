Python | Insert list in another list



The problem of inserting a number at any index is a quite common one. But
sometimes we require to insert the whole list into another list. These kinds
of problems occur in Machine Learning while playing with data. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using insert() \+ loop**  
In this method, we insert one element by 1 at a time using the insert
function. This way we add all the list elements at the specified index in
other list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to insert one list in another

# using insert() + loop

 

# initializing lists 

test_list = [4, 5, 6, 3, 9]

insert_list = [2, 3]

 

# initializing position

pos = 2

 

# printing original list

print ("The original list is : " + str(test_list))

 

# printing insert list 

print ("The list to be inserted is : " + str(insert_list))

 

# using insert() + loop

# to insert one list in another

for i in range(len(insert_list)):

 test_list.insert(i + pos, insert_list[i])

 

# printing result 

print ("The list after insertion is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list to be inserted is : [2, 3]
    The list after insertion is : [4, 5, 2, 3, 6, 3, 9]
    

  
**Method #2 : Using list slicing**  
This is the most pythonic and elegant way to perform this particular task. In
this method, we just slice the list where we need to add the element and
assign the list to be inserted.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to insert one list in another

# using list slicing

 

# initializing lists 

test_list = [4, 5, 6, 3, 9]

insert_list = [2, 3]

 

# initializing position

pos = 2

 

# printing original list

print ("The original list is : " + str(test_list))

 

# printing insert list 

print ("The list to be inserted is : " + str(insert_list))

 

# using list slicing

# to insert one list in another

test_list[pos:pos] = insert_list

 

# printing result 

print ("The list after insertion is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list to be inserted is : [2, 3]
    The list after insertion is : [4, 5, 2, 3, 6, 3, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

