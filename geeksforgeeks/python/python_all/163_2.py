Python – Insert after every Nth element in a list



Sometimes we need to perform a single insertion in python, this can be easily
done with the help of the insert function. But sometimes, we require to insert
in a repeated manner after every n numbers, for that there can be numerous
shorthands that can be quite handy. Lets discuss certain ways in which this
can be done.

 **Method #1 : Usingjoin() + enumerate()**  
We can use the join function to join each of nth substring with the digit K
and enumerate can do the task of performing the selective iteration of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# inserting K after every Nth number

# using join() + enumerate()

 

# initializing list

test_list = ['g', 'e', 'e', 'k', 's', 'f',
'o', 'r',

 'g', 'e', 'e', 'k', 's']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing k 

k = 'x'

 

# initializing N

N = 3

 

# using join() + enumerate()

# inserting K after every Nth number 

res = list(''.join(i + k * (N % 3 == 2) 

 for N, i in enumerate(test_list)))

 

# printing result 

print ("The lists after insertion : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘g’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’, ‘g’, ‘e’,
> ‘e’, ‘k’, ‘s’]  
> The lists after insertion : [‘g’, ‘e’, ‘e’, ‘x’, ‘k’, ‘s’, ‘f’, ‘x’, ‘o’,
> ‘r’, ‘g’, ‘x’, ‘e’, ‘e’, ‘k’, ‘x’, ‘s’]

  
**Method #2 : Usingitertools.chain()**  
This method also has the ability to perform a similar task using an iterator
and hence an improvement in the performance. This function performs a similar
task but uses chain method to join the _n_ substrings.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# inserting K after every Nth number

# using itertool.chain()

from itertools import chain

 

# initializing list

test_list = ['g', 'e', 'e', 'k', 's', 'f',
'o', 'r',

 'g', 'e', 'e', 'k', 's']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing k 

k = 'x'

 

# initializing N

N = 3

 

# using itertool.chain()

# inserting K after every Nth number 

res = list(chain(*[test_list[i : i+N] + [k] 

 if len(test_list[i : i+N]) == N 

 else test_list[i : i+N] 

 for i in range(0, len(test_list), N)]))

 

# printing result 

print ("The lists after insertion : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘g’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’, ‘g’, ‘e’,
> ‘e’, ‘k’, ‘s’]  
> The lists after insertion : [‘g’, ‘e’, ‘e’, ‘x’, ‘k’, ‘s’, ‘f’, ‘x’, ‘o’,
> ‘r’, ‘g’, ‘x’, ‘e’, ‘e’, ‘k’, ‘x’, ‘s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

