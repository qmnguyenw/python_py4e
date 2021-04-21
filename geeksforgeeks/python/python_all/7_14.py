Python – Conditional Join Dictionary List



Given 2 dictionaries list, the task is to write a Python program to perform
conditional join i.e add keys, based upon similarity of paricular key in
similar index dictionary.

 **Example:**

>  **Input :** test_list1 = [{“gfg” : 1, “is” : 3, “best”: 2}, {“gfg” : 1,
> “best” : 6}, {“all” : 7, “best” : 10} ],
>
> test_list2 = [{“good” : 4, “best”: 2}, {“geeks” : 2, “best” : 3 }, {“CS” :
> 2, “best” : 10 } ], test_key = “best”
>
>  **Output :** [{‘gfg’: 1, ‘is’: 3, ‘best’: 2, ‘good’: 4}, {‘gfg’: 1, ‘best’:
> 6}, {‘all’: 7, ‘best’: 10, ‘CS’: 2}]
>
>  
>
>
>  
>
>
>  **Explanation :** best has 2 in both dictionaries of 0th index, hence at
> index 0, dictionaries are merged.
>
>  **Input :** test_list1 = [{“gfg” : 1, “is” : 3, “best”: 3}, {“gfg” : 1,
> “best” : 6}, {“all” : 7, “best” : 10} ],
>
> test_list2 = [{“good” : 4, “best”: 2}, {“geeks” : 2, “best” : 3 }, {“CS” :
> 2, “best” : 10 } ], test_key = “best”
>
>  **Output :** [{‘gfg’: 1, ‘is’: 3, ‘best’: 3}, {‘gfg’: 1, ‘best’: 6},
> {‘all’: 7, ‘best’: 10, ‘CS’: 2}]
>
>  **Explanation :** best has 10 in both dictionaries of 2nd index, hence at
> index 2, dictionaries are merged.

 **Method : Using** **next()** **+** **update()**

In this, we use generator expression to check if dictionary’s key matches the
similar index dictionary key, if yes, then all the corresponding keys are
merged using update().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Conditional Join Dictionary List

# Using update() + next()

 

# initializing lists

test_list1 = [{"gfg": 1, "is": 3, "best": 2}, {

 "gfg": 1, "best": 6}, {"all": 7, "best":
10}]

test_list2 = [{"good": 4, "best": 2}, {

 "geeks": 2, "best": 3}, {"CS": 2, "best":
10}]

 

# printing original list

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing test key

test_key = "best"

 

for sub1 in test_list1:

 

 # checking for matching key

 temp = next(

 (itm for itm in test_list2 if sub1[test_key] ==
itm[test_key]), None)

 if(temp):

 

 # performing update

 sub1.update(temp)

 

# printing result

print("Joined result : " + str(test_list1))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [{‘gfg’: 1, ‘is’: 3, ‘best’: 2}, {‘gfg’: 1, ‘best’:
> 6}, {‘all’: 7, ‘best’: 10}]
>
> The original list 2 is : [{‘good’: 4, ‘best’: 2}, {‘geeks’: 2, ‘best’: 3},
> {‘CS’: 2, ‘best’: 10}]
>
> Joined result : [{‘gfg’: 1, ‘is’: 3, ‘best’: 2, ‘good’: 4}, {‘gfg’: 1,
> ‘best’: 6}, {‘all’: 7,
>
> ‘best’: 10, ‘CS’: 2}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

