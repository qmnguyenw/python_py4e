Python | Segregate list elements by Suffix



Sometimes, we need to filter the list with the last character of each string
in the list. This type of task has many applications in day-day programming
and even in the competitive programming domain. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using list comprehension +endswith()**

In this method, we use list comprehension for traversal logic and the endswith
method to filter out all the strings that end with a particular letter. The
left strings can be used to make a different list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Segregating by Suffix

# Using list comprehension + endwith()

 

# initializing list

test_list = ['apple', 'oranges', 'mango', 'grapes']

 

# initializing end Suffix

end_letter = 's'

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + endwith()

# Segregating by Suffix

with_s = [x for x in test_list if x.endswith(end_letter)]

without_s = [x for x in test_list if x not in with_s]

 

# print result

print("The list without suffix s : " + str(without_s))

print("The list with suffix s : " + str(with_s))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['apple', 'oranges', 'mango', 'grapes']
    The list without suffix s : ['apple', 'mango']
    The list with suffix s : ['oranges', 'grapes']
    

  

  

**Method #2 : Usingfilter() \+ lambda + endwith()**

This task can be performed using the filter function with performs the similar
task internally as the above function and lambda is helper function to build
the logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Segregating by Suffix

# Using filter() + endwith() + lambda

 

# initializing list

test_list = ['apple', 'oranges', 'mango', 'grapes']

 

# initializing end Suffix

end_letter = 's'

 

# printing original list

print("The original list : " + str(test_list))

 

# using filter() + endwith() + lambda

# Segregating by Suffix

with_s = list(filter(lambda x: x.endswith(end_letter),
test_list))

without_s = list(filter(lambda x: not
x.endswith(end_letter), test_list))

 

# print result

print("The list without suffix s : " + str(without_s))

print("The list with suffix s : " + str(with_s))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['apple', 'oranges', 'mango', 'grapes']
    The list without suffix s : ['apple', 'mango']
    The list with suffix s : ['oranges', 'grapes']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

