Python | Grouping similar substrings in list



Sometimes we have an application in which we require to group common prefix
strings into one such that further processing can be done according to the
grouping. This type of grouping is useful in the cases of Machine Learning and
Web Development. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usinglambda + itertools.groupby() + split()**  
The combination of above three functions help us achieve the task. The split
method is key as it defines the seperator by which grouping has to be
performed. The groupby function does the grouping of elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# group similar substrings

# using lambda + itertools.groupby() + split()

from itertools import groupby

 

# initializing list 

test_list = ['geek_1', 'coder_2', 'geek_4', 'coder_3',
'pro_3']

 

# sort list 

# essential for grouping

test_list.sort()

 

# printing the original list 

print ("The original list is : " + str(test_list))

 

# using lambda + itertools.groupby() + split()

# group similar substrings

res = [list(i) for j, i in groupby(test_list,

 lambda a: a.split('_')[0])]

 

# printing result

print ("The grouped list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘coder_2’, ‘coder_3’, ‘geek_1’, ‘geek_4’, ‘pro_3’]  
> The grouped list is : [[‘coder_2’, ‘coder_3’], [‘geek_1’, ‘geek_4’],
> [‘pro_3’]]

  

  

**Method #2 : Usinglambda + itertools.groupby() + partition()**  
The similar task can also be performed replacing the split function with the
partition function. This is more efficient way to perform this task as it uses
the iterators and hence internally quicker.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# group similar substrings

# using lambda + itertools.groupby() + partition()

from itertools import groupby

 

# initializing list 

test_list = ['geek_1', 'coder_2', 'geek_4', 'coder_3',
'pro_3']

 

# sort list 

# essential for grouping

test_list.sort()

 

# printing the original list 

print ("The original list is : " + str(test_list))

 

# using lambda + itertools.groupby() + partition()

# group similar substrings

res = [list(i) for j, i in groupby(test_list,

 lambda a: a.partition('_')[0])]

 

# printing result

print ("The grouped list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘coder_2’, ‘coder_3’, ‘geek_1’, ‘geek_4’, ‘pro_3’]  
> The grouped list is : [[‘coder_2’, ‘coder_3’], [‘geek_1’, ‘geek_4’],
> [‘pro_3’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

