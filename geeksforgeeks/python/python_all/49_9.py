Python – Remove Duplicate Dictionaries characterized by Key



Given a list of dictionaries, remove all the dictionaries which are duplicate
with respect to K key.

>  **Input** : test_list = [{“Gfg” : 6, “is” : 9, “best” : 10}, {“Gfg” : 8,
> “is” : 11, “best” : 10}, {“Gfg” : 2, “is” : 16, “best” : 10}], K = “best”  
>  **Output** : [{“Gfg” : 6, “is” : 9, “best” : 10}]  
>  **Explanation** : All keys have 10 value, only 1st record is retained.
>
>  **Input** : test_list = [{“Gfg” : 6, “is” : 9, “best” : 10}, {“Gfg” : 8,
> “is” : 11, “best” : 12}, {“Gfg” : 2, “is” : 16, “best” : 15}], K = “best”  
>  **Output** : [{“Gfg” : 6, “is” : 9, “best” : 10}, {“Gfg” : 8, “is” : 11,
> “best” : 12}, {“Gfg” : 2, “is” : 16, “best” : 15}]  
>  **Explanation** : All values of “best” are unique, hence no removal of
> dictionaries.

 **Method : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
each dictionary and memoize the Key, if similar key’s same value occur, then
that dictionary is avoided in resultant list of dictionaries.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Duplicate Dictionaries characterized by Key

# Using loop

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing Key 

K = "best"

 

memo = set()

res = []

for sub in test_list:

 

 # testing for already present value

 if sub[K] not in memo:

 res.append(sub)

 

 # adding in memo if new value

 memo.add(sub[K])

 

# printing result 

print("The filtered list : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [{‘Gfg’: 6, ‘is’: 9, ‘best’: 10}, {‘Gfg’: 8, ‘is’: 11,
> ‘best’: 19}, {‘Gfg’: 2, ‘is’: 16, ‘best’: 10}, {‘Gfg’: 12, ‘is’: 1, ‘best’:
> 8}, {‘Gfg’: 22, ‘is’: 6, ‘best’: 8}]  
> The filtered list : [{‘Gfg’: 6, ‘is’: 9, ‘best’: 10}, {‘Gfg’: 8, ‘is’: 11,
> ‘best’: 19}, {‘Gfg’: 12, ‘is’: 1, ‘best’: 8}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

