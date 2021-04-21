Python – Test Kth index in Dictionary value list



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to test if througout the dictionary, the kth index of all values
in dictionary is equal to N. This kind of problem can occur in web development
domain. Let’s discuss certain ways in which this problem can be solved.

>  **Input** : test_dict = {‘Gfg’ : [10, 4, 8, 17], ‘best’ : [90, 4]}  
>  **Output** : True
>
>  **Input** : test_dict = {‘Gfg’ : [10, 7]}  
>  **Output** : False

 **Method #1 : Using loop +items()**  
The combination of above functions can be used to solve this problem. In this,
we check for all items of dictionary using items() and loop is used to iterate
for dictionary keys and testing for equality.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Kth index in Dictionary value list

# Using items() + loop

 

# initializing dictionary

test_dict = {'Gfg' : [1, 4, 8], 'is' : [8, 4,
2], 'best' : [7, 4, 9]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K 

K = 2

 

# initializing N 

N = 4

 

# Test Kth index in Dictionary value list

# Using items() + loop

res = True

for key, val in test_dict.items():

 if val[K - 1] != N:

 res = False

 

# printing result 

print("Are all Kth index equal to N : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary : {'is': [8, 4, 2], 'best': [7, 4, 9], 'Gfg': [1, 4, 8]}
    Are all Kth index equal to N : True
    

