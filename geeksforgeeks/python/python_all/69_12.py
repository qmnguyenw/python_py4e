Python – Filter index similar values



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract all the values in values lists that match the
filtered indices from matching values from list with some key in dictionary.
This kind of application can occur in web development.

>  **Input** : test_dict = {“Gfg” : [4, 5, 7], “is” : [5, 6, 8], “best” : [10,
> 7, 4]}  
>  **Output** : {“Gfg” : [4, 5, 7], “is” : [5, 6, 8], “best” : [10, 7, 4]}
>
>  **Input** : test_dict = {“Gfg” : [4, 20, 5, 7], “is” : [5, 17, 6, 8],
> “best” : [10, 11, 7, 4]}  
>  **Output** : {‘Gfg’: [4, 5, 7], ‘is’: [5, 6, 8], ‘best’: [10, 7, 4]}

 **Method #1 : Using loop +zip() + defaultdict()**  
The combination of above methods can be used to solve this problem. In this,
we initialize the defaultdict with list, bind all the keys with zip() and use
loop to append the required elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter index similar values

# Using loop + zip() + defaultdict()

from collections import defaultdict

 

# initializing dictionary

test_dict = {"Gfg" : [1, 4, 5, 6, 7], "is" :
[5, 6, 8, 9, 10], 

 "best" : [10, 7, 4, 11, 23]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing value list 

filt_list = [4, 5, 7]

 

# Filter index similar values

# Using loop + zip() + defaultdict()

res = defaultdict(list)

 

for x, y, z in zip(test_dict['Gfg'], test_dict['is'],
test_dict['best']):

 if x in filt_list:

 res['Gfg'].append(x)

 res['is'].append(y)

 res['best'].append(z)

 

# printing result 

print("The filtered dictionary : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘Gfg’: [1, 4, 5, 6, 7], ‘is’: [5, 6, 8, 9, 10],
> ‘best’: [10, 7, 4, 11, 23]}  
> The filtered dictionary : {‘Gfg’: [4, 5, 7], ‘is’: [6, 8, 10], ‘best’: [7,
> 4, 23]}

