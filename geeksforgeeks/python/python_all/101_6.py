Python | Consecutive Character Maximum difference



Sometimes, we might have a problem in which we require to get the maximum
difference of 2 numbers from list but with a constraint of having the numbers
in successions. This type of problem can occur while competitive programming.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingmax() + zip() \+ list comprehension**  
This problem can be solved using the combination of above three function in
which max function can be used to get the maximum value, zip and list
comprehension doing the task of extending the logic to the whole list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Character Maximum difference

# using zip() + max() + list comprehension

 

# initializing string 

test_string = '6543452345456987653234'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using zip() + max() + list comprehension

# Consecutive Character Maximum difference

test_string = list(test_string)

res = max(abs(int(a) - int(b)) for a, b in
zip(test_string, test_string[1:]))

 

# print result

print("The maximum consecutive difference is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : 6543452345456987653234
    The maximum consecutive difference is : 3
    

**Method #2 : Usingmax() + map() + operator.sub**  
The above problem can also be solved using yet another combination of
functions. In this combination, map functions performs the task of extending
the logic to whole list and mul operator is used to perform the difference.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Character Maximum difference

# using max() + map() + operator.sub

from operator import sub

 

# initializing string 

test_string = '6543452345456987653234'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using max() + map() + operator.sub

# Consecutive Character Maximum difference

res = max(map(sub, map(int, test_string), map(int,
test_string[1:])))

 

# print result

print("The maximum consecutive difference is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : 6543452345456987653234
    The maximum consecutive difference is : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

