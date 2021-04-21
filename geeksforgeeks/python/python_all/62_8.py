Python – Extract Item with Maximum Tuple Value



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract the item with maximum value of value tuple index.
This kind of problem can have application in domains such as web development.
Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_dict = {‘gfg’ : (4, 6), ‘is’ : (7, 8), ‘best’ : (8, 2)},
> tup_idx = 0  
>  **Output** : (‘best’, (8, 2))
>
>  **Input** : test_dict = {‘gfg’ : (4, 6), ‘best’ : (8, 2)}, tup_idx = 1  
>  **Output** : (‘gfg’ : (4, 6))

 **Method #1 : Using max() + lambda**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of extracting maximum item using max, and value parameter
is checked using lambda.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Item with Maximum Tuple Value

# Using max() + lambda

 

# initializing dictionary

test_dict = {'gfg' : (4, 6),

 'is' : (7, 8),

 'best' : (8, 2)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing tuple index 

# 0 based indexing

tup_idx = 1

 

# Extract Item with Maximum Tuple Value

# Using max() + lambda

res = max(test_dict.items(), key = lambda ele:
ele[1][tup_idx])

 

# printing result 

print("The extracted maximum element item : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {'gfg': (4, 6), 'is': (7, 8), 'best': (8, 2)}
    The extracted maximum element item : ('is', (7, 8))
    

