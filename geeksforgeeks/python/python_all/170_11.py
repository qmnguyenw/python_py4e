Python | Add similar value multiple times in list



Adding a single value in list is quite generic and easy. But to add that value
more than one time, generally, a loop is used to execute this task. Having
shorter tricks to perform this can be handy. Let’s discuss certain ways in
which this can be done.

 **Method #1 : Using * operator**  
We can employ * operator to multiply the occurrence of the particular value
and hence can be used to perform this task of adding value multiple times in
just a single line and makes it readable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to add multiple similar values

# using * operator

 

# using * operator to add multiple values

# adds 3, 50 times.

res = [3] * 50

 

# printing result

print ("The filtered list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The filtered list is : [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
> 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
> 3, 3, 3, 3, 3, 3, 3, 3]

 **Method #2 : Usingextend() \+ list comprehension**  
extend function is used to perform the list append and list comprehension part
is responsible for performing the task of repetition of elements desired
number of times.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to add multiple similar values

# using extend() + list comprehension

 

# using extend() + list comprehension to add multiple values

# adds 3, 50 times.

res = []

res.extend([3 for i in range(50)])

 

# printing result

print ("The filtered list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The filtered list is : [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
> 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
> 3, 3, 3, 3, 3, 3, 3, 3]

 **Method #3 : Usingextend() + itertools.repeat()**  
This is similar to the above method, the task of extend() is similar, but
repeat() performs the task list comprehension performed of iteration N no. of
times desired.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to add multiple similar values

# using extend() + itertools.repeat()

from itertools import repeat

 

# using extend() + itertools.repeat() to add multiple values

# adds 3, 50 times.

res = []

res.extend(repeat(3, 50))

 

# printing result

print ("The filtered list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The filtered list is : [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
> 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
> 3, 3, 3, 3, 3, 3, 3, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

