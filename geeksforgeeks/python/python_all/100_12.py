Python | Minimum Sum of Consecutive Characters



Sometimes, we might have a problem in which we require to get the minimum sum
of 2 numbers from list but with a constraint of having the numbers in
successions. This type of problem can occur while competitive programming.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingmin() + zip() \+ list comprehension**  
This problem can be solved using the combination of above three function in
which min function can be used to get the minimum value, zip and list
comprehension doing the task of extending the logic to the whole list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum Sum of Consecutive Characters

# using zip() + min() + list comprehension

 

# initializing string 

test_string = '6543452345456987653234'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using zip() + min() + list comprehension

# Minimum Sum of Consecutive Characters

test_string = list(test_string)

res = min(int(a) + int(b) for a, b in
zip(test_string, test_string[1:]))

 

# print result

print("The minimum consecutive sum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : 6543452345456987653234
    The minimum consecutive sum is : 5
    

**Method #2 : Usingmin() + map() \+ operator.add**  
The above problem can also be solved using yet another combination of
functions. In this combination, map functions performs the task of extending
the logic to whole list and add operator is used to perform the
multiplication.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum Sum of Consecutive Characters

# using min() + map() + operator.add

from operator import add

 

# initializing string 

test_string = '6543452345456987653234'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using min() + map() + operator.add

# Minimum Sum of Consecutive Characters

res = min(map(add, map(int, test_string), map(int,
test_string[1:])))

 

# print result

print("The minimum consecutive sum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : 6543452345456987653234
    The minimum consecutive sum is : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

