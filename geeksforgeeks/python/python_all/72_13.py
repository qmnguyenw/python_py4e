Python – Flatten Nested Keys



Sometimes, while working with Python data, we can have a problem in which we
need to perform the flattening of certain keys in nested list records. This
kind of problem occurs while data preprocessing. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop**  
This is brute force method to perform this task. In this, we construct new
dictionary by assigning base keys and then perform the flattening of inner key
elements using nested loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Nested Keys

# Using loop

 

# initializing list

test_list = [{'Gfg' : 1, 'id' : 1, 'data' :
[{'rating' : 7, 'price' : 4},

 {'rating' : 17, 'price' : 8}]}, 

 {'Gfg' : 1, 'id' : 2, 'data' : [{'rating' :
18, 'price' : 19}]}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Flatten Nested Keys

# Using loop

res = []

for sub in test_list:

 temp1 = {

 'Gfg': sub['Gfg'],

 'id': sub['id']

 }

 for data in sub.get('data', []):

 res.append({

 **temp1,

 'rating': data['rating'],

 'price': data['price']})

 

# printing result 

print("The flattened list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘data’: [{‘rating’: 7, ‘price’: 4}, {‘rating’: 17,
> ‘price’: 8}], ‘id’: 1, ‘Gfg’: 1}, {‘data’: [{‘rating’: 18, ‘price’: 19}],
> ‘id’: 2, ‘Gfg’: 1}]  
> The flattened list : [{‘price’: 4, ‘rating’: 7, ‘id’: 1, ‘Gfg’: 1},
> {‘price’: 8, ‘rating’: 17, ‘id’: 1, ‘Gfg’: 1}, {‘price’: 19, ‘rating’: 18,
> ‘id’: 2, ‘Gfg’: 1}]

  

  

**Method #2 : Using list comprehension + zip() + itemgetter()**  
The combination of above functions can be used to perform this task. In this,
we extract the required pairs using itemgetter() and combine pairs using
zip(). The compilation of data is using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Nested Keys

# Using list comprehension + zip() + itemgetter()

from operator import itemgetter

 

# initializing list

test_list = [{'Gfg' : 1, 'id' : 1, 'data' :
[{'rating' : 7, 'price' : 4},

 {'rating' : 17, 'price' : 8}]}, 

 {'Gfg' : 1, 'id' : 2, 'data' : [{'rating' :
18, 'price' : 19}]}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing base and flatten keys 

base_keys = 'Gfg', 'id'

flatten_keys = 'rating', 'price'

 

# Flatten Nested Keys

# Using list comprehension + zip() + itemgetter()

res = [dict(zip(base_keys + flatten_keys,
itemgetter(*base_keys)(sub) + itemgetter(*flatten_keys)(data)))
for sub in test_list for data in sub['data']]

 

# printing result 

print("The flattened list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘data’: [{‘rating’: 7, ‘price’: 4}, {‘rating’: 17,
> ‘price’: 8}], ‘id’: 1, ‘Gfg’: 1}, {‘data’: [{‘rating’: 18, ‘price’: 19}],
> ‘id’: 2, ‘Gfg’: 1}]  
> The flattened list : [{‘price’: 4, ‘rating’: 7, ‘id’: 1, ‘Gfg’: 1},
> {‘price’: 8, ‘rating’: 17, ‘id’: 1, ‘Gfg’: 1}, {‘price’: 19, ‘rating’: 18,
> ‘id’: 2, ‘Gfg’: 1}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

