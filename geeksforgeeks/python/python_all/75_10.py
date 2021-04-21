Python – Sorted order Dictionary items pairing



Sometimes, while working with Python dictionaries, we can have problem in
which we need to perform reordering of dictionary items, to pair key and
values in sorted order, smallest pairing to smallest value, largest to largest
value and so on. This kind of application can occur in competitive domain and
day-day programming. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingzip() + sort() + keys() + values()**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of pairing using zip() and sorting is handled by
sort().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sorted order Dictionary items pairing

# Using zip() + sort() + keys() + values()

 

# initializing dictionary

test_dict = {45 : 3, 7 : 8, 98 : 4, 10 :
12, 65 : 90, 15 : 19}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sorted order Dictionary items pairing

# Using zip() + sort() + keys() + values()

vals = list(test_dict.values())

vals.sort()

keys = list(test_dict.keys())

keys.sort()

res = dict(zip(keys, vals))

 

# printing result 

print("The sorted order pairing : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {65: 90, 98: 4, 7: 8, 10: 12, 45: 3, 15: 19}
    The sorted order pairing : {65: 19, 98: 90, 7: 3, 10: 4, 45: 12, 15: 8}
    

**Method #2 : Usingmap() + values() + zip() + sorted()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of sorting using sorted(). The zip() and map() are used
for further pairing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sorted order Dictionary items pairing

# Using map() + values() + zip() + sorted()

 

# initializing dictionary

test_dict = {45 : 3, 7 : 8, 98 : 4, 10 :
12, 65 : 90, 15 : 19}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sorted order Dictionary items pairing

# Using map() + values() + zip() + sorted()

res = dict(zip(*map(sorted, (test_dict,
test_dict.values()))))

 

# printing result 

print("The sorted order pairing : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {65: 90, 98: 4, 7: 8, 10: 12, 45: 3, 15: 19}
    The sorted order pairing : {65: 19, 98: 90, 7: 3, 10: 4, 45: 12, 15: 8}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

