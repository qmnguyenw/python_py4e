Python – Mutiple Column Sort in Tuples



Sometimes, while working with records, we can have a problem in which we need
to perform sort operation on one of the columns, and on other column, if equal
elements, opposite sort. This kind of problem can occur as application in many
domains such as web development. Lets discuss certain ways in which this
problem can be solved.

>  **Input** : test_list = [(6, 7), (6, 5), (6, 4), (7, 10)]  
>  **Output** : [(7, 10), (6, 4), (6, 5), (6, 7)]
>
>  **Input** : test_list = [(10, 7), (8, 5)]  
>  **Output** : [(10, 7), (8, 5)]

 **Method #1 : Usingsorted() + lambda**  
The combination of above functions can offer one of the ways to solve this
problem. In this, we perform sort using sorted() and order and column
manipulation is handled by lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mutiple Column Sort in Tuples

# Using sorted() + lambda

 

# initializing list

test_list = [(6, 7), (6, 5), (1, 4), (8,
10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Mutiple Column Sort in Tuples

# Using sorted() + lambda

res = sorted(test_list, key = lambda sub: (-sub[0],
sub[1]))

 

# printing result 

print("The sorted records : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(6, 7), (6, 5), (1, 4), (8, 10)]
    The sorted records : [(8, 10), (6, 5), (6, 7), (1, 4)]
    

