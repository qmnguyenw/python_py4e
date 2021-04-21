Python – Add K to Minimum element in Column Tuple List



Sometimes, while working with Tuple records, we can have a problem in which we
need to perform task of adding certain element to max/ min element to each
column of Tuple list. This kind of problem can have application in web
development domain. Let’s discuss a certain way in which this task can be
performed.

>  **Input** : test_list = [(4, 5), (3, 2), (2, 2), (4, 6), (3, 2), (4, 5)], K
> = 2  
>  **Output** : [(4, 5), (3, 4), (4, 4), (4, 6), (3, 4), (4, 5)]
>
>  **Input** : test_list = [(4, 5), (3, 2), (2, 2), (4, 6), (3, 2), (4, 5)], K
> = 3  
>  **Output** : [(4, 5), (3, 5), (5, 5), (4, 6), (3, 5), (4, 5)]

 **Method : Using min() \+ loop**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of extracting min’s for each column using min() and
addition of K using logic compiled in loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add K to Minimum element in Column Tuple List

# Using min() + loop

 

# initializing lists

test_list = [(4, 5), (3, 2), (2, 2), (4,
6), (3, 2), (4, 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# Add K to Minimum element in Column Tuple List

# Using min() + loop

a_min = min(a for a, b in test_list)

b_min = min(b for a, b in test_list)

res = []

 

for a, b in test_list:

 if a == a_min and b == b_min:

 res.append((a + K, b + K))

 elif a == a_min :

 res.append((a + K, b))

 elif b == b_min:

 res.append((a, b + K))

 else :

 res.append((a, b))

 

# printing result 

print("Tuple after modification : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [(4, 5), (3, 2), (2, 2), (4, 6), (3, 2), (4, 5)]
    Tuple after modification : [(4, 5), (3, 7), (7, 7), (4, 6), (3, 7), (4, 5)]
    

