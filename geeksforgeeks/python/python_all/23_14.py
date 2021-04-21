Python program to Sort a List of Dictionaries by the Sum of their Values



Given Dictionary List, sort by summation of their values.

> **Input** : test_list = [{1 : 3, 4 : 5, 3 : 5}, {1 : 100}, {8 : 9, 7 : 3}]  
> **Output** : [{8: 9, 7: 3}, {1: 3, 4: 5, 3: 5}, {1: 100}]  
> **Explanation** : 12 < 13 < 100, sorted by values sum.
>
>  **Input** : test_list = [{1 : 100}, {8 : 9, 7 : 3}]  
> **Output** : [{8: 9, 7: 3}, {1: 100}]  
> **Explanation** : 12 < 100, sorted by values sum.

**Method #1 : Using** **sort()** **+** **sum()** **+** **values()**

In this, the task of performing sort is done using sort(), and sum() and
values() are used to get a summation of all the values of the dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionaries by Values Sum

# Using sort() + sum() + values()

 

def values_sum(row):

 

 # return values sum 

 return sum(list(row.values()))

 

# initializing list

test_list = [{1 : 3, 4 : 5, 3 : 5}, {1 :
7, 10 : 1, 3 : 10}, {1 : 100}, {8 : 9,
7 : 3}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort 

test_list.sort(key = values_sum)

 

# printing result 

print("Sorted Dictionaries List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{1: 3, 4: 5, 3: 5}, {1: 7, 10: 1, 3: 10}, {1: 100},
> {8: 9, 7: 3}]  
> Sorted Dictionaries List : [{8: 9, 7: 3}, {1: 3, 4: 5, 3: 5}, {1: 7, 10: 1,
> 3: 10}, {1: 100}]

 **Method #2 : Using** **sorted()** **+** **lambda** **\+ sum() + values()**

In this, we perform sort using sorted() and provide logic using lambda
function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionaries by Values Sum

# Using sorted() + lambda + sum() + values()

 

# initializing list

test_list = [{1 : 3, 4 : 5, 3 : 5}, {1 :
7, 10 : 1, 3 : 10}, {1 : 100}, {8 : 9,
7 : 3}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# lambda function to get values sum 

res = sorted(test_list, key = lambda row :
sum(list(row.values())))

 

# printing result 

print("Sorted Dictionaries List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{1: 3, 4: 5, 3: 5}, {1: 7, 10: 1, 3: 10}, {1: 100},
> {8: 9, 7: 3}]  
> Sorted Dictionaries List : [{8: 9, 7: 3}, {1: 3, 4: 5, 3: 5}, {1: 7, 10: 1,
> 3: 10}, {1: 100}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

