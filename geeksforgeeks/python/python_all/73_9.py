Python – Convert Frequency dictionary to list



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to construct the list out of the values of dictionary. This task
is reverse of finding frequency and has application in day-day programming and
web development domain. Let’s discuss certain ways in which this task can be
performed.

>  **Input :** test_dict = {‘gfg’ : 3, ‘ide’ : 2}  
>  **Output :** [‘gfg’, ‘gfg’, ‘gfg’, ‘ide’, ‘ide’]
>
>  **  
> Input :** test_dict = {‘practice’ : 1, ‘write’ : 2, ‘ide’ : 4}  
>  **Output :** [‘practice’, ‘write’, ‘write’, ‘ide’, ‘ide’, ‘ide’, ‘ide’]

 **Method #1 : Using loop**  
This is brute way to solve this problem. In this, we iterate for dictionary
and extract the frequency and replicate the elements at that frequency.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Frequency dictionary to list

# Using loop

 

# initializing dictionary

test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Convert Frequency dictionary to list

# Using loop

res = []

for key in test_dict:

 for idx in range(test_dict[key]):

 res.append(key)

 

# printing result 

print("The resultant list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘is’: 2, ‘best’: 5, ‘gfg’: 4}  
> The resultant list : [‘is’, ‘is’, ‘best’, ‘best’, ‘best’, ‘best’, ‘best’,
> ‘gfg’, ‘gfg’, ‘gfg’, ‘gfg’]

