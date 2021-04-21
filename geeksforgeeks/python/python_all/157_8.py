Python | List expansion by K



Sometimes, we require to reduce the length of python list but other times we
might also require to increase its size and that too by repeating its each
element N times. This type of utility can come in day-day programming. Let’s
discuss certain ways in which this can be achieved.

 **Method #1 : Using list comprehension**  
This task can be performed using the list comprehension method which is just a
shortened version of the generic loop method in which we repeat each element
for K times using the iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# List extension by K 

# using list comprehension

 

# initializing list

test_list = [4, 5, 2, 8]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K

K = 3

 

# using list comprehension 

# to extend list 

res = [i for i in test_list for j in range(K)]

 

# printing result

print("The resultant list after extension is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [4, 5, 2, 8]  
> The resultant list after extension is : [4, 4, 4, 5, 5, 5, 2, 2, 2, 8, 8, 8]

  

  

**Method #2 : Usingitertools.chain() + itertools.tee() + zip()**  
The combination of the above three function can also help to achieve a
solution to this particular problem. The tee function repeats in the list K
times, nested in zip which links the iteration with particular element and
chain function performs this task for all the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# List extension by K 

# using itertools.chain() + itertools.tee() + zip()

from itertools import chain, tee

 

# initializing list

test_list = [4, 5, 2, 8]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K

K = 3

 

# using itertools.chain() + itertools.tee() + zip()

# to extend list 

res = list(chain(*zip(*tee(test_list, K))))

 

# printing result

print("The resultant list after extension is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [4, 5, 2, 8]  
> The resultant list after extension is : [4, 4, 4, 5, 5, 5, 2, 2, 2, 8, 8, 8]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

