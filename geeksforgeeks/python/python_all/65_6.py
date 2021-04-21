Python – Unique Kth positioned tuples



Sometimes, while working with Python records, we can have a problem in which
we need to extract only the unique tuples, based on some particular index of
tuples. This kind of problem can have applications in domains such as web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** :  
> test_list = [(5, 6, 5), (4, 2, 7), (1, 2, 3), (9, 6, 5)]  
> K = 3  
>  **Output** : [(1, 2, 3), (5, 6, 5), (4, 2, 7)]  
>  **Input** :  
> test_list = [(5, ), (1, ), (1, ), (9, )]  
> K = 1  
>  **Output** : [(1, ), (5, ), (9, )]

 **Method #1 : Usingmap() + next() \+ lambda**  
The combination of above functions can be used to solve this problem. In this,
we extend the logic of getting unique elements extracted using lambda function
and next(), using map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Kth index tuples

# Using map() + next() + lambda

 

# initializing list

test_list = [(5, 6, 8), (4, 2, 7), (1, 2,
3), (9, 6, 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# Unique Kth index tuples

# Using map() + next() + lambda

res = [*map(lambda ele: next(tup for tup in
test_list if tup[K - 1] == ele),

 {tup[K - 1] for tup in test_list})]

 

# printing result 

print("The extracted elements : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(5, 6, 8), (4, 2, 7), (1, 2, 3), (9, 6, 5)]
    The extracted elements : [(4, 2, 7), (5, 6, 8)]
    

  

  

**Method #2 : Usingnext() + groupby() + lambda**  
The combination of above functions can also be used to solve this problem. In
this, we perform task of map() in above using groupby(), in a more compact
way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Kth index tuples

# Using next() + groupby() + lambda

from itertools import groupby

 

# initializing list

test_list = [(5, 6, 8), (4, 2, 7), (1, 2,
3), (9, 6, 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# Unique Kth index tuples

# Using next() + groupby() + lambda

temp = lambda ele : ele[K - 1]

res = [next(val) for _, val in groupby(sorted(test_list,
key = temp), key = temp)]

 

# printing result 

print("The extracted elements : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(5, 6, 8), (4, 2, 7), (1, 2, 3), (9, 6, 5)]
    The extracted elements : [(4, 2, 7), (5, 6, 8)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

