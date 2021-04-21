Python | Joining only adjacent words in list



Sometimes, more than one type of data can come in Python list and sometimes
it’s undesirably tokenized and hence we require to join the words that have
been tokenized and leave the digits as they are. Let’s discuss certain ways in
which this task can be achieved.

 **Method #1 : Using list comprehension +"*" operator**  
This task can be performed using the list comprehension, first by joining the
words and then joining the digits and then separating only the numbers, while
joining to form the resultant string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# joining only adjacent words in list 

# list comprehension + "*" operator

 

# initializing list 

test_list = ['Geeks', '5', 'for', '9', 'Geeks' ,
'2', '5']

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + "*" operator

# joining only adjacent words in list

res = [''.join([i for i in test_list if not i.isdigit()]),

 *[j for j in test_list if j.isdigit()]]

 

# print result

print("The joined adjacent word list(ignoring digits) : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list : [‘Geeks’, ‘5’, ‘for’, ‘9’, ‘Geeks’, ‘2’, ‘5’]  
> The joined adjacent word list(ignoring digits) : [‘GeeksforGeeks’, ‘5’, ‘9’,
> ‘2’, ‘5’]

  

  

**Method #2 : Usingitertools.chain.from_iterable() + groupby() + join()**  
This task can also be performed using the groupby function which groups the
digits together and then from_iterables function joins the list and
characters together joined by the join function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# joining only adjacent words in list 

# itertools.chain.from_iterable() + groupby() + join()

from itertools import chain, groupby

 

# initializing list 

test_list = ['Geeks', '5', 'for', 'Geeks' , '2',
'3']

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.chain.from_iterable() + groupby() + join()

# joining only adjacent words in list

num_group = groupby(test_list, key = str.isalpha)

both_group = [[''.join(i)] if j else list(i)

 for j, i in num_group]

 

res = list(chain.from_iterable(both_group))

 

# print result

print("The joined adjacent word list(ignoring digits) : "

 + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list : [‘Geeks’, ‘5’, ‘for’, ‘Geeks’, ‘2’, ‘3’]  
> The joined adjacent word list(ignoring digits) : [‘Geeks’, ‘5’, ‘forGeeks’,
> ‘2’, ‘3’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

