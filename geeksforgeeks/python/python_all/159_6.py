Python | Associating a single value with all list items



Sometimes we come across a utility in which we have a list and we wish to
associate with it any one of the given value. This can occur in many phases of
programming and knowing the shorthands to it can be useful. Let’s discuss
certain ways in which this can be done.

 **Method #1 : Usingmap() \+ lambda**  
This task can be done using map function which is inbuilt python function that
is generally used to associate or aggregate values. Lambda function can feed a
particular value to the map function for its execution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# associate value in list 

# using map() + lambda

 

# initializing list

test_list = [1, 4, 5, 8, 3, 10]

 

# initializing value to associate

val = 'geeks'

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# printing value 

print ("The value to be attached to each value : " + str(val))

 

# using map() + lambda

# associate value in list 

res = list(map(lambda i: (i, val), test_list))

 

# printing result

print ("The modified attached list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [1, 4, 5, 8, 3, 10]  
> The value to be attached to each value : geeks  
> The modified attached list is : [(1, ‘geeks’), (4, ‘geeks’), (5, ‘geeks’),
> (8, ‘geeks’), (3, ‘geeks’), (10, ‘geeks’)]

  

  

**Method #2 : Usingzip() + itertools.repeat()**  
The zip function can be used to attach the required value with the elements in
a sequence and repeat function can be used to extend the task to all the list
elements in more efficient manner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# associate value in list 

# using zip() + itertools.repeat()

from itertools import repeat

 

# initializing list

test_list = [1, 4, 5, 8, 3, 10]

 

# initializing value to associate

val = 'geeks'

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# printing value 

print ("The value to be attached to each value : " + str(val))

 

# using zip() + itertools.repeat()

# associate value in list 

res = list(zip(test_list, repeat(val)))

 

# printing result

print ("The modified attached list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [1, 4, 5, 8, 3, 10]  
> The value to be attached to each value : geeks  
> The modified attached list is : [(1, ‘geeks’), (4, ‘geeks’), (5, ‘geeks’),
> (8, ‘geeks’), (3, ‘geeks’), (10, ‘geeks’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

