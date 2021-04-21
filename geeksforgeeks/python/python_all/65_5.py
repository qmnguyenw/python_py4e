Python – Rows intersection with K



Sometimes while working with Python Matrix, we can have a problem in which we
need to extract all the rows which match with other matrix, which has a
specfic element. This kind of problem can occur in data domains as Matrix are
input data types for many problems. Let’s discuss certain ways in which this
task can be performed.

>  **Input** :  
> test_list1 = [[5, 6, 7], [7, 6, 6], [5, 7, 10]]  
> test_list2 = [[5, 6, 7], [7, 6, 8], [5, 7, 10]]  
> K = 7  
>  **Output** : 2
>
>  **Input** :  
> test_list1 = [[6, 7], [6], [5]]  
> test_list2 = [[6, 7], [7], [5]]  
> K = 6  
>  **Output** : 1

 **Method #1 : Usingsum() \+ generator expression**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of counting match using sum(), and generator expression is
used to perform the task of comparison.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rows intersection with K

# Using sum() + generator expression

 

# initializing lists

test_list1 = [[5, 6, 7], [7, 6, 6], [5,
7, 10]]

test_list2 = [[5, 6, 7], [7, 6, 8], [5,
7, 10]]

 

# printing original list

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing K 

K = 5

 

# Rows intersection with K

# Using sum() + generator expression

res = sum(sum(a == b for b in test_list2) for a
in test_list1 if K in a)

 

# printing result 

print("The matched rows : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list 1 is : [[5, 6, 7], [7, 6, 6], [5, 7, 10]]
    The original list 2 is : [[5, 6, 7], [7, 6, 8], [5, 7, 10]]
    The matched rows : 2
    

