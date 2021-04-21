Python – Filter Key from Nested item



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract the keys which have a particular key-value pair as
part of their nested item. This kind of problem is common in web development
domain. Lets discuss certain ways in which this task can be performed.

>  **Input** : test_dict = {‘gfg’ : {‘best’ : 10, ‘good’ : 5}}  
>  **Output** : [‘gfg’]
>
>  **Input** : test_dict = {‘gfg’ : {‘best’ : 10, ‘good’ : 12}}  
>  **Output** : []

 **Method #1 : Using loop +__contains__**  
The combination of above functions constitutes the brute force way to perform
this task. In this, we iterate for each key using loop and check for value
presence using __contains__.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Key from Nested item

# Using loop + __contains__

 

# initializing dictionary

test_dict = {'gfg' : {'best' : 4, 'good' : 5}, 

 'is' : {'better' : 6, 'educational' : 4},

 'CS' : {'priceless' : 6}, 

 'Maths' : {'good' : 5}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing dictionary

que_dict = {'good' : 5}

 

# Filter Key from Nested item

# Using loop + __contains__

res = []

for key, val in test_dict.items():

 if(test_dict[key].__contains__('good')):

 if(test_dict[key]['good'] == que_dict['good']):

 res.append(key)

 

# printing result 

print("Match keys : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘CS’: {‘priceless’: 6}, ‘is’: {‘better’: 6,
> ‘educational’: 4}, ‘gfg’: {‘good’: 5, ‘best’: 4}, ‘Maths’: {‘good’: 5}}  
> Match keys : [‘gfg’, ‘Maths’]

