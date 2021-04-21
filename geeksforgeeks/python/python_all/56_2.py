Python – Kth Index Tuple List Mean



Sometimes, while working with Python tuple, we can have a problem in which we
need to compute average of any paritcular index of tuples in a list. This kind
of problem can have application in data domain such as web development. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(‘Gfg’, 1), (‘is’, 5), (‘best’, 7)], K = 1  
>  **Output** : 4.333333333333333
>
>  **Input** : test_list = [(‘Gfg’, 7), (‘best’, 7)], K = 1  
>  **Output** : 7

 **Method #1 : Usingmean() \+ generator expression**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of mean computation using mean() and generator expression
is used for iterations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth Index Tuple List Mean

# Using mean() + generator expression

from statistics import mean

 

# initializing list

test_list = [('Gfg', 4), ('is', 18), ('best', 2),
('for', 5), ('geeks', 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 1

 

# Kth Index Tuple List Mean

# Using mean() + generator expression

res = mean(val[K] for val in test_list)

 

# printing result 

print("The computed mean : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [('Gfg', 4), ('is', 18), ('best', 2), ('for', 5), ('geeks', 1)]
    The computed mean : 6
    

