Python | Merge adjacent Digit characters



Sometimes, more than one type of data can come in python list and sometimes
its undesirably tokenized and hence we require to join the digits that has
been tokenized and leave the alphabets as they are. Let’s discuss certain ways
in which this task can be achieved.

 **Method #1 : Using list comprehension + "*" operator**  
This task can be performed using the list comprehension, first by joining the
digits and then joining the words and then separating only the words, while
joining to form resultant string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Merge adjacent Digit characters

# list comprehension + "*" operator

 

# initializing list 

test_list = ['Geeks', 'for', 'Geeks', '2', '5']

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + "*" operator

# Merge adjacent Digit characters

res = [''.join([i for i in test_list if not i.isalpha()]),
*[j for j in test_list if j.isalpha()]]

 

# print result

print("The joined adjacent word list(ignoring alphabets) : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Geeks', 'for', 'Geeks', '2', '5']
    The joined adjacent word list(ignoring alphabets) : ['25', 'Geeks', 'for', 'Geeks']
    

**Method #2 : Usingitertools.chain.from_iterable() + groupby() + join()**  
This task can also be performed using the groupby function which groups the
alphabets together and then from_iterables function joins the list and
characters together joined by the join function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Merge adjacent Digit characters

# itertools.chain.from_iterable() + groupby() + join()

from itertools import chain, groupby

 

# initializing list 

test_list = ['Geeks', 'for', 'Geeks', '2', '5']

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.chain.from_iterable() + groupby() + join()

# Merge adjacent Digit characters

num_group = groupby(test_list, key = str.isdigit)

both_group = [[''.join(i)] if j else list(i) for j, i in
num_group]

res = list(chain.from_iterable(both_group))

 

# print result

print("The joined adjacent word list(ignoring alphabets) : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Geeks', 'for', 'Geeks', '2', '5']
    The joined adjacent word list(ignoring alphabets) : ['25', 'Geeks', 'for', 'Geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

