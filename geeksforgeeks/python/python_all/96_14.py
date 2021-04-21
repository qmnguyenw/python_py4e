Python | Merge Range Characters in List



Sometimes, we require to merge some of the elements as single element in the
list. This is usually with the cases with character to string conversion. This
type of task is usually required in development domain to merge the names into
one element. Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingjoin() \+ List Slicing**  
The join function can be coupled with list slicing which can perform the task
of joining each character in a range picked by the list slicing functionality.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Merge Range Characters in List

# using join() + list slicing

 

# initializing list 

test_list = ['I', 'L', 'O', 'V', 'E', 'G',
'F', 'G']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing Range, i, j

i, j = 3, 7

 

# using join() + list slicing

# Merge Range Characters in List

test_list[i : j] = [''.join(test_list[i : j])]

 

# printing result 

print ("The list after merging elements : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['I', 'L', 'O', 'V', 'E', 'G', 'F', 'G']
    The list after merging elements : ['I', 'L', 'O', 'VEGF', 'G']
    

**Method #2 : Usingreduce() \+ lambda + list slicing**  
The task of joining each element in a range is performed by reduce function
and lambda. reduce function performs the task for each element in the range
which is defined by the lambda function. It works with Python2 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Merge Range Characters in List

# using reduce() + lambda + list slicing

 

# initializing list 

test_list = ['I', 'L', 'O', 'V', 'E', 'G',
'F', 'G']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing strt, end 

strt, end = 3, 7

 

# using reduce() + lambda + list slicing

# Merge Range Characters in List

test_list[strt : end] = [reduce(lambda i, j: i + j,
test_list[strt : end])]

 

# printing result 

print ("The list after merging elements : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['I', 'L', 'O', 'V', 'E', 'G', 'F', 'G']
    The list after merging elements : ['I', 'L', 'O', 'VEGF', 'G']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

