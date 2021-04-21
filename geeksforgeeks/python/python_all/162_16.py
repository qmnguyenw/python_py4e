Python | Check if k occurs atleast n times in a list



There are many common problems that a developer or common programmer comes
across in day-day coding. One such problem is finding if an element occurs
more than a certain number of times in the list. Let’s discuss certain ways to
deal with this problem.

 **Method #1 :** Using sum() \+ list comprehension  
The list comprehension can be clubbed with the sum function for achieving this
particular task. The sum function does the summation part and the logical case
of returning true is dealt in list comprehension part.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# check for minimum N occureneces of K 

# using sum() + list comprehension

 

# initializing list

test_list = [1, 3, 5, 5, 4, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing k 

k = 5

 

# initializing N

N = 3

 

# using sum() + list comprehension

# checking occurrences of K atleast N times 

res = 0

res = sum([1 for i in test_list if i == k]) >=
N

if res == 1 :

 res = True

else : 

 res = False

 

# printing result 

print ("Does %d occur atleast %d times ? :" %(k, N) +
str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 3, 5, 5, 4, 5]
    Does 5 occur atleast 3 times ? : True
    

  
**Method #2 :** Using next() + islice()  
These both functions can be used together to perform this particular task in
more efficient manner than above. The islice function would handle the
summation part and next function helps with iteration logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# check for minimum N occureneces of K 

# using next() + islice()

from itertools import islice

 

# initializing list

test_list = [1, 3, 5, 5, 4, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing k 

k = 5

 

# initializing N

N = 3

 

# using next() + islice()

# checking occurrences of K atleast N times 

func = (True for i in test_list if i == k)

res = next(islice(func, N-1, None), False)

 

# printing result 

print ("Does %d occur atleast %d times ? :" %(k, N) +
str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 3, 5, 5, 4, 5]
    Does 5 occur atleast 3 times ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

