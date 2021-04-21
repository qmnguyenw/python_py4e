Python – Count Strings with substring String List



The classical problem that can be handled quite easily by python and has been
also dealt with many times is finding if a a string is substring of other. But
sometimes, one wishes to extend this on list of strings and find how many
strings satisfy condition, and hence then requires to traverse the entire
container and perform the generic algorithm. Lets discuss certain ways to
perform this task.

 **Method #1 : Using list comprehension + len()**  
List comprehension is an elegant ways to perform any particular task as it
increases readability in a long run. This task can be performed using naive
method and hence can be reduced to list comprehension as well. The len() is
used to compute length of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Count Strings with substring String List

# using list comprehension + len()

 

# initializing list 

test_list = ['GeeksforGeeks', 'Geeky', 'Computers',
'Algorithms']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing substring

subs = 'Geek'

 

# using list comprehension + len()

# Count Strings with substring String List

res = len([i for i in test_list if subs in i])

 

# printing result 

print ("All strings count with given substring are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
    All strings count with given substring are : 2
    

**Method #2 : Usingfilter() + lambda + len()**  
This function can also perform this task of finding the strings with the help
of lambda. It just filters out all the strings matching the particular
substring and then adds it in a new list. The len() is used to compute length
of list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Count Strings with substring String List

# using filter() + lambda + len()

 

# initializing list 

test_list = ['GeeksforGeeks', 'Geeky', 'Computers',
'Algorithms']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing substring

subs = 'Geek'

 

# using filter() + lambda + len()

# Count Strings with substring String List

res = len(list(filter(lambda x: subs in x,
test_list)))

 

# printing result 

print ("All strings count with given substring are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
    All strings count with given substring are : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

