Python – Test if all digits starts from % K digit



Sometimes we may face a problem in which we need to find for a list if it
contains numbers which are % K. This particular utility has an application in
day-day programming. Let’s discuss certain ways in which this task can be
achieved.

 **Method #1 : Using list comprehension + map()**  
We can approach this problem by converting the elements to the strings and
then testing the starting element of string and if they are % K we can return
true and then convert to set and test for size of result to be one. The
conversion is done by map, set function converts to set and list comprehension
checks for first element of string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if all digits starts from % K digit

# using list comprehension + map() 

 

# initializing list 

test_list = [65, 3, 92, 332] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K 

K = 3

 

# using list comprehension + map() 

# Test if all digits starts from % K digit

res = len(set( not(int(sub[0]) % K) for sub
in map(str, test_list))) == 1

 

# print result 

print("Does each element start with % K digit ? " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [65, 3, 92, 332]
    Does each element start with % K digit ? True
    

**Method #2 : Usingall() \+ list comprehension**  
This is yet another approach in which this problem can be solved. In this we
use all function to check for all elements and return a Boolean result and
list comprehension does the part of conversion of string by str function and
checking for all elements with the first digit of first element to be % K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if all digits starts from % K digit

# using all() + list comprehension 

 

# initializing list 

test_list = [65, 3, 92, 332] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K

K = 3

 

# using all() + list comprehension 

# Check if front digit is Odd in list 

res = not all(int(str(i)[0]) % K for i in
test_list) 

 

# print result 

print("Does each element start with % K digit ? " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [65, 3, 92, 332]
    Does each element start with % K digit ? True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

