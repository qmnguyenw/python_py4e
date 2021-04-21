Python – Associated Values Frequencies in Dictionary



Sometimes, while working with dictionaries, we can have problem in which we
need to compute the values associated to each value in dictionary in records
list. This kind of problem is peculiar, but can have application in
development domains. Lets discuss certain way in which this task can be
performed.

 **Method : Using nesteddefaultdict() + Counter()**  
The combination of above functions can be used to solve this problem. In this,
we use nested defaultdict to keep track of elements and counting of elements
is done by Counter().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Associated Values Frequencies in Dictionary

# Using defaultdict() + Counter()

from collections import defaultdict, Counter

 

# initializing list

test_list = [{'gfg' : 1, 'is' : 3, 'best' : 4},

 {'gfg' : 3, 'is' : 2, 'best' : 4}, 

 {'gfg' : 3, 'is' : 5, 'best' : 2},

 {'gfg' : 5, 'is' : 2, 'best' : 1},

 {'gfg' : 2, 'is' : 4, 'best' : 3},

 {'gfg' : 1, 'is' : 3, 'best' : 5},

 {'gfg' : 1, 'is' : 3, 'best' : 2}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Associated Values Frequencies in Dictionary

# Using defaultdict() + Counter()

res = defaultdict(Counter)

for sub in test_list:

 for key, val in sub.items():

 res[key][val] += 1

 

# printing result 

print("The list after Frequencies : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘gfg’: 1, ‘is’: 3, ‘best’: 4}, {‘gfg’: 3, ‘is’: 2,
> ‘best’: 4}, {‘gfg’: 3, ‘is’: 5, ‘best’: 2}, {‘gfg’: 5, ‘is’: 2, ‘best’: 1},
> {‘gfg’: 2, ‘is’: 4, ‘best’: 3}, {‘gfg’: 1, ‘is’: 3, ‘best’: 5}, {‘gfg’: 1,
> ‘is’: 3, ‘best’: 2}]  
> The list after Frequencies : {‘gfg’: Counter({1: 3, 3: 2, 2: 1, 5: 1}),
> ‘is’: Counter({3: 3, 2: 2, 4: 1, 5: 1}), ‘best’: Counter({2: 2, 4: 2, 1: 1,
> 3: 1, 5: 1})}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

