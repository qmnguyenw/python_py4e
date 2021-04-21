Python | Unpack whole list into variables



Sometimes, while working with list, we can have a wish to have each of element
of list to be converted or unpacked into required variables. This problem can
occur in web development domain. Let’s discuss certain ways in which this
problem can be solved.

 **Method #1 : Using"=" operator**  
This task can be performed using a “=” operator. In this we just ensure enough
variables as the count of list elements and assign them to list, the list
elements get allotted to variables in order of their assignment.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unpack whole list into variables

# using "=" operator

 

# initialize list

test_list = [1, 3, 7, 4, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Unpack whole list into variables

# using "=" operator

one, two, three, four, five = test_list

 

# printing result

print("Variables as assigned are : " + str(one) + " "

 + str(two) + " "

 + str(three) + " "

 + str(four) + " "

 + str(five))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 7, 4, 2]
    Variables as assigned are : 1 3 7 4 2
    

**Method #2 : Using Namedtuple**  
This problem can be solved using a namedtuple, which can store the list
elements with a variable name that can be accessed by using a dot operator
succeeding with name of variable initialized.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unpack whole list into variables

# using Namedtuple

from collections import namedtuple

 

# initialize list

test_list = [1, 3, 7, 4, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Unpack whole list into variables

# using Namedtuple

temp = namedtuple("temp", "one two three four five")

res = temp(*test_list)

 

# printing result

print("Variables as assigned are : " + str(res.one) + " "

 + str(res.two) + " "

 + str(res.three) + " "

 + str(res.four) + " "

 + str(res.five))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 7, 4, 2]
    Variables as assigned are : 1 3 7 4 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

