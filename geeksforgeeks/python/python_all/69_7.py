Python – Change type of key in Dictionary list



Sometimes, while working with data, we can have a problem in which we require
to change the type of particular keys’ value in list of dictionary. This kind
of problem can have application in data domains. Lets discuss certain ways in
which this task can be performed.

>  **Input** : test_list = [{‘gfg’: 9, ‘best’: (7, 2), ‘is’: ‘4’}, {‘is’:
> ‘2’}]  
>  **Output** : [{‘gfg’: 9, ‘best’: (7, 2), ‘is’: 4}, {‘is’: 2}]
>
>  **Input** : test_list = [{‘is’ : ‘98393’}]  
>  **Output** : [{‘is’ : 98393}]

 **Method #1 : Using loop**  
This is brute force way to approach this problem. In this, we iterate for all
list elements and dictionary keys and convert the desired dictionary key’s
value to required type.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Change type of key in Dictionary list

# Using loop

 

# initializing list

test_list = [{'gfg' : 1, 'is' : '56', 'best' :
(1, 2)}, 

 {'gfg' : 5, 'is' : '12', 'best' : (6, 2)},

 {'gfg' : 3, 'is' : '789', 'best' : (7, 2)}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing change key 

chnge_key = 'is'

 

# Change type of key in Dictionary list

# Using loop

for sub in test_list:

 sub[chnge_key] = int(sub[chnge_key])

 

# printing result 

print("The converted Dictionary list : " + str(test_list))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘is’: ’56’, ‘gfg’: 1, ‘best’: (1, 2)}, {‘is’: ’12’,
> ‘gfg’: 5, ‘best’: (6, 2)}, {‘is’: ‘789’, ‘gfg’: 3, ‘best’: (7, 2)}]  
> The converted Dictionary list : [{‘is’: 56, ‘gfg’: 1, ‘best’: (1, 2)},
> {‘is’: 12, ‘gfg’: 5, ‘best’: (6, 2)}, {‘is’: 789, ‘gfg’: 3, ‘best’: (7, 2)}]

