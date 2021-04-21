Python – Find all pairs of consecutive odd positive integer smaller than a
with sum greater than b



Given two positive integers _a_ and _b_ , the task is to write a program in
python to find all pairs of consecutive odd numbers which are smaller than the
first number _a_ and their sum should be greater than the second number _b_.

**Examples:**

    
    
     **Input:**
    a = 60
    b = 100
    **Output:**
    Pairs of consecutive number are:
    51 , 53
    53 , 55
    55 , 57
    57 , 59
    
    **Input:**
    a = 20
    b = 200
    **Output:**
    None

 **Approach:**

Two numbers are given and then check if they are a positive integer and
checked for the first number to be greater than the half of the second number.
Then we will check for odd positive integer and assigned in a variable _a._ In
the _while_ statement, pairs of the odd consecutive integers are found and
printed.

 **Example 1:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# input first and second number

a = 60

b = 100

 

print('a =', a)

print('b =', b)

 

# check the first number should be greater

# than the half of second number and both number

# should be positive integer

if(a > 0 and b > 0 and a > b/2):

 

 # to ensure value in firstNum variable

 # must be odd positive integer

 if(a % 2 == 0):

 a -= 1

 else:

 a -= 2

 

 b //= 2

 print("Pairs of consecutive number are:")

 

 # find the pairs of odd

 # consecutive positive integer

 while(b <= a):

 if(b % 2 != 0):

 x = b

 if(x + 2 <= a):

 print(x, ',', x+2)

 

 b += 1

else:

 print("None")  
  
---  
  
 __

 __

 **Output:**

    
    
    a = 60
    b = 100
    Pairs of consecutive number are:
    51 , 53
    53 , 55
    55 , 57
    57 , 59

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# input first and second number

a = 20

b = 200

 

print('a =', a)

print('b =', b)

 

# check the first number should be greater

# than the half of second number and both number

# should be positive integer

if(a > 0 and b > 0 and a > b/2):

 

 # to ensure value in firstNum variable

 # must be odd positive integer

 if(a % 2 == 0):

 a -= 1

 else:

 a -= 2

 

 b //= 2

 print("Pairs of consecutive number are:")

 

 # find the pairs of odd

 # consecutive positive integer

 while(b <= a):

 if(b % 2 != 0):

 x = b

 if(x + 2 <= a):

 print(x, ',', x+2)

 

 

 b += 1

else:

 print("None")  
  
---  
  
 __

 __

 **Output:**

    
    
    a = 20
    b = 200
    None

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

