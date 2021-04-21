Python – Closest Pair to Kth index element in Tuple



Sometimes, while working with Python records, we can have a problem in which
we need to find the tuple nearest to certain tuple, query on a particular
index. This kind of problem can have application in data domains such as web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** :  
> test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]  
> tup = (17, 23)  
> K = 2
>
>  **Output** : (19, 23)  
>  **Input** :  
> test_list = [(3, 4, 9), (5, 6, 7)]  
> tup = (1, 2, 5)  
> K = 3  
>  **Output** : (5, 6, 7)

 **Method #1 : Usingenumerate() \+ loop**  
The combination of above functions offer brute force way to solve this
problem. In this, we use enumerate() to monitor index and abs() to keep the
minimum difference updated checked for each element over a loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Closest Pair to Kth index element in Tuple

# Using enumerate() + loop

 

# initializing list

test_list = [(3, 4), (78, 76), (2, 3), (9,
8), (19, 23)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing tuple

tup = (17, 23)

 

# initializing K 

K = 1

 

# Closest Pair to Kth index element in Tuple

# Using enumerate() + loop

min_dif, res = 999999999, None

for idx, val in enumerate(test_list):

 dif = abs(tup[K - 1] - val[K - 1])

 if dif < min_dif:

 min_dif, res = dif, idx

 

# printing result 

print("The nearest tuple to Kth index element is : " +
str(test_list[res]))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
    The nearest tuple to Kth index element is : (19, 23)
    

