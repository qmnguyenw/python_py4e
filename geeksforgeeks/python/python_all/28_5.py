Python program to Sort Tuples by their Maximum element



Given a Tuple List sort tuples by maximum element in a tuple.

>  **Input** : test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]  
> **Output** : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 3, 7, 4), (1, 2)]  
> **Explanation** : 19 > 7 = 7 > 2, is order, hence reverse sorted by maximum
> element.
>
>  **Input** : test_list = [(4, 5, 5, 7), (19, 4, 5, 3), (1, 2)]  
> **Output** : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 2)]  
> **Explanation** : 19 > 7 > 2, is order, hence reverse sorted by maximum
> element.

**Method #1 : Using** **max()** **+** **sort()**

In this, we perform task of getting maximum element in tuple using max(), and
sort() operation is used to perform sort.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Tuples by Maximum element

# Using max() + sort()

 

# helper function

def get_max(sub):

 return max(sub)

 

# initializing list

test_list = [(4, 5, 5, 7), (1, 3, 7, 4),
(19, 4, 5, 3), (1, 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sort() is used to get sorted result

# reverse for sorting by max - first element's tuples

test_list.sort(key = get_max, reverse = True)

 

# printing result 

print("Sorted Tuples : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]  
> Sorted Tuples : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 3, 7, 4), (1, 2)]

 **Method #2 : Using sort() +** **lambda** **\+ reverse**

In this, we use similar functionality, the only difference here being use of
lambda fnc. rather than external function for task of getting reverse sorting.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Tuples by Maximum element

# Using sort() + lambda + reverse

 

# initializing list

test_list = [(4, 5, 5, 7), (1, 3, 7, 4),
(19, 4, 5, 3), (1, 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# lambda function getting maximum elements 

# reverse for sorting by max - first element's tuples

test_list.sort(key = lambda sub : max(sub), reverse = True)

 

# printing result 

print("Sorted Tuples : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]  
> Sorted Tuples : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 3, 7, 4), (1, 2)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

