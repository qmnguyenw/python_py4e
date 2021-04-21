Python – Row-wise element Addition in Tuple Matrix



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform Row-wise custom elements addition in Tuple matrix. This kind
of problem can have application in data domains. Let’s discuss certain ways in
which this task can be performed.

>  **Input** :  
> test_list = [[(‘Gfg’, 3)], [(‘best’, 1)]]  
> cus_eles = [1, 2]  
>  **Output** : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]]
>
>  **Input** :  
> test_list = [[(‘Gfg’, 6), (‘Gfg’, 3)]]  
> cus_eles = [7]  
>  **Output** : [[(‘Gfg’, 6, 7), (‘Gfg’, 3, 7)]]

 **Method #1 : Usingenumerate() \+ nested list comprehension**  
The combination of above methods can be used to solve this problem. In this,
we perform the task of adding elements using nested list comprehension and
index iteration by enumerate().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Row-wise element Addition in Tuple Matrix

# Using enumerate() + list comprehension

 

# initializing list

test_list = [[('Gfg', 3), ('is', 3)], [('best',
1)], [('for', 5), ('geeks', 1)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Custom eles

cus_eles = [6, 7, 8]

 

# Row-wise element Addition in Tuple Matrix

# Using enumerate() + list comprehension

res = [[sub + (cus_eles[idx], ) for sub in val] for idx,
val in enumerate(test_list)]

 

# printing result 

print("The matrix after row elements addition : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [[(‘Gfg’, 3), (‘is’, 3)], [(‘best’, 1)], [(‘for’, 5),
> (‘geeks’, 1)]]  
> The matrix after row elements addition : [[(‘Gfg’, 3, 6), (‘is’, 3, 6)],
> [(‘best’, 1, 7)], [(‘for’, 5, 8), (‘geeks’, 1, 8)]]

