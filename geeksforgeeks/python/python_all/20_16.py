Python Program to sort rows of a matrix by custom element count



Given Matrix, the following program shows how to sort rows of a matrix by the
count of presence of numbers from a specified list.

> **Input** : test_list = [[4, 5, 1, 7], [6, 5], [9, 8, 2], [7, 1]], cus_list
> = [4, 5, 7]  
> **Output** : [[9, 8, 2], [6, 5], [7, 1], [4, 5, 1, 7]]  
> **Explanation** : 0 < 1 = 1 < 3 is order of custom elements count.  
>  **Input** : test_list = [[4, 5, 1, 7], [6, 5], [7, 1]], cus_list = [4, 5,
> 7]  
> **Output** : [[6, 5], [7, 1], [4, 5, 1, 7]]  
> **Explanation** : 1 = 1 < 3 is order of custom elements count.  
>

**Method 1 :** _Using_ _sort()_ _and_ _len()_

In this, we perform in-place sort using sort(), and check for all elements and
increase counter in cases of element presence from custom list, len() returns
length to get count.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# sorting util.

def get_count(sub):

 return len([ele for ele in sub if ele in cus_list])

 

 

# initializing list

test_list = [[4, 5, 1, 7], [6, 5], [9, 8,
2], [7, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing custom list

cus_list = [4, 5, 7]

 

# performing inplace sort

test_list.sort(key=get_count)

 

# printing result

print("Sorted Matrix : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[4, 5, 1, 7], [6, 5], [9, 8, 2], [7, 1]]
>
> Sorted Matrix : [[9, 8, 2], [6, 5], [7, 1], [4, 5, 1, 7]]

 **Method 2 :** _Using_ _sorted()_ _,_ _lambda_ _and_ _len()_

Another way of solving this problem is to perform the task of sorting using
sorted() and lambda function offers one statement logic without calling
external function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[4, 5, 1, 7], [6, 5], [9, 8,
2], [7, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing custom list

cus_list = [4, 5, 7]

 

# performing sort using sorted()

res = sorted(test_list, key=lambda sub: len(

 [ele for ele in sub if ele in cus_list]))

 

# printing result

print("Sorted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 1, 7], [6, 5], [9, 8, 2], [7, 1]]
>
> Sorted Matrix : [[9, 8, 2], [6, 5], [7, 1], [4, 5, 1, 7]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

