Python – Scoring Matrix using Dictionary



Sometimes, while working with Python records, we can have a problem in which
we need to resolve scoring in Python Matrix records. This means mapping of
each key of dictionary with its value to aggregate score of each row. This
kind of problem can have applications in gaming and web development domains.
Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [[‘gfg’, ‘best’], [‘geeks’], [‘is’, ‘for’]]  
>  **Output** : [18, 15, 12]
>
>  **Input** : test_list = [[‘gfg’, ‘geeks’, ‘CS’]]  
>  **Output** : [20]

 **Method #1 : Using loop**  
This is one of the way in which this task can be performed. In this, we
iterate for the matrix elements and perform the values substitutions using
dictionary and perform row summations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Scoring Matrix using Dictionary

# Using loop

 

# initializing list

test_list = [['gfg', 'is', 'best'], ['gfg', 'is',
'for', 'geeks']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing test dict

test_dict = {'gfg' : 5, 'is' : 10, 'best' : 13,
'for' : 2, 'geeks' : 15}

 

# Scoring Matrix using Dictionary

# Using loop

res = []

for sub in test_list:

 sum = 0

 for val in sub:

 if val in test_dict:

 sum += test_dict[val]

 res.append(sum)

 

# printing result 

print("The Row scores : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]
    The Row scores : [28, 32]
    

