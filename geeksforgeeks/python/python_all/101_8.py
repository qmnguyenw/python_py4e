Python – Group list by first character of string



Sometimes, we have a use case in which we need to perform the grouping of
strings by various factors, like first letter or any other factor. These type
of problems are typical to database queries and hence can occur in web
development while programming. This article focuses on one such grouping by
first letter of string. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Usingnext() + lambda \+ loop**  
The combination of above 3 functions is used to solve this particular problem
by the naive method. The lambda function performs the task of finding like
initial character, and next function helps in forward iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Initial Character Case Categorization

# using next() + lambda + loop

 

# initializing list

test_list = ['an', 'a', 'geek', 'for', 'g',
'free']

 

# printing original list

print("The original list : " + str(test_list))

 

# using next() + lambda + loop

# Initial Character Case Categorization

util_func = lambda x, y: x[0] == y[0]

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

    
    
    The original list : ['an', 'a', 'geek', 'for', 'g', 'free']
    The list after Categorization : [['an', 'a'], ['geek', 'g'], ['for', 'free']]
    

**Method #2 : Usingsorted() + groupby()**  
This particular task can also be solved using the groupby function which
offers a conventional method to solve this problem. The sorted function sorts
the elements by initial character to be feed to groupby for the relevant
grouping.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Initial Character Case Categorization

# using sorted() + groupby()

from itertools import groupby

 

# initializing list

test_list = ['an', 'a', 'geek', 'for', 'g',
'free']

 

# printing original list

print("The original list : " + str(test_list))

 

# using sorted() + groupby()

# Initial Character Case Categorization

util_func = lambda x: x[0]

temp = sorted(test_list, key = util_func)

res = [list(ele) for i, ele in groupby(temp, util_func)]

 

# print result

print("The list after Categorization : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['an', 'a', 'geek', 'for', 'g', 'free']
    The list after Categorization : [['an', 'a'], ['geek', 'g'], ['for', 'free']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

