Python | Embedded Numbers Summation in String List



Sometimes, while working with Python lists, we can have problem in which we
need to concatenate embedded numbers in Strings list and perform its
summation. This can have application in domains dealing with data. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Usingjoin() \+ loop**  
The combination of above functionalities can be used to perform this task. In
this, we perform the task of extracting number using join() and loop is used
to perform the task of summation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Embedded Numbers Summation in String List

# Using join() + loop

 

# initializing list

test_list = ['g4fg', 'i4s5', 'b9e4st']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Embedded Numbers Summation in String List

# Using join() + loop

res = 0

for sub in test_list:

 res += int(''.join(chr for chr in sub if
chr.isdigit()))

 

# printing result 

print("The summation of strings : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['g4fg', 'i4s5', 'b9e4st']
    The summation of strings : 143
    

**Method #2 : Usingsum() \+ list comprehension**  
The combination of above functions can also be used to perform this task. In
this, we perform summation using sum() and list comprehension is used to
compile string of numbers for summation to work upon.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Embedded Numbers Summation in String List

# Using sum() + list comprehension

 

# initializing list

test_list = ['g4fg', 'i4s5', 'b9e4st']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Embedded Numbers Summation in String List

# Using sum() + list comprehension

res = sum([int(''.join(chr for chr in sub if
chr.isdigit()))

 for sub in test_list])

 

# printing result 

print("The summation of strings : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['g4fg', 'i4s5', 'b9e4st']
    The summation of strings : 143
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

