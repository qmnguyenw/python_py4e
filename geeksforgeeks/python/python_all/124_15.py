Python | Convert string list into multiple cases



Sometimes, while working with Python strings, we might have a problem in which
we have list of strings and we wish convert them into specified cases. This
problem generally occurs in the cases in which the strings we recieve are ill-
cased. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension + inbuilt functions**  
In this method, we use list comprehension as shortened way to perform this
task rather than loop method that could span some lines of codes. The
conversions are made using generic inbuilt functions that can perform
interconversion tasks.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert string list into multiple cases

# Using inbuilt functions + list comprehension

 

# Initializing list

test_list = ['bLue', 'ReD', 'yeLLoW']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert string list into multiple cases

# Using inbuilt functions + list comprehension

res = [(ele.upper(), ele.title(), ele.lower()) for ele in
test_list]

 

# printing result

print("The list with multiple cases are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['bLue', 'ReD', 'yeLLoW']
    The list with multiple cases are : [('BLUE', 'Blue', 'blue'), ('RED', 'Red', 'red'), ('YELLOW', 'Yellow', 'yellow')]
    

**Method #2 : Usingmap() \+ lambda + inbuilt functions**  
This is another method to perform this particular task. In this, we just
perform the task of extending the logic of conversions using lambda and
iterations and application to each string is done by lambda function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert string list into multiple cases

# Using map() + lambda + inbuilt functions

 

# Initializing list

test_list = ['bLue', 'ReD', 'yeLLoW']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert string list into multiple cases

# Using map() + lambda + inbuilt functions

res = list(map(lambda ele: (ele.upper(), ele.title(),
ele.lower()), test_list))

 

# printing result

print("The list with multiple cases are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['bLue', 'ReD', 'yeLLoW']
    The list with multiple cases are : [('BLUE', 'Blue', 'blue'), ('RED', 'Red', 'red'), ('YELLOW', 'Yellow', 'yellow')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

