Python – Group Tuples by Kth Index Element



Sometimes, while working with Python records, we can have a problem in which
we need to perform grouping of elements of tuple by similar Kth index element.
This kind of problem can have application in web development domain. Let’s
discuss certain way in which this task can be performed.

>  **Input** : test_list = [(4, 5), (3, 2), (2, 2), (1, 2), (5, 5)], K = 0  
>  **Output** : [((1, 2), ), ((2, 2), ), ((3, 2), ), ((4, 5), ), ((5, 5), )]
>
>  **Input** : test_list = [(4, 5), (3, 2), (2, 2)], K = 1  
>  **Output** : [((2, 2), (3, 2)), ((4, 5), )]

 **Method : Usinggroupby() + itemegetter() \+ generator expression**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of grouping the elements from Kth index extracted using
itemgetter and generator expression is used to bind whole logic together.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Tuples by Kth Index Element

# Using groupby() + itemegetter() + generator expression

from operator import itemgetter

from itertools import groupby

 

# initializing lists

test_list = [(4, 5), (3, 2), (2, 2), (1,
2), (5, 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# Group Tuples by Kth Index Element

# Using groupby() + itemegetter() + generator expression

test_list.sort()

res = list(tuple(sub) for idx, sub in groupby(test_list,
key = itemgetter(K)))

 

# printing result 

print("Tuples after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [(4, 5), (3, 2), (2, 2), (1, 2), (5, 5)]
    Tuples after grouping : [((1, 2), (2, 2), (3, 2)), ((4, 5), (5, 5))]
    

