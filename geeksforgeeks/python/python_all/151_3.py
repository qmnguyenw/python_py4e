Python | Remove matching tuples



The problem of removing the matching elements from two lists and constructing
a new list having just the filtered elements not present in 2nd list has been
discussed earlier, but sometimes, we have more than an elementary element, but
a tuple as element of list. Handling such a case requires different type of
handling. Lets discuss certain ways how this problem can be solved.

 **Method #1 : Using list comprehension**  
This particular task can be done using the list comprehension as shorthand for
the for loop which we would have used. We just check for the existence of one
tuple in another and make decision accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# filter repeated tuple

# using list comprehension

 

# initializing lists 

test_list1 = [('Geeks', 'for'), ('Geeks', 'is'),
('Computer', 'Science')]

test_list2 = [('Geeks', 'for'), ('Geeks', 'is')]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 1 : " + str(test_list2))

 

# using list comprehension

# filter repeated tuple

res = [sub for sub in test_list1 if sub not in
test_list2]

 

# print result

print("The filtered list of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [('Geeks', 'for'), ('Geeks', 'is'), ('Computer', 'Science')]
    The original list 1 : [('Geeks', 'for'), ('Geeks', 'is')]
    The filtered list of tuples : [('Computer', 'Science')]
    

**Method #2 : Using set() + “-” operator**  
The task of getting the difference of two lists can also be done using the set
that converts the list and then minus operator can be used to get the set
difference.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# filter repeated tuple

# using set() + "-" operator

 

# initializing lists 

test_list1 = [('Geeks', 'for'), ('Geeks', 'is'),
('Computer', 'Science')]

test_list2 = [('Geeks', 'for'), ('Geeks', 'is')]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 1 : " + str(test_list2))

 

# using set() + "-" operator

# filter repeated tuple

res = list(set(test_list1) - set(test_list2))

 

# print result

print("The filtered list of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [('Geeks', 'for'), ('Geeks', 'is'), ('Computer', 'Science')]
    The original list 1 : [('Geeks', 'for'), ('Geeks', 'is')]
    The filtered list of tuples : [('Computer', 'Science')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

