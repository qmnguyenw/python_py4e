Python – Vertical Grouping Value Lists



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to group all the list values vertically, i.e w.r.t similar
index. This kind of problem can have applications in many domains such as web
development. Let’s discuss certain ways in which this problem can be solved.

>  **Input** : test_dict = {‘Gfg’: [4, 8], ‘is’: [87, 2], ‘best’ : [14, 1]}  
>  **Output** : [(4, 87, 14), (8, 2, 1)]
>
>  **Input** : test_dict = {‘Gfg’: [4, 6, 7, 8]}  
>  **Output** : [(4, ), (6, ), (7, ), (8, )]

 **Method #1 : Using list comprehension +zip() + * operator**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of extracting values using values() and zip() is used to
perform vertical grouping after unpacking using * operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Verticle Grouping Value Lists

# Using list comprehension + zip() + * operator

 

# initializing dictionary

test_dict = {'Gfg': [4, 5, 7], 'is': [8, 9,
10], 'best' : [10, 12, 14]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Vertical Grouping Value Lists

# Using list comprehension + zip() + * operator

res = [tuple(idx) for idx in zip(*test_dict.values())]

 

# printing result 

print("The grouped values : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {'Gfg': [4, 5, 7], 'is': [8, 9, 10], 'best': [10, 12, 14]}
    The grouped values : [(4, 8, 10), (5, 9, 12), (7, 10, 14)]
    

