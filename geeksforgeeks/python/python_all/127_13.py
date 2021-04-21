Python | Decimal step range in list



Sometimes, while working with Python list we can have a problem in which we
require to populate the list in a range of decimal. Integral ranges are easier
to handle using inbuilt constructs, but having a decimal value to provide to
range value doesn’t work. Let’s discuss a way in which this problem can be
solved.

 **Method : Using list comprehension**  
One way to solve this problem is by using the list comprehension which can
solve this problem in easier way by iterating the list and multiplying the
range element to the index of element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Decimal step range in list

# using list comprehension

 

# initializing start value 

strt = 5

 

# initializing step value 

step = 0.4

 

# using list comprehension

# Decimal step range 

test_list = [strt + (x * step) for x in range(0,
5)]

 

# Printing result

print("The list after decimal range value initialization : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The list after decimal range value initialization : [5.0, 5.4, 5.8, 6.2, 6.6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

