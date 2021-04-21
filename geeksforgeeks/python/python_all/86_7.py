Python – Occurrence counter in List of Records



Sometimes, while dealing with records we can have a problem in which we need
count the occurrence of incoming digits corresponding to different
characters/players in a game and compile them in a dictionary. This can have
application in gaming and web development. Lets discuss a way in which this
can be done.

 **Method : Using loop +Counter()**  
The combination of above functions can be used to perform this task. In this,
we iterate for the elements and compute frequency using Counter() and unique
characters are mananged by keys of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Occurrence counter in List of Records

# using Counter() + loop

from collections import Counter

 

# Initializing list

test_list = [('Gfg', 1), ('Gfg', 2), ('Gfg', 3),
('Gfg', 1), ('Gfg', 2), ('is', 1), ('is', 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Occurrence counter in List of Records

# using Counter() + loop

res = {}

for key, val in test_list:

 res[key] = [val] if key not in res else res[key] +
[val]

 

res = {key: dict(Counter(val)) for key, val in res.items()}

 

# printing result 

print ("Mapped resultant dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(‘Gfg’, 1), (‘Gfg’, 2), (‘Gfg’, 3), (‘Gfg’, 1),
> (‘Gfg’, 2), (‘is’, 1), (‘is’, 2)]  
> Mapped resultant dictionary : {‘is’: {1: 1, 2: 1}, ‘Gfg’: {1: 2, 2: 2, 3:
> 1}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

