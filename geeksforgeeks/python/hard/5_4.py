Difference Between x = x + y and x += y in Python



We often use **x += y** instead of **x = x + y**. So, are they same or
different? Let’s Find it here.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

x= [1, 2]

another_x = x

y = [3]

 

x += y

 

print(x)

print(another_x)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 3]
    [1, 2, 3]

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

x= [1, 2]

another_x = x

y = [3]

 

x = x + y

 

print(x)

print(another_x)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [1, 2, 3]
    [1, 2]

So here we find that both codes are almost similar but still there are
difference in the outputs. So the reason behind this is that for many types of
objects, x += y will modify the object referred to by x in-place, whereas
x = x + y will create a new object and reassign x to it. This distinction
is important if you still have another reference to the object somewhere like
in this case another_a is another reference to the object.

However, many objects such as numbers and strings are “immutable” – they can’t
be modified in-place – and for those objects, x += y and x = x + y will
typically do exactly the same thing. But if you write your own class you can
customize what + and += do when used with objects of that class, and you
can make them do completely different things if you really want to.

 **Example 3:**

 __

 __  
 __

 __

 __  
 __  
 __

x= "12345"

another_x = x

y = "67890"

 

x += y

 

print(x)

print(another_x)  
  
---  
  
 __

 __

 **Output:**

    
    
    1234567890
    12345

 **Example 4:**

 __

 __  
 __

 __

 __  
 __  
 __

x= "12345"

another_x = x

y = "67890"

 

x = x + y

 

print(x)

print(another_x)  
  
---  
  
 __

 __

 **Output:**

    
    
    1234567890
    12345

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

