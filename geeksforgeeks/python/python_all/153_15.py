Python | Splitting list on empty string



Sometimes, we may face an issue in which we require to split a list to list of
list on the blank character sent as deliminator. This kind of problem can be
used to send messages or can be used in cases where it is desired to have list
of list of native list. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingindex() and list slicing**  
The list slicing can be used to get the sublists from the native list and
index function can be used to check for the empty string which can potentially
act as a separator. The drawback of this is that it only works for a single
split i.e can only divide a list to 2 sublists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# divide list to siblist on deliminator

# using index() + list slicing 

 

# initializing list 

test_list = ['Geeks', 'for', '', 'Geeks', 1, 2]

 

# printing original list

print("The original list : " + str(test_list))

 

# using index() + list slicing

# divide list to siblist on deliminator

temp_idx = test_list.index('')

res = [test_list[: temp_idx], test_list[temp_idx + 1: ]]

 

# print result

print("The list of sublist after separation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘Geeks’, ‘for’, ”, ‘Geeks’, 1, 2]  
> The list of sublist after separation : [[‘Geeks’, ‘for’], [‘Geeks’, 1, 2]]

  

  

**Method #2 : Usingitertools.groupby() + list comprehension**  
The problem of the above proposed method can be solved using the groupby
function which could divide on all the list breaks given by the empty strings.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# divide list to siblist on deliminator

# using itertools.groupby() + list comprehension

from itertools import groupby

 

# initializing list 

test_list = ['Geeks', '', 'for', '', 4, 5, '',

 'Geeks', 'CS', '', 'Portal']

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.groupby() + list comprehension

# divide list to siblist on deliminator

res = [list(sub) for ele, sub in groupby(test_list, key =
bool) if ele]

 

# print result

print("The list of sublist after separation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘Geeks’, ”, ‘for’, ”, 4, 5, ”, ‘Geeks’, ‘CS’, ”,
> ‘Portal’]  
> The list of sublist after separation : [[‘Geeks’], [‘for’], [4, 5],
> [‘Geeks’, ‘CS’], [‘Portal’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

