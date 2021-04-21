Python | Equidistant element list



Sometimes, while working with Python list we can have a problem in which we
need to construct the list in which the range is auto computed using the
start, end and length parameters. The solution of this problem can have many
applications. Let’s discuss a way in which this task can be performed.

 **Method : Using list comprehension**  
This task can be performed using list comprehension, shorthand for the loop
version of logic. In this, we just compute the range using division
manipulation and extend it to increasing list forming equidistant list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Equidistant element list

# using list comprehension

 

# initializing start value 

strt = 5

 

# initializing end value 

end = 10

 

# initializing length

length = 8

 

# Equidistant element list

# using list comprehension

test_list = [strt + x * (end - strt)/length for x
in range(length)]

 

# Printing result

print("The Equidistant list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The Equidistant list is : [5.0, 5.625, 6.25, 6.875, 7.5, 8.125, 8.75, 9.375]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

