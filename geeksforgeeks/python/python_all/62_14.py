Python – Custom Tuple Key Summation in Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform group summation of values, of certain key on
particular index of tuple keys of dictionary. This problem is quite custom,
but can have application in domains that revolves around data processing.
Let’s discuss certain ways in which this task can be performed.

>  **Input** :  
> test_dict = {(‘a’, ‘b’): 14, (‘c’, ‘a’): 16, (‘a’, ‘c’): 67}  
> K = ‘c’, idx = 1  
>  **Output** : 16
>
>  **Input** :  
> test_dict = {(‘a’, ‘b’): 14, (‘c’, ‘a’): 16, (‘a’, ‘c’): 67}  
> K = ‘c’, idx = 2  
>  **Output** : 67

 **Method #1 : Usingsum() \+ generator expression**  
The combination of above functions can be used to solve this problem. In this,
we perform summation using sum() and perform task of filtering using generator
expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Tuple Key Summation in Dictionary

# Using sum() + generator expression

 

# initializing dictionary

test_dict = {('a', 'b'): 14, ('c', 'a'): 16,
('a', 'c'): 67, ('b', 'a'): 17}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 'a'

 

# initializing index

idx = 1

 

# Custom Tuple Key Summation in Dictionary

# Using sum() + generator expression

res = sum(val for key, val in test_dict.items() if key[idx
- 1] == K)

 

# printing result 

print("The grouped summation : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {('a', 'b'): 14, ('c', 'a'): 16, ('a', 'c'): 67, ('b', 'a'): 17}
    The grouped summation : 81
    

