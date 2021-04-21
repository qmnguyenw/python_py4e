Python | Index minimum value Record



In python we can bind a structural information in form of tuples and then can
retrieve the same and has manyfold application. But sometimes we require the
information of tuple corresponding to minimum value of other tuple index. This
functionality has many applications such as ranking. Lets discuss certain ways
in which this can be achieved.

 **Method #1 : Usingmin() + operator.itemgetter()**  
We can get the minimum of corresponding tuple index from a list using the key
itemgetter index provided and then mention the index information required
using index specification at the end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Index minimum value Record

# using min() + itemgetter()

from operator import itemgetter

 

# initializing list 

test_list = [('Rash', 143), ('Manjeet', 200),
('Varsha', 100)]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using min() + itemgetter()

# Index minimum value Record

res = min(test_list, key = itemgetter(1))[0]

 

# printing result

print ("The name with minimum score is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
    The name with minimum score is : Varsha
    

**Method #2 : Usingmin() \+ lambda**  
This method is almost similar to the method discussed above, just the
difference is the specification and processing of target tuple index for
minimum is done by lambda function. This improved readability of code.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Index minimum value Record

# using min() + lambda

 

# initializing list 

test_list = [('Rash', 143), ('Manjeet', 200),
('Varsha', 100)]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using min() + lambda

# Index minimum value Record

res = min(test_list, key = lambda i : i[1])[0]

 

# printing result

print ("The name with minimum score is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
    The name with minimum score is : Varsha
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

