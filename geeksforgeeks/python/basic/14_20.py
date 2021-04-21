Python | Removing dictionary from list of dictionaries



The common utility to remove the dictionary corresponding to particular key in
a list of dictionaries is also a problem whose concise version is always
helpful. This has application in web development due to the introduction of
No-SQL databases, which work mostly on Key-Value pairs. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using del + loop**  
In the naive method of performing this particular task, we require to use
_del_ to delete the particular key if it matches the key that is required to
be deleted.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to delete dictionary in list

# using del + loop 

 

# initializing list of dictionaries

test_list = [{"id" : 1, "data" : "HappY"},

 {"id" : 2, "data" : "BirthDaY"},

 {"id" : 3, "data" : "Rash"}]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using del + loop 

# to delete dictionary in list

for i in range(len(test_list)):

 if test_list[i]['id'] == 2:

 del test_list[i]

 break

 

# printing result

print ("List after deletion of dictionary : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘id’: 1, ‘data’: ‘HappY’}, {‘id’: 2, ‘data’:
> ‘BirthDaY’}, {‘id’: 3, ‘data’: ‘Rash’}]  
> List after deletion of dictionary : [{‘id’: 1, ‘data’: ‘HappY’}, {‘id’: 3,
> ‘data’: ‘Rash’}]

  
**Method #2 : Using list comprehension**  
This method works by constructing the whole new or overwriting the original
list by all the dictionaries except the one that has the key that has to be
deleted.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to delete dictionary in list

# using list comprehension

 

# initializing list of dictionaries

test_list = [{"id" : 1, "data" : "HappY"},

 {"id" : 2, "data" : "BirthDaY"},

 {"id" : 3, "data" : "Rash"}]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension

# to delete dictionary in list

res = [i for i in test_list if not (i['id'] ==
2)]

 

# printing result

print ("List after deletion of dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘id’: 1, ‘data’: ‘HappY’}, {‘id’: 2, ‘data’:
> ‘BirthDaY’}, {‘id’: 3, ‘data’: ‘Rash’}]  
> List after deletion of dictionary : [{‘id’: 1, ‘data’: ‘HappY’}, {‘id’: 3,
> ‘data’: ‘Rash’}]

  
**Method #3 : Usingfilter() + lambda**  
filter function can be used to get the dictionary with the required key and
lambda function is used to iterate to the lists elements one by one before
which filter can perform its task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to delete dictionary in list

# using filter() + lambda

 

# initializing list of dictionaries

test_list = [{"id" : 1, "data" : "HappY"},

 {"id" : 2, "data" : "BirthDaY"},

 {"id" : 3, "data" : "Rash"}]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using filter() + lambda

# to delete dictionary in list

res = list(filter(lambda i: i['id'] != 2,
test_list))

 

# printing result

print ("List after deletion of dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘id’: 1, ‘data’: ‘HappY’}, {‘id’: 2, ‘data’:
> ‘BirthDaY’}, {‘id’: 3, ‘data’: ‘Rash’}]  
> List after deletion of dictionary : [{‘id’: 1, ‘data’: ‘HappY’}, {‘id’: 3,
> ‘data’: ‘Rash’}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

