Python – Extracting Key from Value Substring



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to find the key from given value, querying substring from key’s
value. This kind of problem is common and have application in many domains
including web development. Lets discuss certain ways in which this task can be
performed.

>  **Input** : test_dict = {1 : ‘Gfg is best’, 2 : ‘CS is best’}  
>  **Output** : [1, 2]
>
>  **Input** : test_dict = {1 : ‘best’}  
>  **Output** : [1]

 **Method #1 : Using loop +items()**  
The combination of above functionalities, can be used to solve this problem.
In this, we extract the dictionary values using items() and loop is used to
check for substring using “in” operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting Key from Value Substring

# Using loop + items()

 

# initializing dictionary

test_dict = {1 : 'Gfg is good', 2 : 'Gfg is best', 3
: 'Gfg is on top'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing search_word 

srch_wrd = 'best'

 

# Extracting Key from Value Substring

# Using loop + items()

res = []

for key, val in test_dict.items():

 if srch_wrd in val:

 res.append(key)

 

# printing result 

print("The Corresponding key : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {1: ‘Gfg is good’, 2: ‘Gfg is best’, 3: ‘Gfg is on
> top’}  
> The Corresponding key : [2]

