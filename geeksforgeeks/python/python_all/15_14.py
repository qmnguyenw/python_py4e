Python Program to Find Numbers Divisible by 7 and Multiple of 5 in a Given
Range



Given a range of numbers, the task is to write a Python program to find
numbers divisible by 7 and multiple of 5.

 **Example:**

    
    
     **Input:** Enter minimum 100
    Enter maximum 200
    
    **Output:**
    105  is divisible by 7 and 5.
    140  is divisible by 7 and 5.
    175  is divisible by 7 and 5.
    
    
    **Input:** Input:Enter minimum 29
    Enter maximum 36
    
    **Output:**
    35  is divisible by 7 and 5.

A set of integers can be checked for divisibility by 7 and 5 by performing the
modulo operation of the number with 7 and 5 respectively, and then checking
the remainder. This can be done in the following ways :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# enter the starting range number

start_num = int(29)

 

# enter the ending range number

end_num = int(36)

 

# initialise counter with starting number

cnt = start_num

 

# check until end of the range is achieved

while cnt <= end_num:

 

 # if number divisible by 7 and 5

 if cnt % 7 == 0 and cnt % 5 == 0:

 print(cnt, " is divisible by 7 and 5.")

 

 # increment counter

 cnt += 1  
  
---  
  
 __

 __

 **Output:**

    
    
    35  is divisible by 7 and 5.

This can also be done by checking if the number is divisible by 35, since the
LCM of 7 and 5 is 35 and any number divisible by 35 is divisible by 7 and 5
and vice versa also.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# enter the starting range number

start_num = int(68)

 

# enter the ending range number

end_num = int(167)

 

# initialise counter with starting number

cnt = start_num

 

# check until end of the range is achieved

while cnt <= end_num:

 

 # check if number is divisible by 7 and 5

 if(cnt % 35 == 0):

 print(cnt, "is divisible by 7 and 5.")

 

 # incrementing counter

 cnt += 1  
  
---  
  
 __

 __

 **Output:**

    
    
    70 is divisible by 7 and 5.
    105 is divisible by 7 and 5.
    140 is divisible by 7 and 5.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

