Python – Extract Numerical Dictionary values



Sometimes, while working with Python Dictionaries, we can have a problem in
which we need to extract only if a particular key index is numeric value from
the dictionaries which are in form of strings. This can be desired in
applications in which we require to do preprocessing. Let’s discuss certain
ways in which this task can be performed.

>  **Input** : test_dict = {‘best’: [‘5′, ’35’, ‘geeks’], ‘CS’: [1, 2, 3],
> ‘Gfg’: [‘124’, ‘4’, ‘8’]}  
>  **Output** : [(‘5’, 1, ‘124’), (’35’, 2, ‘4’)]
>
>  **Input** : test_dict = {“Gfg” : [“4”], ‘best’ : [“6”], ‘CS’ : [1]}  
>  **Output** : [(‘6’, 1, ‘4’)]

 **Method #1 : Using loop +zip() + isdigit()**  
The combination of above functions can be used to perform this task. In this,
we check for numeric string using isdigit() and zip to perform the cumulation
of keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Numerical Dictionary values

# Using loop + zip() + isdigit()

 

# initializing dictionary

test_dict = {"Gfg" : ["34", "45", 'geeks'], 'is' :
["875", None, "15"], 'best' : ["98", 'abc',
'12k']}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Extract Numerical Dictionary values

# Using loop + zip() + isdigit()

res = []

for a, b, c in zip(*test_dict.values()):

 if a.isdigit() :

 res.append((a, b, c))

 

# printing result 

print("The Numerical values : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘Gfg’: [’34’, ’45’, ‘geeks’], ‘best’: [’98’,
> ‘abc’, ’12k’], ‘is’: [‘875′, None, ’15’]}  
> The Numerical values : [(’34’, ’98’, ‘875’), (’45’, ‘abc’, None)]

