Python | Initialize dictionary with None values



Sometimes, while working with dictionaries, we might have an utility in which
we need to initialize a dictionary with None values, so that they can be
altered later. This kind of application can occur in cases of memoizations in
general or competitive programming. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Usingzip() + repeat()**  
The combination of these functions can be used to perform this particular
task. In this, the None value is attached to the keys repeated using the
repeat() by help of zip()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary with None values

# Using zip() + repeat()

from itertools import repeat

 

# Using zip() + repeat()

# Initialize dictionary with None values

res = dict(zip(range(10), repeat(None)))

 

# printing result 

print("The dictionary with None values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The dictionary with None values : {0: None, 1: None, 2: None, 3: None, 4:
> None, 5: None, 6: None, 7: None, 8: None, 9: None}

  

  

**Method #2 : Usingfromkeys()**  
This task can also be performed more efficiently using the inbuilt function of
fromkeys() which is tailor-made for this task itself and hence recommended.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary with None values

# Using fromkeys()

 

# Using fromkeys()

# Initialize dictionary with None values

res = dict.fromkeys(range(10))

 

# printing result 

print("The dictionary with None values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The dictionary with None values : {0: None, 1: None, 2: None, 3: None, 4:
> None, 5: None, 6: None, 7: None, 8: None, 9: None}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

