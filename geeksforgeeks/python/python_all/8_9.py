Python program to Mark duplicate elements in string



Given a list, the task is to write a Python program to mark the duplicate
occurrence of elements with progressive occurrence number.

>  **Input :** test_list = [‘gfg’, ‘is’, ‘best’, ‘gfg’, ‘best’, ‘for’, ‘all’,
> ‘gfg’]
>
>  **Output :** [‘gfg1’, ‘is’, ‘best1’, ‘gfg2’, ‘best2’, ‘for’, ‘all’, ‘gfg3’]
>
>  **Explanation :** gfg’s all occurrence are marked as it have multiple
> repetitions(3).
>
>  **Input :** test_list = [‘gfg’, ‘is’, ‘best’, ‘best’, ‘for’, ‘all’]
>
>  
>
>
>  
>
>
>  **Output :** [‘gfg’, ‘is’, ‘best1’, ‘best2’, ‘for’, ‘all’]
>
>  **Explanation :** best’s all occurrence are marked as it have multiple
> repetitions(2).

 **Method 1: Using** **count()** **+** **enumerate()** **+** **list
comprehension** **+** **slicing**

In this, in order to get the duplicate count, the list is sliced to current
element index, and count of occurrence of that element till current index is
computed using count() and append.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mark duplicate elements

# Using count() + enumerate() + list comprehension + slicing 

 

# initializing list

test_list = ["gfg", "is", "best", "gfg", 

 "best", "for", "all", "gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting count till current using count() and slicing

res = [val + str(test_list[:idx].count(val) + 1) if
test_list.count(val) > 1 else val for idx,

 val in enumerate(test_list)]

 

# printing result

print("Duplicates marked List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘is’, ‘best’, ‘gfg’, ‘best’, ‘for’, ‘all’,
> ‘gfg’]
>
> Duplicates marked List : [‘gfg1’, ‘is’, ‘best1’, ‘gfg2’, ‘best2’, ‘for’,
> ‘all’, ‘gfg3’]

 **Method 2: Using** **map()** **+** **count()** **+** **lambda**

Similar to the above method, the only difference being map() is used to get a
function using lambda to extend to whole list elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mark duplicate elements

# Using map() + count() + lambda

 

# initializing list

test_list = ["gfg", "is", "best", "gfg", 

 "best", "for", "all", "gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting count till current using count() and slicing

res = list(map(lambda ele: ele[1] + str(test_list[ :
ele[0]].count(ele[1]) + 1) if test_list.count(ele[1]) >
1 else ele[1],

 enumerate(test_list)))

 

# printing result

print("Duplicates marked List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘is’, ‘best’, ‘gfg’, ‘best’, ‘for’, ‘all’,
> ‘gfg’]
>
> Duplicates marked List : [‘gfg1’, ‘is’, ‘best1’, ‘gfg2’, ‘best2’, ‘for’,
> ‘all’, ‘gfg3’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

