Python – Merge Dictionaries List with duplicate Keys



Given two List of dictionaries with possible duplicate keys, write a Python
program to perform merge.

 **Examples:**

>  **Input** : test_list1 = [{“gfg” : 1, “best” : 4}, {“geeks” : 10, “good” :
> 15}, {“love” : “gfg”}], test_list2 = [{“gfg” : 6}, {“better” : 3, “for” :
> 10, “geeks” : 1}, {“gfg” : 10}]  
> **Output** : [{‘gfg’: 1, ‘best’: 4}, {‘geeks’: 10, ‘good’: 15, ‘better’: 3,
> ‘for’: 10}, {‘love’: ‘gfg’, ‘gfg’: 10}]  
> **Explanation** : gfg while merging retains value of 1, and “best” is added
> to dictionary as key from other list’s 1st dictionary ( same index ).  
>
>
> **Input** : test_list1 = [{“gfg” : 1, “best” : 4}, {“love” : “gfg”}],
> test_list2 = [{“gfg” : 6}, {“gfg” : 10}]  
> **Output** : [{‘gfg’: 1, ‘best’: 4}, {‘love’: ‘gfg’, ‘gfg’: 10}]  
> **Explanation** : gfg while merging retains value of 1, and “best” is added
> to dictionary as key from other list’s 1st dictionary ( same index ).

**Approach : Using loop +** **keys()**

  

  

In this we reconstruct the key value pair in accordance of all the keys not
recurring, checking using in operator and extracting keys using keys().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge Dictionaries List with duplicate Keys

# Using loop + keys()

 

# initializing lists

test_list1 = [{"gfg": 1, "best": 4}, {"geeks":
10, "good": 15},

 {"love": "gfg"}]

 

test_list2 = [{"gfg": 6}, {"better": 3, "for":
10, "geeks": 1},

 {"gfg": 10}]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

 

for idx in range(0, len(test_list1)):

 

 # getting keys of corresponding index

 id_keys = list(test_list1[idx].keys())

 for key in test_list2[idx]:

 

 # checking for keys presence

 if key not in id_keys:

 test_list1[idx][key] = test_list2[idx][key]

 

# printing result

print("The Merged Dictionary list : " + str(test_list1))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [{‘gfg’: 1, ‘best’: 4}, {‘geeks’: 10, ‘good’: 15},
> {‘love’: ‘gfg’}]  
> The original list 2 is : [{‘gfg’: 6}, {‘better’: 3, ‘for’: 10, ‘geeks’: 1},
> {‘gfg’: 10}]  
> The Merged Dictionary list : [{‘gfg’: 1, ‘best’: 4}, {‘geeks’: 10, ‘good’:
> 15, ‘better’: 3, ‘for’: 10}, {‘love’: ‘gfg’, ‘gfg’: 10}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

