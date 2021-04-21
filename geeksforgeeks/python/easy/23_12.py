Python Set | difference_update()



The difference_update() method helps in an in-place way of differentiating the
set. The previously discussed set difference() helps to find out the
difference between two sets and returns a new set with the difference value,
but the difference_update() updates the existing caller set.

If A and B are two sets. The set difference() method will get the (A – B) and
will return a new set. The set difference_update() method modifies the
existing set. If (A – B) is performed, then A gets modified into (A – B), and
if (B – A) is performed, then B gets modfied into (B – A).

 **Syntax:**

    
    
    **A.difference_update(B)** for (A - B)
    **B.difference_update(A)** for (B - A)
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/difference_update-1.png)

The function **returns _None_** and changes the value of the existing set.  
In this example, we will get the difference between two sets and show how the
difference_update works.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to get the difference between two sets

# using difference_update() between set A and set B

 

# Driver Code

A = {10, 20, 30, 40, 80}

B = {100, 30, 80, 40, 60}

 

# Modifies A and returns None

A.difference_update(B)

 

# Prints the modified set

print (A)  
  
---  
  
 __

 __

Output:

    
    
    {20, 10}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

