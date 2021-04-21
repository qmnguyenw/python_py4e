Python – Remove dictionary from a list of dictionaries if a particular value
is not present



Given a list of dictionaries, remove all dictionaries which don’t have K as a
value.

 **Examples:**

>  **Input** : test_list = [{“Gfg” : 4, “is” : 8, “best” : 9}, {“Gfg” : 3,
> “is”: 7, “best” : 5}], K = 7  
> **Output** : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}]  
> **Explanation** : Resultant dictionary doesn’t contain 7 as any element.
>
>  **Input** : test_list = [{“Gfg” : 4, “is” : 7, “best” : 9}, {“Gfg” : 3,
> “is”: 7, “best” : 5}], K = 7  
> **Output** : []  
> **Explanation** : All contain 7 as element in List.  
>

**Method #1 : Using loop + values()**

  

  

This is one of the ways in which this task can be performed. In this, we
perform task of iterating for all the dictionaries using loop and check for
value presence using values().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove dictionary if K value not present

# Using loop + values()

 

# initializing lists

test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},

 {"Gfg" : 5, "is": 8, "best" : 1},

 {"Gfg" : 3, "is": 7, "best" : 6}, 

 {"Gfg" : 3, "is": 7, "best" : 5}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 7

 

res = []

 

# using loop to check for K element 

for sub in test_list:

 if K not in list(sub.values()):

 res.append(sub)

 

# printing result 

print("Filtered dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}, {‘Gfg’: 5, ‘is’: 8,
> ‘best’: 1}, {‘Gfg’: 3, ‘is’: 7, ‘best’: 6}, {‘Gfg’: 3, ‘is’: 7, ‘best’: 5}]  
> Filtered dictionaries : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}, {‘Gfg’: 5, ‘is’: 8,
> ‘best’: 1}]

 **Method #2 : Using list comprehension**

This is yet another way in which this task can be performed. In this, we
extract all the values using one-liner using list comprehension. The values
are extracted using values().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove dictionary if K value not present

# Using list comprehension

 

# initializing lists

test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},

 {"Gfg" : 5, "is": 8, "best" : 1},

 {"Gfg" : 3, "is": 7, "best" : 6}, 

 {"Gfg" : 3, "is": 7, "best" : 5}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 7

 

res = []

 

# using one-liner to extract dicts with NO K value

# using not in operator to check presence

res = [sub for sub in test_list if K not in
list(sub.values())]

 

# printing result 

print("Filtered dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}, {‘Gfg’: 5, ‘is’: 8,
> ‘best’: 1}, {‘Gfg’: 3, ‘is’: 7, ‘best’: 6}, {‘Gfg’: 3, ‘is’: 7, ‘best’: 5}]  
> Filtered dictionaries : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}, {‘Gfg’: 5, ‘is’: 8,
> ‘best’: 1}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

