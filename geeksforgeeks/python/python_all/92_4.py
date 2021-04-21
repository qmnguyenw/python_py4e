Python – Case Insensitive Strings Grouping



Sometimes, we have a use case in which we need to perform the grouping of
strings by various factors, like first letter or any other factor. These type
of problems are typical to database queries and hence can occur in web
development while programming. This article focuses on one such grouping by
case insensitivity i.e grouping all strings which are same but have different
cases. Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingnext() \+ lambda + loop**  
The combination of above 3 functions is used to solve this particular problem
by the naive method. The lambda function performs the task of finding like
cases, and next function helps in forward iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Case Insensitive Strings Grouping

# using next() + lambda + loop

 

# initializing list

test_list = ['man', 'a', 'gEek', 'for', 'GEEK',
'FoR']

 

# printing original list

print("The original list : " + str(test_list))

 

# using next() + lambda + loop

# Case Insensitive Strings Grouping

util_func = lambda x, y: str.lower(x) == str.lower(y)

res = []

for sub in test_list:

 ele = next((x for x in res if util_func(sub, x[0])),
[])

 if ele == []:

 res.append(ele)

 ele.append(sub)

 

# print result

print("The list after Categorization : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['man', 'a', 'gEek', 'for', 'GEEK', 'FoR']
    The list after Categorization : [['man'], ['a'], ['gEek', 'GEEK'], ['for', 'FoR']]
    

**Method #2 : Usingsorted() + groupby()**  
This particular task can also be solved using the groupby function which
offers a conventional method to solve this problem. The sorted function sorts
the elements by size to be feed to groupby for the relevant grouping.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Case Insensitive Strings Grouping

# using sorted() + groupby()

from itertools import groupby

 

# initializing list

test_list = ['man', 'a', 'gEek', 'for', 'GEEK',
'FoR']

 

# printing original list

print("The original list : " + str(test_list))

 

# using sorted() + groupby()

# Case Insensitive Strings Grouping

util_func = lambda x: str.lower(x)

temp = sorted(test_list, key = util_func)

res = [list(ele) for i, ele in groupby(temp, util_func)]

 

# print result

print("The list after Categorization : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['man', 'a', 'gEek', 'for', 'GEEK', 'FoR']
    The list after Categorization : [['man'], ['a'], ['gEek', 'GEEK'], ['for', 'FoR']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

