Python – Replace Non-Maximum Records



Sometimes, while working with Python records, we can have a problem in which
we need to perform replace of all the records whose one element is not
Maximum. This kind of problem can have application in many domains including
day-day programming and web development domain. Let’s discuss certain ways in
which this task can be performed.

>  **Input** :  
> test_list = [(1, 4), (9, 11)]  
> K = “Non-Max”  
>  **Output** : [‘Non-Max’, (9, 11)]
>
>  **Input** :  
> test_list = [(9, 11), (9, 11), (9, 11)]  
> K = “Non-Max”  
>  **Output** : [(9, 11), (9, 11), (9, 11)]

 **Method #1 : Using loop +map() + filter() \+ lambda**  
The combination of above functionalities can be used to perform this task. In
this, we perform task of filtering using map() and filter function, after that
allocation of values to non-maximum elements using brute force approach using
loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Non-Maximum Records

# Using loop + map() + filter() + lambda

 

# initializing list

test_list = [(1, 4), (9, 11), (4, 6), (6,
8), (9, 11)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = None

 

# Replace Non-Maximum Records

# Using loop + map() + filter() + lambda

res = []

temp = list(filter(lambda ele: ele == max(test_list),
test_list))

for ele in test_list:

 if ele not in temp:

 res.append(K)

 else :

 res.append(ele)

 

# printing result 

print("The list after replacing Non-Maximum : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(1, 4), (9, 11), (4, 6), (6, 8), (9, 11)]
    The list after replacing Non-Maximum : [None, (9, 11), None, None, (9, 11)]
    

