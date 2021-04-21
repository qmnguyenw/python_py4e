Python | Tokenizing strings in list of strings



Sometimes, while working with data, we need to perform the string tokenization
of the strings that we might get as an input as list of strings. This has a
usecase in many application of Machine Learning. Let’s discuss certain ways in
which this can be done.

 **Method #1 : Using list comprehension +split()**

We can achieve this particular task using list comprehension to traverse for
each strings from list of strings and split function performs the task of
tokenization.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tokenizing strings in list of strings

# using list comprehension + split()

 

# initializing list

test_list = ['Geeks for Geeks', 'is', 'best computer science
portal']

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + split()

# Tokenizing strings in list of strings

res = [sub.split() for sub in test_list]

 

# print result

print("The list after split of strings is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘Geeks for Geeks’, ‘is’, ‘best computer science
> portal’]  
> The list after split of strings is : [[‘Geeks’, ‘for’, ‘Geeks’], [‘is’],
> [‘best’, ‘computer’, ‘science’, ‘portal’]]
>
>  
>
>
>  
>

**Method #2 : Usingmap() + split()**  
This is yet another method in which this particular task can be solved. In
this method, we just perform the similar task as above, just we use map
function to bind the split logic to the entire list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tokenizing strings in list of strings

# using map() + split()

 

# initializing list

test_list = ['Geeks for Geeks', 'is', 'best computer science
portal']

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + split()

# Tokenizing strings in list of strings

res = list(map(str.split, test_list))

 

# print result

print("The list after split of strings is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘Geeks for Geeks’, ‘is’, ‘best computer science
> portal’]  
> The list after split of strings is : [[‘Geeks’, ‘for’, ‘Geeks’], [‘is’],
> [‘best’, ‘computer’, ‘science’, ‘portal’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

