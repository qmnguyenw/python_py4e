Python – Summation after elements removal



Sometimes we need to perform the operation of removing all the items from the
lists that are present in other list, i.e we are given some of the invalid
numbers in one list which needs to be get ridden from the original list and
perform its summation. Lets discuss various ways in which this can be
performed.

 **Method #1 : Using list comprehension + sum()**  
The list comprehension can be used to perform the naive method in just the one
line and hence gives an easy method to perform this particular task. The task
of performing summation is done using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Summation after elements removal

# using list comprehension + sum()

 

# initializing list 

test_list = [1, 3, 4, 6, 7, 6]

 

# initializing remove list 

remove_list = [3, 6]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing remove list 

print ("The remove list is : " + str(remove_list))

 

# using list comprehension + sum() to perform task

res = sum([i for i in test_list if i not in
remove_list])

 

# printing result

print ("The list after performing removal summation is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 4, 6, 7, 6]
    The remove list is : [3, 6]
    The list after performing removal summation is : 12
    

**Method #2 : Usingfilter() + lambda + sum()**  
The filter function can be used along with lambda to perform this task and
creating a new filtered list of all the elements that are not present in the
remove element list. The task of performing summation is done using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Summation after elements removal

# using filter() + lambda + sum()

 

# initializing list 

test_list = [1, 3, 4, 6, 7]

 

# initializing remove list 

remove_list = [3, 6]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing remove list 

print ("The remove list is : " + str(remove_list))

 

# using filter() + lambda + sum() to perform task

res = sum(filter(lambda i: i not in remove_list,
test_list))

 

# printing result

print ("The list after performing removal summation is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 4, 6, 7, 6]
    The remove list is : [3, 6]
    The list after performing removal summation is : 12
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

