Python | Convert number to list of integers



The interconversion of data types is a problem that is quite common in
programming. Sometimes we need to convert a single number to list of integers
and we don’t wish to spend several lines of codes doing it. Hence having ways
to perform this task using shorthands comes handy. Let’s discuss ways in which
this can be performed.  

 **Method #1 : Using list comprehension**  
List comprehension can be used as a shorthand to the longer format of naive
method. In this method, we convert the number to string and then extract its
each character and re convert it to integer.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# conversion of number to list of integers

# using list comprehension

 

# initializing number 

num = 2019

 

# printing number 

print ("The original number is " + str(num))

 

# using list comprehension

# to convert number to list of integers

res = [int(x) for x in str(num)]

 

# printing result 

print ("The list from number is " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original number is 2019
    The list from number is [2, 0, 1, 9]

  
**Method #2 : Usingmap()**  
map function can be used to perform the following task converting each of
the string converted number to the desired integer value to be reconverted to
the list format.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# conversion of number to list of integers

# using map()

 

# initializing number 

num = 2019

 

# printing number 

print ("The original number is " + str(num))

 

# using map()

# to convert number to list of integers

res = list(map(int, str(num)))

 

# printing result 

print ("The list from number is " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original number is 2019
    The list from number is [2, 0, 1, 9]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

