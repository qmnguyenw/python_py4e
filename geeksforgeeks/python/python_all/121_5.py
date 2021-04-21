Python | Convert tuple to float value



Sometimes, while working with tuple, we can have a problem in which, we need
to convert a tuple to floating-point number in which first element represents
integer part and next element represents a decimal part. Let’s discuss certain
way in which this can be achieved.

 **Method : Usingjoin() + float() + str() \+ generator expression**

The combination of above functionalities can solve this problem. In this, we
1st convert the tuple elements into a string, then join them and convert them
to desired integer.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple to float

# using join() + float() + str() + generator expression

 

# initialize tuple

test_tup = (4, 56)

 

# printing original tuple 

print("The original tuple : " + str(test_tup))

 

# Convert tuple to float

# using join() + float() + str() + generator expression

res = float('.'.join(str(ele) for ele in test_tup))

 

# printing result

print("The float after conversion from tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (4, 56)
    The float after conversion from tuple is : 4.56
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

