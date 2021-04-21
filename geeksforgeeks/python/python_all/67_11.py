Python – Maximum and Minimum K elements in Tuple



Sometimes, while dealing with tuples, we can have problem in which we need to
extract only extreme K elements, i.e maximum and minimum K elements in Tuple.
This problem can have applications across domains such as web development and
Data Science. Let’s discuss certain ways in which this problem can be solved.

>  **Input** : test_tup = (3, 7, 1, 18, 9), k = 2  
>  **Output** : (3, 1, 9, 18)
>
>  **Input** : test_tup = (3, 7, 1), k=1  
>  **Output** : (1, 3)

 **Method #1 : Usingsorted() \+ loop**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the sort operation using sorted(), and the problem of
extraction of max and min K elements using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum and Minimum K elements in Tuple

# Using sorted() + loop

 

# initializing tuple

test_tup = (5, 20, 3, 7, 6, 8)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# initializing K 

K = 2

 

# Maximum and Minimum K elements in Tuple

# Using sorted() + loop

res = []

test_tup = list(test_tup)

temp = sorted(test_tup)

 

for idx, val in enumerate(temp):

 if idx < K or idx >= len(temp) - K:

 res.append(val)

res = tuple(res)

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original tuple is : (5, 20, 3, 7, 6, 8)
    The extracted values : (3, 5, 8, 20)
    

