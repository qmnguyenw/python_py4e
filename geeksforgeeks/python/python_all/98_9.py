Python – Incremental Sublist Sum



Sometimes we need to group elements and grouping techniques and requirements
vary accordingly. One such way to group the elements is by the i’th size in
list which stores the dictionary of index keys with values of summation of
subsequent size i. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingislice() + sum() \+ dictionary comprehension**  
The slice method can be used to group the chunks of list required to be made
as values of the dictionaries which are then assigned to their destined index
key using the dictionary comprehension. The sum() is used to perform sum of
created list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental Sublist Sum

# using islice() + sum() + dictionary comprehension

from itertools import islice

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using islice() + sum() + dictionary comprehension

# Incremental Sublist Sum

temp = iter(test_list)

res = {key: val for key, val in ((i,
sum(list(islice(temp, i)))) for i in range(1,
len(test_list))) if val}

 

# printing result

print("The Incremental Sublist Sum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14, 5]
    The Incremental Sublist Sum is : {1: 4, 2: 15, 3: 37, 4: 49}
    

**Method #2 : Usingitemgetter() + takewhile() + islice() + sum()**  
In order to increase the computation speed, we introduce new functions to
perform this particular task, takewhile and itemgetter functions which
performs the task of grouping the sliced values. The sum() is used to perform
sum of created list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental Sublist Sum

# using itemgetter() + takewhile() + islice() + sum()

from itertools import islice, takewhile

from operator import itemgetter

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using itemgetter() + takewhile() + islice() + sum()

# Incremental Sublist Sum

temp = iter(test_list)

res = {key: val for key, val in takewhile(itemgetter(1), ((i,
sum(list(islice(temp, i)))) for i in range(1,
len(test_list))))}

 

# printing result

print("The Incremental Sublist Sum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14, 5]
    The Incremental Sublist Sum is : {1: 4, 2: 15, 3: 37, 4: 49}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

