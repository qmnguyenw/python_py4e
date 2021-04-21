Python – Assign K to Non Max-Min elements in Tuple



Sometimes, while working with Python data, we can have a problem in which we
need to assign particular value as per certain condition. One of condition can
be non-max, min element. This kind of task can occur in many application of
day-day programming and competitive programming. Lets discuss certain ways in
which this task can be performed.

>  **Input** :  
> test_tuple = (3, 6, 3, 6, 34, 34)  
> K = None  
>  **Output** : (3, None, 3, None, 34, 34)
>
>  **Input** :  
> test_tuple = (3, 34)  
> K = None  
>  **Output** : (3, 34)

 **Method #1 : Usingmax() + min() + tuple() \+ loop**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of finding minimum and maximum element using min() and
max() and brute force to assign all excepted elements to K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign K to Non Max-Min elements in Tuple

# Using min() + max() + loop + tuple()

 

# initializing tuple

test_tuple = (5, 6, 3, 6, 10, 34)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# initializing K 

K = 4

 

# Assign K to Non Max-Min elements in Tuple

# Using min() + max() + loop + tuple()

res = []

for ele in test_tuple:

 if ele not in [max(test_tuple), min(test_tuple)]:

 res.append(K)

 else:

 res.append(ele)

res = tuple(res)

 

# printing result 

print("The tuple after conversion: " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (5, 6, 3, 6, 10, 34)
    The tuple after conversion: (4, 4, 3, 4, 4, 34)
    

