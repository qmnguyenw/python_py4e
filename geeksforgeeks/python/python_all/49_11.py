Python – Sort list of Single Item dictionaries according to custom ordering



Given single item dictionaries list and keys ordering list, perform sort of
dictionary according to custom keys.

>  **Input** : test_list1 = [{‘is’ : 4}, {“Gfg” : 10}, {“Best” : 1}],
> test_list2 = [“Gfg”, “is”, “Best”]  
>  **Output** : [{‘Gfg’: 10}, {‘is’: 4}, {‘Best’: 1}]  
>  **Explanation** : By list ordering, dictionaries list get sorted.
>
>  **Input** : test_list1 = [{“Gfg” : 10}, {‘is’ : 4}, {“Best” : 1}],
> test_list2 = [“Gfg”, “is”, “Best”]  
>  **Output** : [{‘Gfg’: 10}, {‘is’: 4}, {‘Best’: 1}]  
>  **Explanation** : Already ordered. No reordering required.

 **Method #1 : Using sorted() + index() + keys() + lambda**

The combination of above functionalities can be used to solve this problem. In
this, we perform sort using sorted(), index() is used to get ordering from
custom list, keys() used to extract the keys from dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort list of Single Item dictionaries according to custom ordering

# Using sorted() + index() + keys() + lambda 

 

# initializing lists

test_list1 = [{'is' : 4}, {'for' : 7}, {"Gfg" :
10}, {"Best" : 1}, {"CS" : 8}] 

test_list2 = ["Gfg", "is", "Best", "for", "CS"]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# sorted() used to perform sort(), returns the result

# to other variable, ordering handled using index() from order list

res = sorted(test_list1, key = lambda ele:
test_list2.index(list(ele.keys())[0]))

 

# printing result 

print("The custom order list : " + str(res))   
  
---  
  
__

__

**Output**

> The original list 1 is : [{‘is’: 4}, {‘for’: 7}, {‘Gfg’: 10}, {‘Best’: 1},
> {‘CS’: 8}]  
> The original list 2 is : [‘Gfg’, ‘is’, ‘Best’, ‘for’, ‘CS’]  
> The custom order list : [{‘Gfg’: 10}, {‘is’: 4}, {‘Best’: 1}, {‘for’: 7},
> {‘CS’: 8}]

 **Method #2 : Using sort() + index() + keys() + lambda**

This is yet another way in which this task can be performed. In this, we
perform the task of sorting using sort(), performs inplace sorting, other
constructs remain same.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort list of Single Item dictionaries according to custom ordering

# Using sort() + index() + keys() + lambda

 

# initializing lists

test_list1 = [{'is' : 4}, {'for' : 7}, {"Gfg" :
10}, {"Best" : 1}, {"CS" : 8}] 

test_list2 = ["Gfg", "is", "Best", "for", "CS"]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# sort() used to perform inplace sort

test_list1.sort(key = lambda ele:
test_list2.index(list(ele.keys())[0]))

 

# printing result 

print("The custom order list : " + str(test_list1))   
  
---  
  
__

__

**Output**

> The original list 1 is : [{‘is’: 4}, {‘for’: 7}, {‘Gfg’: 10}, {‘Best’: 1},
> {‘CS’: 8}]  
> The original list 2 is : [‘Gfg’, ‘is’, ‘Best’, ‘for’, ‘CS’]  
> The custom order list : [{‘Gfg’: 10}, {‘is’: 4}, {‘Best’: 1}, {‘for’: 7},
> {‘CS’: 8}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

