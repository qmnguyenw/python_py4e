Python – How to Sort a Dictionary by Kth Index Value



While working with Python, one might come to a problem in which one needs to
perform a sort on dictionary based on Kth index of value list. This can be
typically in case of scoring or web development. Let’s discuss a method by
which this task can be performed.

>  **Input** : test_dict = {‘gfg’ : [5, 6, 7], ‘is’ : [1, 4, 7], ‘best’ : [8,
> 3, 1]}, K = 2  
>  **Output** : [(‘best’, [8, 3, 1]), (‘gfg’, [5, 6, 7]), (‘is’, [1, 4, 7])]
>
>  **Input** : test_dict = {‘gfg’ : [5, 6, 7], ‘is’ : [1, 4, 7], ‘best’ : [8,
> 3, 1]}, K = 0  
>  **Output** : [(‘is’, [1, 4, 7]), (‘gfg’, [5, 6, 7]), (‘best’, [8, 3, 1])]

 **Method : Usingsorted() \+ lambda**  
The combination of above functions can be used to solve this problem. In this,
we perform sort using sorted() and lambda function is used to drive Kth index
logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by Kth Index Value

# Using sorted() + lambda

 

# initializing dictionary

test_dict = {'gfg' : [5, 6, 7],

 'is' : [1, 4, 7],

 'best' : [8, 3, 1]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K

K = 1

 

# Sort Dictionary by Kth Index Value

# Using sorted() + lambda

res = sorted(test_dict.items(), key = lambda key: key[1][K])

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {'gfg': [5, 6, 7], 'is': [1, 4, 7], 'best': [8, 3, 1]}
    The sorted dictionary : [('best', [8, 3, 1]), ('is', [1, 4, 7]), ('gfg', [5, 6, 7])]
    

