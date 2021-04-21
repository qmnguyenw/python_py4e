Python | Ways to sort a zipped list by values



Zipped lists are those lists where several lists are mapped together to form
one list which can be used as one entity altogether. In Python Zip()
function is used to map different lists.

Let’s discuss a few methods to demonstrate the problem.

 **Method #1:** Using lambda and sort

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort zipped list by values

# using lambda and sorted

 

# Declaring initial lists

list1 = ['geeks', 'for', 'Geeks']

list2 = [3, 2, 1]

zipped = zip(list1, list2)

 

# Converting to list

zipped = list(zipped)

 

# Printing zipped list

print("Initial zipped list - ", str(zipped))

 

# Using sorted and lambda

res = sorted(zipped, key = lambda x: x[1])

 

# printing result

print("final list - ", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial zipped list -  [('geeks', 3), ('for', 2), ('Geeks', 1)]
    final list -  [('Geeks', 1), ('for', 2), ('geeks', 3)]
    

  
**Method #2:** Using operator and sort

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort zipped list by values

# using operator and sorted

 

import operator

# Declaring initial lists

list1 = ['akshat', 'Manjeet', 'nikhil']

list2 = [3, 2, 1]

zipped = zip(list1, list2)

 

# Converting to list

zipped = list(zipped)

 

# Printing zipped list

print("Initial zipped list - ", str(zipped))

 

# Using sorted and operator

res = sorted(zipped, key = operator.itemgetter(1))

 

# printing result

print("final list - ", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial zipped list -  [('akshat', 3), ('Manjeet', 2), ('nikhil', 1)]
    final list -  [('nikhil', 1), ('Manjeet', 2), ('akshat', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

