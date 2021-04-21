Python | Contiguous Boolean Range



Sometimes, we come across a problem in which we have a lot of data in a list
in the form of True and False value, this kind of problem is common in Machine
learning domain and sometimes we need to know that at a particular position
which boolean value was present. Let’s discuss certain ways in which this can
be done.  

 **Method #1 : Usingenumerate() + zip() + list comprehension**  
By using combination of above three functions, this task can easily be
accomplished. The enumerate function handles the role of iteration, zip
function groups the like values and the logic part is handled by list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Contiguous Boolean Ranging

# using enumerate() + zip() + list comprehension

 

# initializing list 

test_list = [True, True, False, False, True,

 True, True, True, False, True]

 

# printing the original list 

print ("The original list is : " + str(test_list))

 

# using enumerate() + zip() + list comprehension

# for Contiguous Boolean Ranging

res = [x for x, (i , j) in enumerate(zip( [2]

 + test_list, test_list + [2])) if i != j]

 

# printing result

print ("The boolean range list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [True, True, False, False, True, True, True, True,
> False, True]  
> The boolean range list is : [0, 2, 4, 8, 9, 10]

  
**Method #2 : Usingsum() + accumulate() + groupby()**  
The above three functions can also be clubbed together to achieve the
particular task, as they use the iterators to achieve it. The sum function
counts each value, groupby groups each one and all together are accumulated by
the accumulate function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Contiguous Boolean Ranging

# using sum() + accumulate() + groupby()

from itertools import accumulate, groupby

 

# initializing list 

test_list = [True, True, False, False, False,

 True, True, True, False, False]

 

# printing the original list 

print ("The original list is : " + str(test_list))

 

# using sum() + accumulate() + groupby()

# for Contiguous Boolean Ranging

res = [0] + list(accumulate(sum(1 for i in j) 

 for i, j in groupby(test_list)))

 

# printing result

print ("The boolean range list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [True, True, False, False, False, True, True, True,
> False, False]  
> The boolean range list is : [0, 2, 5, 8, 10]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

