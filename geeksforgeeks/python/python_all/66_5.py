Python – Paired Existance in Records



Sometimes, while working with Python records, we can have a problem in which
we need to check for paired existance inside the record, or else if one
doesn’t exist, other also should not. This kind of problem is common in
domains such as Data Science and web development. Let’s discuss certain ways
in which this task can be performed.

>  **Input** :  
> test_list = [(‘Gfg’, ‘is’, ‘Best’), (‘Gfg’, ‘is’, ‘good’), (‘CS’, ‘is’,
> ‘good’)]  
> pairs = (‘is’, ‘good’)  
>  **Output** : [(‘Gfg’, ‘is’, ‘good’), (‘CS’, ‘is’, ‘good’)]
>
>  **Input** :  
> test_list = [(‘Gfg’, ‘is’, ‘Best’), (‘Gfg’, ‘is’, ‘good’), (‘CS’, ‘is’,
> ‘better’)]  
> pairs = (‘better’, ‘good’)  
>  **Output** : []

 **Method #1 : Using generator expression**  
This is brute force way in which this task can be performed. In this, we check
for existance/non-existance of both numbers and accept the result if, none or
both are present.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Paired Existance in Records

# Using generator expression

 

# initializing list

test_list = [('Gfg', 'is', 'Best'),

 ('Gfg', 'is', 'good'), 

 ('CS', 'is', 'good')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Pairs 

pairs = ('Gfg', 'Best')

 

# Paired Existance in Records

# Using generator expression

res = []

for sub in test_list:

 if ((pairs[0] in sub and pairs[1] in sub) or (

 pairs[0] not in sub and pairs[1] not in sub)):

 res.append(sub)

 

# printing result 

print("The resultant records : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [(‘Gfg’, ‘is’, ‘Best’), (‘Gfg’, ‘is’, ‘good’), (‘CS’,
> ‘is’, ‘good’)]  
> The resultant records : [(‘Gfg’, ‘is’, ‘Best’), (‘CS’, ‘is’, ‘good’)]

