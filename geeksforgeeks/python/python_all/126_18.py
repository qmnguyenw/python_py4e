Python | Handling no element found in index()



Sometimes, while working with Python lists, we are confronted with a problem
in which we need to check whether an element is present in a list and also
where exactly, which index it occurs. The convenient solution of it is to use
index(). But problem with this can come that sometimes, the desired element
might not be present in the list. Let’s discuss a method in which this
exception can be handled.

 **Method : UsingValueError + try + except**

In this method, knowing that the value might not exists, we catch the error in
try-except block. The ValueError is raised in the absence and can be used to
catch this particular exception.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Handling no element found in index()

# Using try + except + ValueError

 

# initializing list

test_list = [6, 4, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Handling no element found in index()

# Using try + except + ValueError

try :

 test_list.index(11)

 res = "Element found"

except ValueError :

 res = "Element not in list !"

 

# Printing result

print("The value after catching error : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [6, 4, 8, 9, 10]
    The value after catching error : Element not in list!
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

